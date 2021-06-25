from time import perf_counter

import click
import pyarrow as pa
from pyarrow import csv
from pyarrow import parquet as pq


@click.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.argument("output_path", type=click.Path(exists=False, dir_okay=False))
@click.option("--verbose", default=True)
def main(input_file, output_path, verbose):
    read_start = perf_counter()
    table = pq.read_table(input_file)
    if verbose:
        click.echo(
            f"reading from {click.format_filename(input_file)} took {perf_counter() - read_start:.3f} seconds"
        )
    write_start = perf_counter()
    csv.write_csv(table, output_path)
    if verbose:
        click.echo(
            f"writing to {click.format_filename(output_path)} took {perf_counter() - read_start:.3f} seconds"
        )


if __name__ == "__main__":
    main()
