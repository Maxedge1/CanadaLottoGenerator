# CanadaLottoGenerator

[![CI](https://github.com/Maxedge1/CanadaLottoGenerator/actions/workflows/ci.yml/badge.svg)](https://github.com/Maxedge1/CanadaLottoGenerator/actions/workflows/ci.yml)
[![Release](https://github.com/Maxedge1/CanadaLottoGenerator/actions/workflows/release.yml/badge.svg)](https://github.com/Maxedge1/CanadaLottoGenerator/actions/workflows/release.yml)

Small Python package and CLI to generate Canadian-style lotto numbers.

Usage:

Generate a single draw:

```bash
python -m canada_lotto_generator
```

Generate 3 draws with a bonus ball, as JSON:

```bash
python -m canada_lotto_generator -n 3 --bonus --format json
```

Use presets and seed for deterministic draws:

```bash
python -m canada_lotto_generator --preset 649 --seed 42
```

Run tests locally:

```bash
python -m pytest
```

Docker:

```bash
docker build -t canada-lotto .
# Run the CLI inside a container
docker run --rm canada-lotto -n 3 --preset 649
```

Continuous Integration:

CI is defined in `.github/workflows/ci.yml` which runs tests on Python 3.10-3.12. The release workflow is in `.github/workflows/release.yml` and publishes on tag push `v*` using the `PYPI_API_TOKEN` secret (create it in repository Settings → Secrets).

Coverage: [![Codecov](https://codecov.io/gh/Maxedge1/CanadaLottoGenerator/branch/main/graph/badge.svg)](https://codecov.io/gh/Maxedge1/CanadaLottoGenerator)

Docs: [![Docs](https://github.com/Maxedge1/CanadaLottoGenerator/workflows/Docs/badge.svg)](https://github.com/Maxedge1/CanadaLottoGenerator/actions?query=workflow%3ADocs)

Dependabot: [![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=Maxedge1/CanadaLottoGenerator)](https://github.com/Maxedge1/CanadaLottoGenerator/security/dependabot)
