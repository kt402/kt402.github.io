# KT

## Dev

```bash
yarn install --frozen-lockfile        # install
yarn serve                            # test locally
yarn build                            # build for production
yarn lint                             # lint and fix files
```

## Extraction

* Python 3.10 required
* Directory: ./extraction

1. Take excel file and manually export sheet as csv file
2. Run Python program with constants set to create the recommendations

```bash
cd extraction
pipenv install
pipenv run python extract.py
```