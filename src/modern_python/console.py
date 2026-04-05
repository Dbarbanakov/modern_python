# src/hypermodern_python/console.py
import textwrap

import click
import requests

from . import __version__


API_URL = 'https://jsonplaceholder.typicode.com/posts'


@click.command()
@click.version_option(version=__version__)
def main():
    """The modern Python project."""
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    for post in data[:3]:

        title = post["title"]
        extract = post["userId"]

        click.secho(title, fg="green")
        click.secho(extract, fg='blue')
