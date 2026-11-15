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

The dataset is **not included here** — it unpacks to 684 MB, and two of its tables exceed GitHub's
file-size limit. You do not need to fetch it by hand: the notebook's **Data** cell downloads
`shared_data.zip` (153 MB) from the authors' figshare record,
[doi:10.6084/m9.figshare.31566433](https://doi.org/10.6084/m9.figshare.31566433) (CC BY 4.0),
unpacks it, and skips if the data is already on disk. The expected layout is:

```
shared_data/
└── study_data/
    └── files/
        ├── training_area/
        ├── test_area/
        └── apply_area/
```

Everything resolves from `shared_data/study_data/files`, so no paths need editing.

## Running it

```bash
python -m venv .venv
.venv/Scripts/pip install jupyterlab
.venv/Scripts/jupyter lab "Data Audit & EDA.ipynb"
```

Then run it top to bottom. The first two cells set themselves up: **Packages** installs anything
missing and prints the versions in use, and **Data** fetches the dataset as described above.

Built and executed on Python 3.14.7 with pandas 3.1.1, geopandas 1.2.0, pyogrio 0.13.0,
matplotlib 3.11.2, seaborn 0.13.2 and scipy 1.18.1. Nothing in the notebook is random, so a
re-run reproduces every figure and table exactly.

## Note

The dataset and the paper are the original authors' work, reused here under CC BY 4.0 for an
academic review exercise. The audit, notebook and figures are my own.
