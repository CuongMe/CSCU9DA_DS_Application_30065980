# CSCU9DA — Data Audit & Preliminary EDA

An independent data audit of the study data behind Weis and Dawid (2026), *Optimizing bike-sharing
station locations: A machine learning and artificial neural networks approach using geospatial and
demographic data*, PLOS ONE, [doi:10.1371/journal.pone.0349339](https://doi.org/10.1371/journal.pone.0349339).

## Contents

| Path | What it is |
|---|---|
| `Data Audit & EDA.ipynb` | The audit notebook, executed end to end |
| `figures/` | The five figures the notebook writes |
| `paper/` | The source paper (open access, CC BY 4.0) |

## Getting the data

The dataset is **not included here** — it is 684 MB and already published by the original authors.
Download it from the figshare record and unpack it so the layout matches:

```
https://doi.org/10.6084/m9.figshare.31566433

shared_data/
└── study_data/
    └── files/
        ├── training_area/
        ├── test_area/
        └── apply_area/
```

The notebook resolves everything from `shared_data/study_data/files`, so no paths need editing.

## Running it

```bash
python -m venv .venv
.venv/Scripts/pip install pandas geopandas pyogrio matplotlib seaborn scipy jupyterlab
.venv/Scripts/jupyter lab "Data Audit & EDA.ipynb"
```

Built against Python 3.12 with pandas 3.1, geopandas 1.2, matplotlib 3.11, seaborn 0.13 and scipy 1.18.
Nothing in the notebook is random, so re-running reproduces every figure and table exactly.

## Note

The dataset and the paper are the original authors' work, reused here under CC BY 4.0 for an
academic review exercise. The audit, notebook and figures are my own.
