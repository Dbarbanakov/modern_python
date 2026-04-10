# src/hypermodern_python/console.py
"""Command-line interface."""

import textwrap

import click

from . import __version__, get_data


@click.command()
@click.option(
    "--endpoint",
    "-p",
    default="todos",
    help="Reaches different end points of the API - todos or posts.",
    metavar="END",
    show_default=True,
)
@click.version_option(version=__version__)
def main(endpoint: str) -> None:
    """The hypermodern Python project."""
    data = get_data.api_data(endpoint=endpoint)

    click.echo(textwrap.fill(data.title))
    click.secho(data.id, fg="blue")
