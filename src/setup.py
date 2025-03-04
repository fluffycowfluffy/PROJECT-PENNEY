import subprocess

def import_libs():
  """
  Automate the installation of required libraries
  via the command line.

  Automated commands written for a
  macOS/Unix environment
  """
  try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"],
                   check =  True, # flag possible errors with installation
                   stdout = subprocess.PIPE, # stdout captures output to this file
                   stderr = subprocess.PIPE) # stderr captures diagnostic information to this file
    print("All requirements installed!")
  except CalledProcessError as e:
    print(f"Unable to install all requirements from requirements.txt due to error {e}")
  except Exception as e:
    print(f"Unable to install all requirements from requirements.txt due to unexpected error {e}")
