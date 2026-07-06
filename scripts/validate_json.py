#!/usr/bin/env python3
"""Validate every JSON file parses, every schemas/*.json is a valid JSON Schema,
and every data file that names a research_program/project validates against its schema."""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parent.parent
errors = []

json_files = sorted(ROOT.rglob("*.json"))
parsed = {}
for path in json_files:
    if ".git" in path.parts:
        continue
    try:
        parsed[path] = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")

schema_dir = ROOT / "research-program" / "schemas"
for path, doc in parsed.items():
    if path.parent == schema_dir:
        try:
            Draft202012Validator.check_schema(doc)
        except Exception as e:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON Schema ({e})")

resolver = RefResolver(base_uri=schema_dir.as_uri() + "/", referrer={})


def validate_against(schema_name, instances_path, items_key=None):
    schema = json.loads((schema_dir / schema_name).read_text())
    validator = Draft202012Validator(schema, resolver=resolver)
    data = parsed.get(instances_path)
    if data is None:
        return
    items = data[items_key] if items_key else [data]
    for i, item in enumerate(items):
        for err in validator.iter_errors(item):
            errors.append(f"{instances_path.relative_to(ROOT)}[{i}]: {err.message}")


validate_against(
    "project.schema.json",
    ROOT / "research-program" / "data" / "sample-projects.json",
    items_key="projects",
)
validate_against(
    "research-program.schema.json",
    ROOT / "research-program" / "data" / "research-programs.json",
    items_key="programs",
)

if errors:
    print("JSON validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"OK: {len(json_files)} JSON files parse; schemas and sample data validate.")
