import fire
import requests


URL_TEMPLATE = "http://info.dla.go.th/public/surveyInfo.do?cmd=surveyForm&orgInfoId={key}"

YEARS = [2015, 2016, 2017, 2018, 2019]
YINDX = dict(zip(YEARS, range(3, 3 + len(YEARS))))
ORG_IDS_FILE = "./data/local-governor-ids.txt"

def _build_key(year, org_id):
    return "%s%s" % (year, "%04d" % int(org_id))

def scrape_year(year, trial=None, dry_run=False):
    with open(ORG_IDS_FILE, "r") as f:
        for org_id in f:
            text = scrape_year_org(year, org_id)

            if not dry_run:
                # save to gstorage
                pass

            if trial == 0:
                break
            else:
                trial -= 1


def scrape_year_org(year, org_id):
    yidx = YINDX[year]
    url = URL_TEMPLATE.format(key=_build_key(yidx, org_id))

    print("Scraping %s" % url)

    r = requests.get(url)

    return r.text

if __name__ == "__main__":
    fire.Fire({
        "year": scrape_year,
        "year-org": scrape_year_org
    })