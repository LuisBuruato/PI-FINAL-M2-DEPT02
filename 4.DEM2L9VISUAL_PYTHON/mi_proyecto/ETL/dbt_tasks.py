from prefect import task
import subprocess

@task
def run_dbt(models=None):
    cmd = ["dbt", "run"]
    if models:
        cmd += ["--models", models]

    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise Exception("DBT run failed")
    return result.stdout

