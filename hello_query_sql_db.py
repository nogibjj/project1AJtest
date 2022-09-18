#!/usr/bin/env python

import click
from dblib.querydb import find_year, find_director

# build a click group
@click.group()
def cli():
    pass


# build a click command
@click.command()
@click.option("--n", default=2020, help="Find release year")
def query_release_year(n):
    """Find release year"""
    find_release_year(n)


@click.command()
def query_duration(n):
    """Find duration of movie """
    find_duration()


# run the command
if __name__ == "__main__":
    cli.add_command(query_release_year)
    cli.add_command(query_duration)
    cli()
