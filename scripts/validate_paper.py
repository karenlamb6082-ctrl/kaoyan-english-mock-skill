"""English I package v1.1 structural checks; never claims semantic truth."""
import argparse
import json
import math
import re
import sys
from pathlib import Path, PureWindowsPath
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SUPPORTED = {"$schema", "$defs", "$ref", "allOf", "title", "description", "type", "const",
             "enum", "minLength", "minimum", "maximum", "required", "properties",
             "additionalProperties", "items", "minItems", "maxItems", "minProperties"}
READING_TYPES = {"detail", "inference", "function", "meaning", "main_idea", "attitude"}
CLOZE_TYPES = {"lexical", "collocation_preposition", "logical_link", "syntax_grammar", "discourse_cohesion"}
DIFFICULTIES = {"predicted_easy", "predicted_medium", "predicted_hard"}
GATES = ["structure", "semantic", "source", "visual", "candidate"]
STAGES = ["DRAFT", "STRUCTURE_CHECKED", "SEMANTICALLY_REVIEWED", "SOURCE_VERIFIED",
          "VISUALLY_REVIEWED", "PILOT_READY", "EMPIRICALLY_REVIEWED"]

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError("Non-finite JSON: " + x)))

def schema_errors(value, node, schema, where="$"):
    errors = []
    unknown = set(node) - SUPPORTED
    if unknown:
        return [f"{where}: unsupported schema keywords: {sorted(unknown)}"]
    if "$ref" in node:
        name = node["$ref"]
        if not name.startswith("#/$defs/"):
            return [f"{where}: only local schema refs supported"]
        target = schema.get("$defs", {}).get(name[len("#/$defs/"):])
        return schema_errors(value, target, schema, where) if target else [f"{where}: missing schema ref"]
    for branch in node.get("allOf", []):
        errors.extend(schema_errors(value, branch, schema, where))
    types = node.get("type", [])
    types = [types] if isinstance(types, str) else types
    def matches(t):
        return {"object": isinstance(value, dict), "array": isinstance(value, list),
                "string": isinstance(value, str), "boolean": isinstance(value, bool),
                "null": value is None, "integer": type(value) is int,
                "number": type(value) in (int, float) and math.isfinite(value)}.get(t, False)
    if types and not any(matches(t) for t in types):
        return errors + [f"{where}: expected {types}, got {type(value).__name__}"]
    if "const" in node and (type(value) != type(node["const"]) or value != node["const"]):
        errors.append(f"{where}: invalid constant")
    if "enum" in node and value not in node["enum"]:
        errors.append(f"{where}: value outside allowed enum")
    if isinstance(value, str) and len(value.strip()) < node.get("minLength", 0):
        errors.append(f"{where}: empty/short string")
    if type(value) in (int, float):
        if value < node.get("minimum", -math.inf): errors.append(f"{where}: violates minimum")
        if value > node.get("maximum", math.inf): errors.append(f"{where}: violates maximum")
    if isinstance(value, list):
        if len(value) < node.get("minItems", 0) or len(value) > node.get("maxItems", math.inf):
            errors.append(f"{where}: wrong array length")
        if "items" in node:
            for i, item in enumerate(value): errors.extend(schema_errors(item, node["items"], schema, f"{where}[{i}]"))
    if isinstance(value, dict):
        if len(value) < node.get("minProperties", 0): errors.append(f"{where}: too few properties")
        for key in node.get("required", []):
            if key not in value: errors.append(f"{where}: missing {key}")
        for key, item in value.items():
            if key in node.get("properties", {}):
                errors.extend(schema_errors(item, node["properties"][key], schema, f"{where}.{key}"))
            elif node.get("additionalProperties") is False:
                errors.append(f"{where}: unknown property {key}")
            elif isinstance(node.get("additionalProperties"), dict):
                errors.extend(schema_errors(item, node["additionalProperties"], schema, f"{where}.{key}"))
    return errors

def word_count(text):
    text = re.sub(r"\{\{/?\d+\}\}", "", text)
    return len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text))

def local_asset(base, name):
    if Path(name).is_absolute() or PureWindowsPath(name).drive or "\\" in name:
        raise ValueError("asset must use portable relative forward-slash path")
    path = (Path(base) / name).resolve()
    if not path.is_relative_to(Path(base).resolve()):
        raise ValueError("asset escapes the paper directory")
    return path

def check_state(data):
    errors = []
    if not isinstance(data, dict): return ["state must be an object"]
    required = ("schema_version", "rules_version", "series_id", "next_paper", "history", "cooling",
                "quality_debt", "empirical", "pending_rule_changes")
    for key in required:
        if key not in data: errors.append("missing state field " + key)
    if errors: return errors
    if data["schema_version"] != "1.1": errors.append("unknown state schema version")
    if data["rules_version"] != "1.1.0": errors.append("state rules_version must be 1.1.0")
    if not isinstance(data["series_id"], str) or not data["series_id"].strip(): errors.append("invalid series_id")
    if type(data["next_paper"]) is not int or data["next_paper"] < 1: errors.append("invalid next_paper")
    for key in ("history", "quality_debt", "pending_rule_changes"):
        if not isinstance(data[key], list): errors.append(key + " must be array")
    cooling = data["cooling"]
    if not isinstance(cooling, dict) or cooling.get("next_writing_family") not in ("picture", "data"):
        errors.append("invalid cooling / writing family")
    empirical = data["empirical"]
    if not isinstance(empirical, dict) or empirical.get("status") not in ("none", "available"):
        errors.append("invalid empirical state")
    return errors

def validate(data, base):
    schema = read_json(ROOT / "PAPER_SCHEMA.json")
    errors = schema_errors(data, schema, schema)
    warnings, counts = [], {}
    if errors:
        return {"status": "FAIL", "errors": errors, "warnings": warnings, "word_counts": counts}
    def need(test, message):
        if not test: errors.append(message)
    def band(label, text, lo, hi):
        counts[label] = word_count(text); need(lo <= counts[label] <= hi, f"{label}: word count {counts[label]} outside {lo}-{hi}")
    def ids(items, wanted, label):
        need([q.get("id") for q in items] == list(wanted), label + ": wrong/duplicate/out-of-order question ids")

    sources = {s["id"]: s for s in data["sources"]}
    need(len(sources) == len(data["sources"]), "duplicate source ids")
    for s in data["sources"]:
        url = urlparse(s["url"]); need(url.scheme in ("https", "http") and bool(url.netloc), "invalid source URL: " + s["id"])
        if s["verification"] not in ("content_checked", "archived_snapshot", "user_provided"):
            warnings.append("source content not verified: " + s["id"])

    source_sections = [data["cloze"], *data["readings"], data["part_b"], data["translation"]]
    for section in source_sections:
        need(isinstance(section.get("source_ids"), list) and bool(section["source_ids"]), "section missing source_ids")
        for source_id in section.get("source_ids", []): need(source_id in sources, "missing referenced source " + source_id)
        need(section.get("voice_anchor_source_id") in section.get("source_ids", []), "voice anchor must be in source_ids")

    cloze = data["cloze"]; ids(cloze["questions"], range(1, 21), "cloze")
    marks = [int(x) for x in re.findall(r"\{\{(\d+)\}\}", cloze["text"])]
    need(marks == list(range(1, 21)), "cloze: need ordered markers {{1}} through {{20}}")
    band("cloze", cloze["text"], 240, 300)
    all_objective = list(cloze["questions"])
    for q in cloze["questions"]:
        need(q["construct"] in CLOZE_TYPES, f"Q{q['id']}: invalid cloze construct")

    need([r["id"] for r in data["readings"]] == [1, 2, 3, 4], "readings: ids must be 1..4")
    for i, reading in enumerate(data["readings"], 1):
        ids(reading["questions"], range(16 + i * 5, 21 + i * 5), f"text{i}")
        band(f"text{i}", " ".join(reading["paragraphs"]), 380, 430)
        need(len({q["answer"] for q in reading["questions"]}) >= 3, f"text{i}: fewer than 3 answer letters")
        for q in reading["questions"]: need(q["primary_type"] in READING_TYPES, f"Q{q['id']}: invalid primary_type")
        all_objective.extend(reading["questions"])
    need(len({r["domain"] for r in data["readings"]}) >= 3, "readings: fewer than three declared domains")

    for q in all_objective:
        need(q["options"][q["answer"]] == q["answer_text"], f"Q{q['id']}: answer_text/key mismatch")
        need(q["difficulty"] in DIFFICULTIES, f"Q{q['id']}: difficulty must remain predicted")
        need(q["strongest_distractor"] != q["answer"], f"Q{q['id']}: strongest distractor equals answer")
    sequence = "".join(q["answer"] for q in all_objective)
    need(not re.search(r"([ABCD])\1{3}", sequence), "answer sequence: run of 4 or more")
    for section in (cloze["questions"], *[r["questions"] for r in data["readings"]]):
        seq = "".join(q["answer"] for q in section)
        for period in (2, 3, 4, 5):
            for start in range(len(seq) - period * 3 + 1):
                need(seq[start:start+period*3] != seq[start:start+period] * 3, "answer sequence: periodic repeated block")
    if set(sequence[:20]) != set("ABCD"):
        warnings.append("cloze answer distribution omits a letter; release owner must justify or revise")
    absolute = re.compile(r"\b(always|only|completely|impossible|never|all|every|automatically)\b", re.I)
    absolute_hits = sum(bool(absolute.search(text)) for q in data["readings"] for item in q["questions"] for text in item["options"].values())
    if absolute_hits >= 8: warnings.append(f"reading distractors contain {absolute_hits} obvious absolute cues; semantic audit required")

    part_b = data["part_b"]; ids(part_b["items"], range(41, 46), "part_b")
    band("part_b", " ".join(part_b["body"]), 430, 550)
    for item in part_b["items"]:
        if part_b["display_mode"] == "prompts": need(bool(item["prompt"].strip()), f"Q{item['id']}: missing visible prompt")
        need(item["answer"] in part_b["choices"], f"Q{item['id']}: unavailable choice")
        if item["answer"] in part_b["choices"]: need(item["answer_text"] == part_b["choices"][item["answer"]], f"Q{item['id']}: answer_text mismatch")
    if part_b["display_mode"] == "inline":
        need([int(x) for x in re.findall(r"\{\{(\d+)\}\}", " ".join(part_b["body"]))] == list(range(41, 46)), "part_b: invalid inline slots")

    tr = data["translation"]; ids(tr["items"], range(46, 51), "translation")
    joined = " ".join(tr["paragraphs"]); band("translation", joined, 350, 450)
    spans = re.findall(r"\{\{(\d+)\}\}(.*?)\{\{/\1\}\}", joined, re.S)
    need([int(n) for n, _ in spans] == list(range(46, 51)), "translation: invalid/missing marked spans")
    remainder = re.sub(r"\{\{(\d+)\}\}(.*?)\{\{/\1\}\}", "", joined, flags=re.S)
    need("{{" not in remainder and "}}" not in remainder, "translation: unmatched or unexpected markers")
    for item in tr["items"]:
        found = [text for n, text in spans if int(n) == item["id"]]
        need(found == [item["text"]], f"Q{item['id']}: underline text mismatch")
        band(f"translation_{item['id']}", item["text"], 25, 35)
    band("writing_a_sample", data["writing_a"]["sample"], 90, 140)
    band("writing_b_sample", data["writing_b"]["sample"], 160, 200)

    visual = data["writing_b"]["visual"]
    try:
        asset = local_asset(base, visual["path"]); need(asset.is_file(), "visual asset missing")
        need(asset.suffix.lower() in (".png", ".jpg", ".jpeg"), "visual: only PNG/JPEG supported")
    except ValueError as ex: errors.append("visual: " + str(ex))
    if visual["family"] == "data": need(bool(visual["charts"]), "data family requires chart metadata")
    for chart in visual["charts"]:
        values = [row["value"] for row in chart["values"]]
        need(len(values) == len({row["label"] for row in chart["values"]}), "duplicate chart category")
        if chart["unit"] == "percent":
            need(all(0 <= x <= 100 for x in values), "percentage outside 0..100")
            if not chart["multiple_choice"]: need(abs(sum(values) - 100) <= chart["rounding_tolerance"], "single-choice chart total is not 100")
        elif chart["unit"] == "count":
            need(all(type(x) is int and 0 <= x <= chart["sample_size"] for x in values), "invalid count value")
            if not chart["multiple_choice"]: need(sum(values) == chart["sample_size"], "count total differs from sample_size")

    ledger = data["authoring"]["claim_ledger"]
    claim_types = {"SOURCE_FACT", "SOURCE_PARAPHRASE", "SUPPORTED_SYNTHESIS", "INVENTED_BRIDGE", "AUTHORIAL_INTERPRETATION"}
    need(bool(ledger), "claim ledger is empty")
    for i, claim in enumerate(ledger):
        need(isinstance(claim, dict), f"claim_ledger[{i}] must be object")
        if isinstance(claim, dict):
            for key in ("section", "location", "claim_type", "source_ids", "note"):
                need(bool(claim.get(key)), f"claim_ledger[{i}] missing {key}")
            need(claim.get("claim_type") in claim_types, f"claim_ledger[{i}] invalid claim_type")
            for source_id in claim.get("source_ids", []): need(source_id in sources, f"claim_ledger[{i}] missing source {source_id}")

    release = data["release"]; need(release["revision"] == data["meta"]["revision"], "release/meta revision mismatch")
    gates = {g["name"]: g for g in release["gates"]}; need(set(gates) == set(GATES) and len(release["gates"]) == len(GATES), "release must contain each gate exactly once")
    for name, gate in gates.items():
        if gate["status"] == "pass":
            need(bool(gate["reviewer"].strip()), f"{name} gate: pass without reviewer")
            need(bool(gate["timestamp"]), f"{name} gate: pass without timestamp")
            need(bool(gate["evidence"].strip()), f"{name} gate: pass without evidence")
            need(gate.get("reviewed_revision") == data["meta"]["revision"], f"{name} gate: evidence revision mismatch")
            if name == "semantic":
                need(gate.get("key_visible") is False, "semantic gate: blind solver must not see the key")
                need(gate["independence"] in ("independent", "fresh_context"), "semantic gate: independent or fresh-context review required")
    stage = release["stage"]; rank = STAGES.index(stage)
    if data["meta"]["example_only"]: need(rank <= 1, "example fixture cannot claim release review stages")
    if rank >= 2:
        pending = re.compile(r"migration placeholder|pending semantic review|not independently reviewed|legacy_unclassified", re.I)
        need(not pending.search(json.dumps(all_objective, ensure_ascii=False)), "semantic stage contains unresolved migration placeholders")
    if rank >= 3:
        for source in data["sources"]:
            need(source["verification"] in ("content_checked", "archived_snapshot"), "source stage requires content verification: " + source["id"])
            need(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", source["accessed"])), "source stage requires actual access date: " + source["id"])
    required_for_stage = {1: ["structure"], 2: ["structure", "semantic"], 3: ["structure", "semantic", "source"],
                          4: ["structure", "semantic", "source", "visual"],
                          5: ["structure", "semantic", "source", "visual"],
                          6: ["structure", "semantic", "source", "visual", "candidate"]}
    for gate_name in required_for_stage.get(rank, []): need(gates.get(gate_name, {}).get("status") == "pass", f"stage {stage} requires passed {gate_name} gate")
    if rank >= 5 and gates.get("semantic", {}).get("independence") == "not_independent":
        errors.append("PILOT_READY requires independent or fresh-context semantic review")
    if data["meta"]["example_only"]: warnings.append("structural fixture only; not a semantic benchmark")
    warnings.append("Machine checks do not prove source truth, natural grammar, unique answers, image/data match, visual quality, or exam equivalence.")
    return {"status": "FAIL" if errors else "STRUCTURE_PASS", "errors": errors, "warnings": warnings,
            "word_counts": counts, "answer_sequence": sequence, "declared_stage": stage}

def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("paper", type=Path); args = parser.parse_args()
    try: report = validate(read_json(args.paper), args.paper.resolve().parent)
    except (OSError, ValueError, KeyError, TypeError, RecursionError) as ex:
        report = {"status": "FAIL", "errors": [str(ex)], "warnings": []}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["status"] == "FAIL" else 0

if __name__ == "__main__": sys.exit(main())
