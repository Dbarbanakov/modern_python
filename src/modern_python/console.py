# src/hypermodern_python/console.py
import textwrap

import click

from . import __version__, get_data


@click.command()
@click.version_option(version=__version__)
def main():
    """The modern Python project."""
    data = get_data.api_data()

    for post in data[:4]:

        title = post["title"]
        status = post["completed"]

        # click.secho(title, fg="green")
        click.echo(textwrap.fill(title))
        click.secho(status, fg='blue')
