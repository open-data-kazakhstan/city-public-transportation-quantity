# PUBLIC TRANSPORTATION 

## Data 

Data is in xlsx format and synced with upstream source yearly. It is sourced from https://stat.gov.kz/ru/industries/business-statistics/stat-transport/spreadsheets/

**Note:** Since stat.gov.kz requested for a signed key for authorization, we just downloaded and put in directory *archive*. It is temporary solution

We have processed the source data to make it normalized and derived from it several aggregated datasets:

* `data/public-transport-quantity-final.csv` - data by segments.

We have also added some metadata such as column descriptions and [data packaged it][dp].

[dp]: https://frictionlessdata.io/data-package/

## Preparation

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repository uses openpyxl to convert  excel files into CSV format, so you will need to install that library if you haven't already

You first need to install the dependencies:

```
pip install -r scripts/requirements.txt
```

Then run the script.

```
python scripts/process.py
```

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/