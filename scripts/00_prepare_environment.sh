#!/usr/bin/env bash
set -euo pipefail

echo "Checking Python environment..."
python --version
python - <<'PYCHECK'
import numpy, pandas, sklearn, matplotlib, yaml
print("Core packages loaded successfully.")
PYCHECK

echo "Environment check complete."
