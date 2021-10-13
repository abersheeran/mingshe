import subprocess

source_dirs = "mingshe tests"
subprocess.check_call(f"pdm run flake8 {source_dirs}", shell=True)
