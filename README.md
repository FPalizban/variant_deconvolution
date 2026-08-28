# Weakly supervised single-sample WGS deconvolution for pediatric leukemia

This repository contains the public code framework for a weakly supervised, single-sample whole-genome sequencing (WGS) variant-deconvolution and candidate-prioritization workflow for pediatric leukemia.

The framework was developed to analyze leukemia-derived blood/PBMC WGS when matched normal, remission, parental, fibroblast, or sorted-cell DNA is unavailable. It integrates variant-level evidence, allele-fraction structure, structural-variant proximity, biological annotation, and unrelated non-cancer control-background features to generate an interpretable, confidence-aware candidate map.


> **Important:** this repository does **not** contain controlled-access genomic data, patient-level clinical data, BAM/CRAM files, VCF files, or patient-level prediction outputs.

## Study overview

Matched normal DNA is particularly challenging to obtain in pediatric leukemia because blood and bone marrow can contain leukemic cells, limiting access to an uncontaminated constitutional comparator. The goal of this framework is not to replace matched-normal sequencing, but to provide a structured discovery approach for tumor-only leukemia WGS.

The workflow supports:

- weakly supervised variant-origin, biological-role, event-context, and confidence-tier prediction;
- use of unrelated non-cancer controls as a background-normalization layer, not as matched normals;
- structural-variant-proximity annotation from Manta or equivalent SV calls;
- retention and ranking of unresolved variants as an unknown-candidate discovery layer;
- evidence-layer ablation and leakage-aware benchmarking;
- external pediatric ALL catalog concordance analysis;
- publication-ready summary figures from aggregate/non-identifiable outputs.

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── CITATION.cff
├── LICENSE_TO_DISCUSS_WITH_PI_OR_INSTITUTION.txt
├── .gitignore
├── config/
│   └── example_config.yaml
├── scripts/
│   ├── 00_prepare_environment.sh
│   ├── 01_build_feature_matrix.py
│   ├── 02_train_multitask_deconvolution_model.py
│   ├── 03_compare_model_versions.py
│   ├── 04_unknown_candidate_prioritization.py
│   ├── 05_external_all_catalog_concordance.py

├── docs/
│   ├── data_privacy_and_availability.md
│   ├── method_overview.md
│   └── figure_guide.md
└── figures/
    └── README.md
```



## Minimal installation

```bash
python3 -m venv leukemia_wgs_env
source leukemia_wgs_env/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Example workflow

Edit `config/example_config.yaml` first, then run:

```bash
bash scripts/00_prepare_environment.sh
python scripts/01_build_feature_matrix.py --config config/example_config.yaml
python scripts/02_train_multitask_deconvolution_model.py --config config/example_config.yaml
python scripts/03_compare_model_versions.py --config config/example_config.yaml
python scripts/04_unknown_candidate_prioritization.py --config config/example_config.yaml
python scripts/05_external_all_catalog_concordance.py --config config/example_config.yaml
```

## Data availability

This repository provides code and documentation only. The pediatric leukemia WGS data and unrelated non-cancer control WGS data are not publicly redistributed because they contain controlled-access human genomic information. Users should adapt the workflow to authorized WGS datasets processed under their own institutional approvals.

## How to cite


## Contact

email: palizbanf@chop.edu
