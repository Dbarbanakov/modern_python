# noxfile.py
"""Nox sessions."""

import tempfile
from typing import Any

import nox
from nox import Session

locations = "src", "tests", "./noxfile.py"

nox.options.sessions = "lint", "mypy", "pytype", "typeguard", "tests"


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """Install packages constrained by Poetry's lock file."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "-f",
            "requirements.txt",
            "--without-hashes",
            "-o",
            requirements.name,
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python="3.12", reuse_venv=True)
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python="3.12")
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python="3.12", reuse_venv=True)
def tests(session: Session) -> None:
    """Run the test suite.

    Args:
        session: A nox Session.

    In case of running - 'poetry run nox -- args'

        Use 'poetry run nox -- -s tests -- filename.py'
        Example: poetry run nox -- -s tests -- tests/test_console.py

        because of the following reasons -
            poetry run nox → runs Nox inside Poetry env
            --             → tells Nox “everything after this goes to sessions”
            -s tests       → your Nox session name (example)
            second --      → tells Nox to forward remaining args to pytest
            filename.py    → passed to pytest
    """
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--without", "dev", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)


@nox.session(python="3.12")
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "-f",
            "requirements.txt",
            "--without-hashes",
            "-o",
            requirements.name,
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "scan", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.12")
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)


@nox.session(python="3.12")
def pytype(session: Session) -> None:
    """Type-check using pytype."""
    args = session.posargs or locations
    install_with_constraints(session, "pytype")
    session.run("pytype", *args)


@nox.session(python="3.12")
def typeguard(session: Session) -> None:
    """Runtime type checking using Typeguard."""
    args = session.posargs or ["-m", "not e2e"]
    session.run("poetry", "install", external=True)
    install_with_constraints(session, "pytest", "pytest-mock", "typeguard")
    session.run("pytest", "--typeguard-packages=hypermodern_python", *args)


@nox.session(python="3.12")
def xdoctest(session: Session) -> None:
    """Run examples with xdoctest."""
    session.run("poetry", "install", external=True)
    install_with_constraints(session, "xdoctest")
    session.run("python", "-m", "xdoctest", "hypermodern_python")
