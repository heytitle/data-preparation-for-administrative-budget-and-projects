import fire
import requests

from multiprocessing import Pool

URL_TEMPLATE = "http://info.dla.go.th/public/surveyInfo.do?cmd=surveyForm&orgInfoId={key}"

YEARS = [2015, 2016, 2017, 2018, 2019]
YINDX = dict(zip(YEARS, range(3, 3 + len(YEARS))))
ORG_IDS_FILE = "./data/local-governor-ids.txt"


BASE_DIR = "./outputs/budgets"

def _build_key(year, org_id):
    return "%s%s" % (year, "%04d" % int(org_id))


def scrape_years(years, trial=None, dry_run=False, pool_size=10):
    for y in years:
        print("Working on Y=%s" % y)
        scrape_year(y, trial=trial, dry_run=dry_run, pool_size=pool_size)

def scrape_year(year, trial=None, dry_run=False, pool_size=5):
    with open(ORG_IDS_FILE, "r") as f:
        org_ids = f.readlines()[:trial]

    year_org_ids = map(lambda x: (year, x.strip()), org_ids)

    with Pool(pool_size) as p:
        p.map(do_job, year_org_ids)

    return p.join()

def do_job(args):
    year, org_id = args
    text = scrape_year_org(year, org_id)

    with open("%s/%s/%s.html" % (BASE_DIR, year, org_id), "w") as f:
        f.write(text)


def scrape_year_org(year, org_id):
    yidx = YINDX[year]
    url = URL_TEMPLATE.format(key=_build_key(yidx, org_id))

    print("Scraping %s" % url)

    r = requests.get(url)

    return r.text

if __name__ == "__main__":
    fire.Fire({
        "years": scrape_years,
        "year": scrape_year,
        "year-org": scrape_year_org
    })