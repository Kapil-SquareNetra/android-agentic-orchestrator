#!/usr/bin/env python3
"""Validate android-agentic-orchestrator skill pack consistency."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills" / "android"
ORCH_REF = SKILLS / "android-orchestrator" / "references"
ORCH_SKILL = SKILLS / "android-orchestrator" / "SKILL.md"
INDEX = ROOT / "INDEX.md"
CURSOR_ROUTING = SKILLS / "android-orchestrator" / "assets" / "cursor-routing"
ROUTING_CASES = ROOT / "tests" / "routing_cases.yml"
LINK_RE = re.compile(r"\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
DEP_LINE_RE = re.compile(r"^- `?(android-[a-z0-9-]+)`?")
PHASE_SKILL_RE = re.compile(r"`(android-[a-z0-9-]+)`")
HUB_PHASE_ROW_RE = re.compile(r"^\| ([^|]+) \|")

sys.path.insert(0, str(ROOT / "scripts"))
from routing_resolve import (  # noqa: E402
    folder_for_alias,
    load_aliases_and_routing,
    resolve_file_skills,
    resolve_with_tasks,
)


def fail(errors: list[str]) -> None:
    for err in errors:
        print(f"ERROR: {err}", file=sys.stderr)
    sys.exit(1 if errors else 0)


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def alias_for_folder(aliases: dict[str, str], folder: str) -> str | None:
    for key, value in aliases.items():
        if value == folder:
            return key
    if folder.startswith("android-"):
        stem = folder.removeprefix("android-")
        if stem in aliases:
            return stem
    return None


def parse_skill_dependencies(skill_md: Path) -> set[str]:
    text = skill_md.read_text(encoding="utf-8")
    if "## Dependencies" not in text:
        return set()
    section = text.split("## Dependencies", 1)[1].split("## ", 1)[0]
    folders: set[str] = set()
    for line in section.splitlines():
        if " when " in line.lower():
            continue
        match = DEP_LINE_RE.match(line.strip())
        if match:
            folders.add(match.group(1))
    return folders


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def check_famwise() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if path == Path(__file__).resolve():
            continue
        if path.is_file() and path.suffix in {".md", ".mdc", ".yml", ".yaml"}:
            if "FamWise" in path.read_text(encoding="utf-8", errors="replace"):
                errors.append(f"FamWise leak in {path.relative_to(ROOT)}")
    return errors


def check_paths_frontmatter() -> list[str]:
    errors: list[str] = []
    for skill_md in SKILLS.glob("android-*/SKILL.md"):
        text = skill_md.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if m and re.search(r"^paths:\s*$", m.group(1), re.MULTILINE):
            errors.append(f"paths: frontmatter still present in {skill_md.relative_to(ROOT)}")
    return errors


def check_spoke_frontmatter() -> list[str]:
    errors: list[str] = []
    for skill_md in SKILLS.glob("android-*/SKILL.md"):
        if skill_md.parent.name == "android-orchestrator":
            continue
        fm = parse_frontmatter(skill_md)
        if fm.get("disable-model-invocation") is not True:
            errors.append(f"{skill_md.relative_to(ROOT)}: spokes must set disable-model-invocation: true")
        if fm.get("name") != skill_md.parent.name:
            errors.append(
                f"{skill_md.relative_to(ROOT)}: name {fm.get('name')} != folder {skill_md.parent.name}"
            )
    return errors


def check_cursor_routing_removed() -> list[str]:
    if CURSOR_ROUTING.exists():
        return [f"Remove deprecated {CURSOR_ROUTING.relative_to(ROOT)}/"]
    return []


def check_routing_yaml() -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    file_routing = load_yaml(ORCH_REF / "file-routing.yml")
    aliases: dict[str, str] = file_routing.get("skill_aliases", {})
    routing = file_routing.get("routing", {})

    skills_dir = {p.name for p in SKILLS.iterdir() if p.is_dir() and p.name.startswith("android-")}

    for alias, folder in aliases.items():
        if folder not in skills_dir:
            errors.append(f"Alias {alias} -> {folder} but folder missing")

    for pattern, alias_list in routing.items():
        if not isinstance(alias_list, list):
            errors.append(f"Route {pattern} must be a list of aliases")
            continue
        resolved: list[str] = []
        for alias in alias_list:
            folder = folder_for_alias(aliases, alias)
            if folder not in skills_dir:
                errors.append(f"Route {pattern}: unknown alias {alias} -> {folder}")
            resolved.append(folder)
        if len(resolved) != len(set(resolved)):
            errors.append(f"Route {pattern} lists aliases that resolve to the same skill")

    task_data = load_yaml(ORCH_REF / "task-routing.yml")
    for task_name, entry in (task_data.get("tasks") or {}).items():
        for alias in entry.get("skills", []):
            folder = folder_for_alias(aliases, alias)
            if folder not in skills_dir:
                errors.append(f"task-routing {task_name}: unknown alias {alias} -> {folder}")

    try:
        load_yaml(ORCH_REF / "skill-dependencies.yml")
    except yaml.YAMLError as exc:
        errors.append(f"skill-dependencies.yml parse error: {exc}")

    return aliases, errors


def check_routing_cases() -> list[str]:
    errors: list[str] = []
    if not ROUTING_CASES.exists():
        return errors
    data = load_yaml(ROUTING_CASES)
    for case in data.get("cases", []):
        path = case["path"]
        expected = sorted(case["skills"])
        actual = resolve_file_skills(path)
        if actual != expected:
            errors.append(f"routing case {path}: expected {expected}, got {actual}")
    for case in data.get("task_cases", []):
        path = case["path"]
        tasks = case.get("tasks", [])
        expected = sorted(case["skills"])
        actual = resolve_with_tasks(path, tasks)
        if actual != expected:
            errors.append(f"task routing case {path} {tasks}: expected {expected}, got {actual}")
    return errors


def extract_hub_phase_skills() -> dict[str, set[str]]:
    text = ORCH_SKILL.read_text(encoding="utf-8")
    block = text.split("### Phase skill loads (mandatory)", 1)[1].split("Spokes use", 1)[0]
    phases: dict[str, set[str]] = {}
    for line in block.splitlines():
        if not line.startswith("|") or "Phase" in line or line.startswith("|-------"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        phase = cells[0]
        skills = set(PHASE_SKILL_RE.findall(cells[1]))
        phases[phase] = skills
    return phases


def extract_index_phase_skills() -> dict[str, set[str]]:
    text = INDEX.read_text(encoding="utf-8")
    block = text.split("## Phase → which spokes to load", 1)[1].split("## Skill catalog", 1)[0]
    phases: dict[str, set[str]] = {}
    for line in block.splitlines():
        if not line.startswith("|") or "Phase" in line or line.startswith("|-------"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        phase = cells[0]
        skills = set(PHASE_SKILL_RE.findall(cells[1]))
        phases[phase] = skills
    return phases


def check_index_hub_phase_parity() -> list[str]:
    errors: list[str] = []
    hub = extract_hub_phase_skills()
    index = extract_index_phase_skills()
    if hub.keys() != index.keys():
        errors.append(f"Phase names differ: hub {sorted(hub)} vs INDEX {sorted(index)}")
    for phase in hub:
        if phase in index and hub[phase] != index[phase]:
            errors.append(f"Phase {phase} skills differ: hub {sorted(hub[phase])} vs INDEX {sorted(index[phase])}")
    return errors


def check_skill_dependencies_yml(aliases: dict[str, str]) -> list[str]:
    errors: list[str] = []
    data = load_yaml(ORCH_REF / "skill-dependencies.yml")
    deps_map: dict = data.get("dependencies", {})

    for alias, entry in deps_map.items():
        folder = folder_for_alias(aliases, alias)
        skill_md = SKILLS / folder / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"skill-dependencies key {alias}: no {skill_md}")
            continue

        expected_aliases = set(entry.get("requires", []))
        spoken_folders = parse_skill_dependencies(skill_md)
        spoken_aliases = set()
        for folder_name in spoken_folders:
            a = alias_for_folder(aliases, folder_name)
            if a:
                spoken_aliases.add(a)
            else:
                errors.append(f"{skill_md.relative_to(ROOT)}: unknown dep {folder_name}")

        if spoken_aliases != expected_aliases:
            errors.append(
                f"{folder}/SKILL.md deps {sorted(spoken_aliases)} "
                f"!= skill-dependencies.yml {alias} requires {sorted(expected_aliases)}"
            )

    return errors


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".mdc"}:
            continue
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            link_path = target.split("#", 1)[0]
            if not link_path:
                continue
            resolved = (path.parent / link_path).resolve()
            if not resolved.exists():
                errors.append(f"Broken link in {path.relative_to(ROOT)}: {target}")
    return errors


def main() -> None:
    errors: list[str] = []
    errors.extend(check_famwise())
    errors.extend(check_paths_frontmatter())
    errors.extend(check_spoke_frontmatter())
    errors.extend(check_cursor_routing_removed())
    aliases, routing_errors = check_routing_yaml()
    errors.extend(routing_errors)
    errors.extend(check_routing_cases())
    errors.extend(check_index_hub_phase_parity())
    errors.extend(check_skill_dependencies_yml(aliases))
    errors.extend(check_markdown_links())

    if errors:
        fail(errors)
    print("validate_pack: OK")


if __name__ == "__main__":
    main()
