import subprocess

source_dirs = "mingshe tests"
subprocess.check_call(f"flake8 {source_dirs}", shell=True)
