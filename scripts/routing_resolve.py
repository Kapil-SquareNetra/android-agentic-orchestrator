#!/usr/bin/env python3
"""Resolve file paths to skill folders using file-routing.yml."""

from __future__ import annotations

import fnmatch
from pathlib import Path

import yaml

ORCH_REF = Path(__file__).resolve().parents[1] / "skills" / "android" / "android-orchestrator" / "references"


def load_aliases_and_routing() -> tuple[dict[str, str], dict[str, list[str]]]:
    data = yaml.safe_load((ORCH_REF / "file-routing.yml").read_text(encoding="utf-8"))
    return data["skill_aliases"], data["routing"]


def folder_for_alias(aliases: dict[str, str], alias: str) -> str:
    return aliases.get(alias, f"android-{alias}")


def _match_glob_parts(pattern_parts: list[str], path_parts: list[str]) -> bool:
    if not pattern_parts:
        return not path_parts
    head, *tail = pattern_parts
    if head == "**":
        if not tail:
            return True
        for skip in range(len(path_parts) + 1):
            if _match_glob_parts(tail, path_parts[skip:]):
                return True
        return False
    if not path_parts:
        return False
    if not fnmatch.fnmatchcase(path_parts[0], head):
        return False
    return _match_glob_parts(tail, path_parts[1:])


def path_matches(pattern: str, rel_path: str) -> bool:
    path = rel_path.replace("\\", "/").strip("/")
    pat = pattern.replace("\\", "/").strip("/")
    if not path or not pat:
        return path == pat
    return _match_glob_parts(pat.split("/"), path.split("/"))


def resolve_file_skills(rel_path: str) -> list[str]:
    """Return sorted unique android-* folder names for a repo-relative path."""
    aliases, routing = load_aliases_and_routing()
    path = rel_path.replace("\\", "/").lstrip("/")
    matched: set[str] = set()
    for pattern, alias_list in routing.items():
        if path_matches(pattern, path):
            for alias in alias_list:
                matched.add(folder_for_alias(aliases, alias))
    return sorted(matched)


def resolve_with_tasks(rel_path: str, task_keys: list[str]) -> list[str]:
    skills = set(resolve_file_skills(rel_path))
    task_data = yaml.safe_load((ORCH_REF / "task-routing.yml").read_text(encoding="utf-8"))
    aliases, _ = load_aliases_and_routing()
    tasks = task_data.get("tasks", {})
    for key in task_keys:
        entry = tasks.get(key, {})
        for alias in entry.get("skills", []):
            skills.add(folder_for_alias(aliases, alias))
    return sorted(skills)
