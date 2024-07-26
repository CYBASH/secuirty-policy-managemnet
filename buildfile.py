#Build Src: https://coderslegacy.com/python-cx_freeze-tutorial/
#Command: python buildfile.py build


from cx_Freeze import setup, Executable
import os
import shutil

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'gui'

executables = [
    Executable('main.py', base=base, icon="images/pro4.jpeg")
]

setup(name='SECURITY PROJECT MANAGEMENT',
      version = '1',
      description = 'SECURITY PROJECT MANAGEMENT',
      options = {'build_exe': build_options},
      executables = executables)


# Define additional files and directories to copy
additional_files = ["organization.db", "images/"]

# Define the output directory
output_dir = os.path.join("build", "exe.win-amd64-3.12")  # Adjust according to your Python version and platform

# Copy additional files and directories
for item in additional_files:
    source = os.path.join(os.getcwd(), item)
    destination = os.path.join(output_dir, item)

    if os.path.isdir(source):
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        shutil.copy2(source, destination)

