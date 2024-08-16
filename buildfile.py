#Build Src: https://coderslegacy.com/python-cx_freeze-tutorial/
#Command: python buildfile.py build

"Automated Step 2"
    #step 2: Add manifest file to the exe file. 
    #   command: mt.exe -manifest "D:\Cyber Security Intern\Project\secuirty-policy-managemnet\application files\runasadmin.manifest" -outputresource:"D:\Cyber Security Intern\Project\secuirty-policy-managemnet\build\exe.win-amd64-3.12\secuirty-policy-managemnet.exe";1

#step 3: https://www.youtube.com/watch?v=O3RXTFAiZJs&t=406s



from cx_Freeze import setup, Executable
import os
import shutil
import subprocess


# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'gui'

executables = [
    Executable('main.py', base=base, target_name = 'secuirty-policy-managemnet', icon="images/icon.ico")
]

setup(name='SECURITY PROJECT MANAGEMENT',
      version = '1',
      description = 'SECURITY PROJECT MANAGEMENT',
      options = {'build_exe': build_options},
      executables = executables)


# Define additional files and directories to copy
additional_files = ["organization.db", "images/"]

# Define the output directory
output_dir = os.path.join("build", "exe.win-amd64-3.11")  # Adjust according to your Python version and platform

# Copy additional files and directories
for item in additional_files:
    source = os.path.join(os.getcwd(), item)
    destination = os.path.join(output_dir, item)

    if os.path.isdir(source):
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        shutil.copy2(source, destination)


# Define the PowerShell command
command = (
    'mt.exe -manifest "D:/secuirty-policy-managemnet/application files/runasadmin.manifest" '
    '-outputresource:"D:/secuirty-policy-managemnet/build/exe.win-amd64-3.11/secuirty-policy-managemnet.exe;1"'
)

# Run the command using subprocess
result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
print(result)
