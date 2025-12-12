"""Helpers for release workflows (changelog and draft parsing).

These helpers make the logic in the GitHub Actions workflow testable.
"""
from __future__ import annotations

from typing import Iterable, Mapping


def extract_changelog_section(changelog: str, version: str) -> str:
    """Extract the changelog section for a given version.

    If the exact `version` section is present (heading like ``## [1.2.3]``),
    return the contents under that heading until the next heading. If not
    present, return the `Unreleased` section if available. If neither is
    present, return an empty string.
    """
    lines = changelog.splitlines()
    target = f"## [{version}]"
    unreleased = "## [Unreleased]"

    def _extract(start_idx: int) -> str:
        out = []
        for line in lines[start_idx:]:
            if line.startswith("## [") and out:
                break
            out.append(line)
        return "\n".join(out).strip()

    # Search for exact version
    for i, line in enumerate(lines):
        if line.strip().startswith(target):
            return _extract(i + 1)

    # Fallback to Unreleased
    for i, line in enumerate(lines):
        if line.strip().startswith(unreleased):
            return _extract(i + 1)

    return ""


def find_draft_body_from_releases(releases: Iterable[Mapping]) -> str:
    """Return the body of a draft release (prefer no tag_name or 'Unreleased').

    Scans a list of release objects (as returned by GitHub API) and returns
    the body of the preferred draft release if found, otherwise an empty
    string.
    """
    for r in releases:
        if r.get("draft"):
            tag = r.get("tag_name") or ""
            name = (r.get("name") or "")
            # Prefer drafts without a tag name (Release Drafter uses empty tag_name)
            if not tag:
                return r.get("body") or ""
            if "Unreleased" in name or "Draft" in name:
                return r.get("body") or ""
    return ""
