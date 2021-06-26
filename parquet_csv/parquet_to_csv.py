from time import perf_counter
import sys
import click
import pyarrow as pa
from pyarrow import csv
from pyarrow import parquet as pq


@click.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.option(
    "-o",
    "--output-path",
    default="-",
    show_default="standard output",
    type=click.Path(exists=False, dir_okay=False),
)
@click.option("--header/--no-header", default=True)
@click.option("--verbose", default=True)
def parquet_to_csv(input_file, output_path, header, verbose):
    read_start = perf_counter()
    table = pq.read_table(input_file)
    if verbose:
        click.echo(
            f"reading from {click.format_filename(input_file)} took {perf_counter() - read_start:.3f} seconds",
            file=sys.stderr,
        )
    write_start = perf_counter()
    csv.write_csv(
        table,
        sys.stdout.buffer if output_path == "-" else output_path,
        write_options=csv.WriteOptions(include_header=header),
    )
    if verbose:
        click.echo(
            f"writing to {click.format_filename(output_path)} took {perf_counter() - write_start:.3f} seconds",
            file=sys.stderr,
        )


if __name__ == "__main__":
    parquet_to_csv()
