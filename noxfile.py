# noxfile.py
import nox


@nox.session(python="3.12", reuse_venv=True)
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", '--cov')
