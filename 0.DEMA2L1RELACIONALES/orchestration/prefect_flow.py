from prefect import flow, task
import subprocess
import os

BASE = os.path.dirname(os.path.dirname(__file__))
RAW_DIR = os.path.join(BASE, 'data', 'raw')
STAGING_DIR = os.path.join(BASE, 'data', 'staging')

@task
def extract():
    print('Running extract.py')
    subprocess.check_call(['python', os.path.join(BASE, 'scripts', 'extract.py')])

@task
def transform():
    print('Running transform.py')
    subprocess.check_call(['python', os.path.join(BASE, 'scripts', 'transform.py')])

@task
def load():
    print('Running load.py')
    subprocess.check_call(['python', os.path.join(BASE, 'scripts', 'load.py')])

@flow
def etl_flow():
    extract()
    transform()
    load()

if __name__ == '__main__':
    etl_flow()
