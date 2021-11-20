import subprocess

# Initilize as git repository
subprocess.run(["git", "init"])

# Setup poetry deps and venv
subprocess.run(["poetry", "install"])

