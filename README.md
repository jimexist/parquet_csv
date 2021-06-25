# Parquet_CSV

[![CI](https://github.com/Jimexist/parquet_csv/actions/workflows/build.yml/badge.svg)](https://github.com/Jimexist/parquet_csv/actions/workflows/build.yml) | [PyPI](https://pypi.org/project/parquet-csv/)

A Parquet to and from CSV converter that is based on [Apache Arrow](https://arrow.apache.org/) for its speed and memory efficiency.

## How to install

```bash
pip install parquet_csv
```

Use `pip3` if both Python2 and Python3 are installed. This application only works with Python3.

## How to use

`parquet_to_csv` converts `parquet` files to `csv` files.

```text
Usage: parquet_to_csv.py [OPTIONS] INPUT_FILE OUTPUT_PATH

Options:
  --header / --no-header
  --verbose BOOLEAN
  --help                  Show this message and exit.
```
