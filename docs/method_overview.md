# Method overview

The workflow is organized around five evidence layers:

1. Variant-level read evidence and technical QC.
2. Allele-fraction structure.
3. Structural-variant proximity.
4. Biological and clinical annotation.
5. Unrelated non-cancer control-background normalization.

The model predicts weak-label tasks for variant origin, biological role, event context, and confidence tier. Ambiguous variants are retained as an unknown discovery layer rather than discarded.
