# LIDC 3D Zernike — Pulmonary Nodule Morphology Analysis

Research code and selected reproducibility evidence accompanying the manuscript:

**Three-Dimensional Zernike Spectral Descriptors for Quantitative Pulmonary Nodule Morphology Analysis**

Author and software copyright holder: **Chia-Hung Wei**  
License: **MIT** (original project code only)

## Scope and reproducibility

This repository contains a portable **synthetic surface-versus-volume** Zernike experiment, archived outputs and comparison evidence, and selected clinical analysis scripts. It does **not** include the original LIDC-IDRI CT images or a fully independent clinical end-to-end reproduction environment.

For the previously completed Windows synthetic reproduction, three regenerated CSV outputs matched the reference archives exactly: **1,224** matched-descriptor rows, **102** aggregate rows and **12** summary rows. The archived summary has also been independently recalculated from matched descriptors (12 Spearman coefficients, maximum difference approximately **1.11 × 10⁻¹⁶**). These claims apply to the synthetic experiment only, not to every clinical analysis.

## Repository contents

| Path | Purpose |
| --- | --- |
| `run_synthetic.py` | Entrypoint for the full continuous point-sampled synthetic experiment |
| `portable/` | Synthetic Zernike experiment implementation |
| `tests/` | Smoke test, comparison tool and archived-summary validator |
| `evidence/` | Original archived synthetic results and verification evidence |
| `legacy_scripts/` | Selected clinical analysis and figure-generation scripts; **not a standalone clinical pipeline** |
| `requirements.txt` | Python dependencies |
| `CITATION.cff` / `LICENSE` | Citation metadata and software license |

Figure 1 of the manuscript is a schematic and requires no numerical data reproduction.

## Requirements and synthetic experiment

Recommended environment: Python 3.11 (the archived Windows run used Python 3.11.5 and SciPy 1.11.1). From the repository root:

```bash
python -m pip install -r requirements.txt
python run_synthetic.py
```

`run_synthetic.py` runs 3 shape families × 17 severity levels × 12 repeats × 2 sampling measures. By default, it writes results under the repository root. To choose another output location, set the `LIDC_PROJECT_ROOT` environment variable **before** running. Depending on hardware, the full experiment may be computationally demanding.

The exact-match comparison tool requires a **separately supplied** original output archive and a newly generated output directory:

```bash
python tests/compare_full_outputs.py --original-zip /path/to/output.zip --new-dir /path/to/new/output
```

Do not assume `/path/to/output.zip` is bundled with this repository.

## Archived synthetic evidence

The `evidence/` directory contains the original archived files, regenerated CSVs and logs used in the earlier validations. Filenames are intentionally retained to preserve established provenance. These are synthetic descriptors, not patient-level LIDC records. Historical verification logs are evidence of their recorded runs, not a claim that all experiments have been freshly rerun for this release.

## Clinical analysis limitations

The files under `legacy_scripts/` are selected research scripts associated with analyses in the manuscript. Some still use absolute Windows paths, expect separately prepared LIDC-derived intermediate tables, or depend on preprocessing not distributed here. They should **not** be described as executable end-to-end clinical reproduction from a fresh download.

LIDC-IDRI source images and annotations must be obtained independently from The Cancer Imaging Archive (TCIA), subject to its terms. The MIT license does not cover third-party datasets, medical imaging data or third-party code. No patient-level clinical data are distributed as part of this package.

## Citation

Refer to `CITATION.cff` to cite this software repository. Cite the related journal article separately when publication details become available.
