"""Migrate a 1.0 paper record to a 1.1 structural draft; never grants review status."""
import argparse
import copy
import json
import sys
from pathlib import Path

LETTERS = "ABCD"
def other(answer): return next(x for x in LETTERS if x != answer)

def migrate(data):
    if data.get("schema_version") == "1.1": return copy.deepcopy(data)
    if data.get("schema_version") != "1.0": raise ValueError("only paper schema 1.0 can be migrated")
    out = copy.deepcopy(data); out["schema_version"] = "1.1"
    out["meta"]["revision"] += "-migrated-1.1"
    for source in out["sources"]:
        source.setdefault("author", None); source.setdefault("accessed", "unknown")
        source["verification"] = "unverified"
        source.setdefault("voice", "historical adaptation")
        source.setdefault("rights_note", "Structural fixture only; verify third-party rights before redistribution.")
        source.setdefault("snapshot_hash", None)
    sections = [out["cloze"], *out["readings"], out["part_b"], out["translation"]]
    for section in sections:
        source_id = section.pop("source_id")
        section["source_ids"] = [source_id]; section["voice_anchor_source_id"] = source_id
    for q in out["cloze"]["questions"]:
        q.setdefault("traps", ["Pending semantic review."] * 4)
        label = q.get("construct", "")
        q["construct"] = ("syntax_grammar" if "被动" in label else "logical_link" if "逻辑" in label or "转折" in label
                          else "discourse_cohesion" if "衔接" in label or "照应" in label else "collocation_preposition" if "搭配" in label else "lexical")
        q["secondary_operation"] = label or "legacy_unclassified"
        q["evidence_span"] = q.get("evidence", "legacy evidence")
        q["difficulty"] = "predicted_medium"
        q["strongest_distractor"] = other(q["answer"])
        q["strongest_distractor_case"] = "Migration placeholder; fresh adversarial review required."
        q["decisive_boundary"] = "Migration placeholder; not semantically approved."
        q["substitution_review"] = {x: "Not independently reviewed after migration." for x in LETTERS}
    for reading in out["readings"]:
        for q in reading["questions"]:
            label = q.pop("construct", "")
            if "主旨" in label or "标题" in label: primary = "main_idea"
            elif "态度" in label: primary = "attitude"
            elif "功能" in label or "例" in label: primary = "function"
            elif "语义" in label or "句意" in label: primary = "meaning"
            elif "细节" in label or "定位" in label: primary = "detail"
            else: primary = "inference"
            q["primary_type"] = primary; q["secondary_operation"] = label or "legacy_unclassified"
            q["evidence_span"] = q["evidence"]
            q["difficulty"] = "predicted_" + q.get("difficulty", "medium").replace("predicted_", "")
            q["strongest_distractor"] = other(q["answer"])
            q["strongest_distractor_case"] = "Migration placeholder; fresh adversarial review required."
            q["decisive_boundary"] = "Migration placeholder; not semantically approved."
    out["authoring"] = {
        "steelman": {"support": "Historical record migrated for structural testing.", "oppose": "No 1.1 independent review has been completed.", "decisive_variables": ["fresh blind review", "source audit", "candidate data"]},
        "claim_ledger": [{"section": "legacy_fixture", "location": "whole record", "claim_type": "SOURCE_PARAPHRASE", "source_ids": [s["id"] for s in out["sources"]], "note": "Legacy metadata only; rebuild paragraph-level mapping before release."}],
        "ecosystem": [{"section": "legacy_fixture", "status": "requires fresh audit"}],
        "exceptions": ["Migrated example is a structural fixture, not a releasable paper."]
    }
    out["release"] = {"stage": "DRAFT", "revision": out["meta"]["revision"], "gates": [
        {"name": name, "status": "not_run", "reviewer": "", "independence": "not_applicable", "timestamp": None, "evidence": ""}
        for name in ("structure", "semantic", "source", "visual", "candidate")],
        "known_limitations": ["Migrated historical fixture; all 1.1 review gates remain not_run."]}
    out.pop("qa", None)
    return out

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("source", type=Path); parser.add_argument("destination", type=Path); args = parser.parse_args()
    if args.destination.exists(): raise FileExistsError("destination exists; migration never overwrites")
    data = json.loads(args.source.read_text(encoding="utf-8-sig")); out = migrate(data)
    args.destination.parent.mkdir(parents=True, exist_ok=True)
    args.destination.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(args.destination)
    return 0

if __name__ == "__main__": sys.exit(main())
