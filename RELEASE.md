# Releasing

This project uses a tag-based release workflow. Push a tag like `v0.1.0` to trigger building artifacts and creating a GitHub Release with the built distributions attached.

Secrets required for releases:
- `PYPI_API_TOKEN` (create in repository Secrets) — used by the release workflow to publish to PyPI.
- `GITHUB_TOKEN` (provided by Actions) — used to create GitHub Releases and upload assets. Ensure the token has appropriate `contents` permissions if using a fine-grained PAT.

Note: The repository is configured with two tag-triggered workflows:
- `.github/workflows/release.yml` — builds and publishes to PyPI on tag push.
- `.github/workflows/tag-release.yml` — builds, creates a GitHub Release (using the changelog as the body), uploads artifacts, and publishes to PyPI if `PYPI_API_TOKEN` is present.

How the release body is generated:
- On tag push the workflow extracts the matching `## [<version>]` section from `CHANGELOG.md` (falls back to `## [Unreleased]` if missing) and uses that text as the release body.

Recommended steps:
1. Update `CHANGELOG.md` under a `## [<version>]` heading.
2. Commit the changelog and push a tag, e.g. `git tag v0.1.0 && git push origin v0.1.0`.

If you need automated release notes drafting, Release Drafter is configured to help create draft release notes from merged PRs.
