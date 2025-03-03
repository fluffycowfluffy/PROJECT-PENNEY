import subprocess

def import_libs():
  """
  Automate the installation of required libraries
  via the command line.

  Automated commands written for a
  macOS/Unix environment
  """
  subprocess.run(["pip", "install", "-r", "requirements.txt"])
  # ans = subprocess.run(["python", "--version"], text = True)
  print("All requirements installed")

if __name__ == "__main__":
  import_libs()
