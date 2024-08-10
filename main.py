from User_Interface import startMainUI
from securitypolicy import *
import sqlite3
import tempfile
import os
import atexit
import shutil


def createTempFile():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
    filename = temp_file.name

    temp_dir = tempfile.gettempdir()

    destination_file = os.path.join(temp_dir, os.path.basename("images/pro4.jpeg"))

    shutil.copy("images/pro4.jpeg", destination_file)


    return filename

def deleteTempFile():
    temp_file_name = filename
    if os.path.exists(temp_file_name):
        os.remove(temp_file_name)
    temp_dir = tempfile.gettempdir()
    files = os.listdir(temp_dir)

    # Iterate through the files and delete HTML files
    for file in files:
        if file.endswith('.html') or file.endswith('.jpeg'):
            os.remove(os.path.join(temp_dir, file))


if __name__ == "__main__":
    policyList = []

    conn = sqlite3.connect('organization.db')
    cursor = conn.cursor()

    cursor.execute("SELECT rowid,* FROM policies") 
    policyList = cursor.fetchall()

    filename = createTempFile()

    with open(filename, 'w') as f:
        for policy in policyList:
            text = str(policy[0]) + ". " + str(policy[1]) + ": " + str(policy[2]) + " (v" + str(policy[3]) + ")" + "\n"
            f.write(text)

    atexit.register(deleteTempFile)
    startMainUI(filename)
 