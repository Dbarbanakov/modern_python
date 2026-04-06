# noxfile.py
import nox


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
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
