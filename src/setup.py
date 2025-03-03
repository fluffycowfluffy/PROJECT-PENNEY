import subprocess

def import_libs():
  """
  Automate the installation of required libraries
  via the command line.

  Automated commands written for a
  macOS/Unix environment
  """
  try:
    if subprocess.run(["pip", "install", "-r", "requirements.txt"]):
      print("All requirements installed!")
  except Exception as e:
    print("Unable to install requirements from requirements.txt")
