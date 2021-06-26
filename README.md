# Parquet_CSV

[![CI](https://github.com/Jimexist/parquet_csv/actions/workflows/build.yml/badge.svg)](https://github.com/Jimexist/parquet_csv/actions/workflows/build.yml) | [PyPI](https://pypi.org/project/parquet-csv/)

A Parquet to and from CSV converter that is based on [Apache Arrow](https://arrow.apache.org/) for its speed and memory efficiency.

## How to install

```bash
pip install parquet_csv
```

Use `pip3` if both Python2 and Python3 are installed. This application only works with Python3.

## How to use

### Converting Parquet

`parquet_to_csv` converts `parquet` files to `csv` files. By default it prints to the standard
output, but can be directed via pipe or `-o` flag to write to a file.

```text
Usage: parquet_to_csv.py [OPTIONS] INPUT_FILE

Options:
  -o, --output-path FILE  [default: (standard output)]
  --header / --no-header
  --verbose BOOLEAN
  --help                  Show this message and exit.
```

### Selecting columns, `gzip`-ing output

Following UNIX principle, you should be using [xsv](https://github.com/BurntSushi/xsv) for selecting
columns from the csv or do other transformations: just pipe the output to `xsv` and you're all set.

Similarly if you'd want the file to be compressed, pipe the result to `gzip` and direct to a local
file ending in `.csv.gz`.
