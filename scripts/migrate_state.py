"""Migrate a copied 1.0 series state to 1.1 without overwriting either file."""
import argparse
import json
import sys
from pathlib import Path

def migrate(data):
    if data.get("schema_version") == "1.1": return data
    if data.get("schema_version") != "1.0": raise ValueError("only state schema 1.0 can be migrated")
    out = dict(data); out["schema_version"] = "1.1"; out["rules_version"] = "1.1.0"
    cooling = dict(out.get("cooling", {}))
    cooling["part_b_recent_forms"] = cooling.pop("part_b_forms", [])
    cooling["policy"] = "轮换按最近最少使用，不永久排除题型。"
    out["cooling"] = cooling
    history = []
    for row in out.get("history", []):
        item = dict(row); item.setdefault("release_stage", "DRAFT"); history.append(item)
    out["history"] = history
    debt = list(out.get("quality_debt", []))
    note = "旧版成卷尚未通过1.1发布门禁；文件名不能替代审查状态"
    if note not in debt: debt.append(note)
    out["quality_debt"] = debt
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
