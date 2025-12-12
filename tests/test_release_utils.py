from canada_lotto_generator.release import (
    extract_changelog_section,
    find_draft_body_from_releases,
)


SAMPLE_CHANGELOG = """
# Changelog

## [Unreleased]
- Upcoming change A

## [0.2.0]
- Added feature X

## [0.1.0]
- Initial release
"""


def test_extract_exact_version():
    s = extract_changelog_section(SAMPLE_CHANGELOG, "0.2.0")
    assert "Added feature X" in s


def test_extract_unreleased_when_missing_version():
    s = extract_changelog_section(SAMPLE_CHANGELOG, "9.9.9")
    assert "Upcoming change A" in s


def test_extract_empty_when_no_sections():
    s = extract_changelog_section("# Empty\nNo sections here", "1.0.0")
    assert s == ""


def test_find_draft_prefers_no_tag_name():
    releases = [
        {"draft": True, "tag_name": "v0.1.0", "body": "draft 1"},
        {"draft": True, "tag_name": "", "body": "drafter body"},
    ]
    assert find_draft_body_from_releases(releases) == "drafter body"


def test_find_draft_prefers_unreleased_name():
    releases = [
        {"draft": True, "tag_name": "v0.1.0", "name": "Unreleased Draft", "body": "unreleased body"},
    ]
    assert find_draft_body_from_releases(releases) == "unreleased body"


def test_find_draft_none():
    releases = [{"draft": False, "tag_name": "v0.1.0", "body": "x"}]
    assert find_draft_body_from_releases(releases) == ""
