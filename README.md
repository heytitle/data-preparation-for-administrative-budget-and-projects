# Data Acquisition & Preparation for codeforthailand's [Local Administrative Budget and Project][url]


## Data Acquisition
We retrieve from govspending.data.go.th using `./scripts/scrape-projects` with the seed file from `./output/org-list.csv`.

## Data Cleansing and Preparation
1. We consolidate what we get from the first step into a big file using `./notebooks/1-consolidation.ipynb`.
2. After that, we compute statistics needed for [the website][url] using `./notebooks/2-compute-statistics.ipynb`.

Please take a look inside the files for details.

[url]: https://codeforthailand.github.io/2019-local-administrative-budget-and-projects