# noxfile.py
import tempfile

import nox

locations = "src", "tests", "noxfile.py"

nox.options.sessions = "lint", "safety", "tests"


def install_with_constraints(session, *args, **kwargs):

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
def black(session):
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python="3.12")
def lint(session):
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python="3.12", reuse_venv=True)
def tests(session):
    """
    In case of running:
        'poetry run nox -- args'
        Use 'poetry run nox -- -s tests -- filename.py'
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
def safety(session):
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
