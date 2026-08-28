#!/usr/bin/env python3
"""
Unknown candidate prioritization

This is a publication-safe scaffold script. Replace placeholder functions with the
project-specific implementation before release, and do not hard-code private paths
or patient identifiers.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import yaml


def load_config(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank unresolved variants and genes as a discovery layer.")
    parser.add_argument("--config", required=True, help="Path to YAML config file.")
    args = parser.parse_args()

    cfg = load_config(args.config)
    outdir = Path(cfg.get("outputs", {}).get("outdir", "results/public_example_output"))
    outdir.mkdir(parents=True, exist_ok=True)

    print("Prioritizing unknown candidates placeholder...")
    print(f"Output directory: {outdir}")

    # TODO: add implementation here.
    # Keep controlled-access data outside the repository.
    # Export only aggregate, non-identifiable outputs for public release.


if __name__ == "__main__":
    main()
