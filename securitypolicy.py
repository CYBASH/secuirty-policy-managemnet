import sqlite3
from random import randint
class Policy:
    def __init__(self , name , description):
        self.name = name
        self.description = description
        self.id = None
    
    def insertPolicy(self):
        cursor.execute("""
            INSERT INTO policies(name , description , version) VALUES(?,?,?)
        """ , (self.name , self.description , 1))

        self.id = cursor.lastrowid
        print("Policy Added")

        conn.commit()
    
    def updatePolicy(self , newName , newDescription):

        self.id = self.getPolicyId(newName , newDescription)
        
        newVersion = self.getPolicyVersion() + 1

        cursor.execute("""
            UPDATE policies SET name = ? , description = ? , version = ? where rowid = ?
        """ , (newName , newDescription , newVersion , self.id))

        conn.commit()    

    def getPolicyId(self , newName , newDescription):
        cursor.execute("SELECT rowid FROM policies WHERE name = ?" , (newName ,))
        return cursor.fetchone()[0]
        
    
    def getPolicyVersion(self):
        cursor.execute("SELECT version FROM policies WHERE rowid = ?" , (self.id,))
        return cursor.fetchone()[0]
    
    def displayPolicies(self):
        print("POLICIES TABLE: ")
        cursor.execute("""
            SELECT rowid , * FROM policies
        """)
        for i in cursor.fetchall():
            print(i)
        
        



















print("Main function")

conn = sqlite3.connect('organization.db')

cursor = conn.cursor()



