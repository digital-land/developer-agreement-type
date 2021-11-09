#!/usr/bin/env python3
import csv
from pathlib import Path

site="https://www.digital-land.info/"
dataset = Path().cwd().name
print("dataset:", dataset)


def redirect(path, to):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        f.write('<meta http-equiv="refresh" content="0; url=%s%s">' % (site, to))


redirect("./docs/index.html", "dataset/%s" % dataset)

with open("docs/.nojekyll", 'w') as f: f.write('')

for row in csv.DictReader(open("../entity-builder/dataset/entity.csv")):
    if row["dataset"] != dataset:
        continue

    path = Path("./docs/%s/index.html" % (row["reference"]))
    redirect(path, "entity/" + row["entity"])
