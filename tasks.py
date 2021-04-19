from invoke import task


@task
def lint(c):
    """Invoke linting for the project."""
    c.run("black .")
