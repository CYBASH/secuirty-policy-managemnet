from User_Interface import startMainUI
from securitypolicy import *
import sqlite3
import tempfile
import os
import atexit


def createTempFile():
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
    filename = temp_file.name
    return filename

def deleteTempFile():
    temp_file_name = filename
    if os.path.exists(temp_file_name):
        os.remove(temp_file_name)


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
