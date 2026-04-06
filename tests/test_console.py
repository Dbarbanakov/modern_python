# tests/test_console.py
import click.testing

from modern_python import console
import pytest


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
