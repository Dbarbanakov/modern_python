# src/hypermodern_python/console.py
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
def main(endpoint):
    """The modern Python project."""
    data = get_data.api_data(end_point=endpoint)

    for post in data[:4]:

        title = post["title"]
        status = post.get("completed") if "completed" in post else post.get("body")

        click.echo(textwrap.fill(title))
        click.secho(status, fg="blue")
