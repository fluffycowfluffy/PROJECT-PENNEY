import subprocess as sp

def import_libs():
  """
  Automate the installation of required libraries
  via the command line.

  Automated commands written for a
  macOS/Unix environment
  """
  try:
    sp.run(["pip", "install", "-r", "requirements.txt"],
                   check =  True, # flag possible errors with installation
                   stdout = sp.PIPE, # stdout captures output to this file
                   stderr = sp.PIPE) # stderr captures diagnostic information to this file
    print("All requirements installed!")
  except sp.CalledProcessError as e:
    print(f"Unable to install all requirements from requirements.txt due to error: {e}")
  except Exception as e:
    print(f"Unable to install all requirements from requirements.txt due to unexpected error: {e}")
