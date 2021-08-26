import subprocess

source_dirs = "mingshe tests"
subprocess.check_call(f"isort --check --diff {source_dirs}", shell=True)
subprocess.check_call(f"flake8 {source_dirs}", shell=True)
