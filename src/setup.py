import subprocess

def import_libs():
  """
  Automate the installation of required libraries
  via the command line.

  Automated commands written for a
  macOS/Unix environment
  """
  subprocess.run("pip install -r requirements.txt")
  return None
