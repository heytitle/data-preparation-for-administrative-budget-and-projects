import json
import fire
import requests
import pandas as pd

from multiprocessing import Pool

MAX_RETRIES = 5
LIMIT = 20
URL =  "https://govspendingapi.data.go.th/api/service/cgdcontract"


with open(".token", "r") as f:
    TOKEN = f.readline().strip()

def get_all(params, retries=0):
    req = requests.get(URL, params)
    print("-> req ", params)
    if not req:
        if retries > MAX_RETRIES:
            print("Tried this request more than %d times" % MAX_RETRIES, params)
            return []
        retries += 1
        print("Retry %d" % retries)
        return get_all(params, retries=retries)
    data = req.json()['result']
    if len(data) == LIMIT:
        params['offset'] = params['offset'] + LIMIT
        return data + get_all(params)
    else:
        return data

def do_scrape(attr, year=2561):
    org_name = attr['search_name']
    province = attr['cleaned_province']
    if not province:
        print("Skipping %s" % org_name)
        return

    year = 2561
    data = get_all(dict(
        user_token=TOKEN,
        year=year,
        dept_name=org_name,
        limit=LIMIT,
        offset=0
    ))

    slug = "%s-%s-%s" % (org_name, province, year)
    print("Saving file to %s (%d records)" % (slug, len(data)))
    with open("%s/%s.json" % (attr['output_dir'], slug),  "w") as f:
        output = dict(
            org=org_name,
            province=province,
            projects=data
        )
        json.dump(data, f, ensure_ascii=False)


def main(input_file, output_dir, pool_size=5):
    # read token from file
    with open(".token", "r") as f:
        token = f.readline().strip()

    df = pd.read_csv(input_file)
    df["output_dir"] = output_dir

    records = df.to_dict("records")

    with Pool(pool_size) as p:
        p.map(do_scrape, records)

if __name__ == "__main__":
    fire.Fire(main)