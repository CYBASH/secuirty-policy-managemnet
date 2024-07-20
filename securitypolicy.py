import sqlite3
from hash import *

class Policy:
    def __init__(self , name , description):
        self.conn = sqlite3.connect('organization.db')
        self.cursor = self.conn.cursor()

        self.name = name
        self.description = description
        self.id = None
    
    def insertPolicy(self):
        self.cursor.execute("""
            INSERT INTO policies(name , description , version) VALUES(?,?,?)
        """ , (self.name , self.description , 1))

        self.id = self.cursor.lastrowid
        print("Policy Added")

        self.conn.commit()
    
    def updatePolicy(self , newName , newDescription):

        self.id = self.getPolicyId(newName , newDescription)
        
        newVersion = self.getPolicyVersion() + 1

        self.cursor.execute("""
            UPDATE policies SET name = ? , description = ? , version = ? where rowid = ?
        """ , (newName , newDescription , newVersion , self.id))

        self.conn.commit()    

    def getPolicyId(self , newName , newDescription):
        self.cursor.execute("SELECT rowid FROM policies WHERE name = ?" , (newName ,))
        return self.cursor.fetchone()[0]
        
    
    def getPolicyVersion(self):
        self.cursor.execute("SELECT version FROM policies WHERE rowid = ?" , (self.id,))
        return self.cursor.fetchone()[0]
    
    def displayPolicies(self):
        print("POLICIES TABLE: ")
        self.cursor.execute("""
            SELECT rowid , * FROM policies
        """)
        for i in self.cursor.fetchall():
            print(i)
        
        


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('organization.db')
        self.cursor = self.conn.cursor()
    

    def insertCredentials(self , username , password , email):
        p = Password(password)
        p.encrypt()
        hashPassword = p.getHashCode()

        if self.isUsernameTaken(username):
            print("Username already taken")
            return

        self.cursor.execute("""
            INSERT INTO credentials(username , password , email) VALUES(?,?,?)
        """ , (username , hashPassword , email))

    
    def getUsername(self , email):
        self.cursor.execute("""
            SELECT username FROM credentials where email = ?
        """ , (email,))

        try:
            return self.cursor.fetchone()[0]
        
        except TypeError:
            print("Email not found")
    
    def getPassword(self , username):
        self.cursor.execute("""
            SELECT password FROM credentials where username = ?
        """ , (username,))

        try:
            return self.cursor.fetchone()[0]
        
        except TypeError:
            print("User not found")

    def getEmail(self , username):
        self.cursor.execute("""
            SELECT email FROM credentials where username = ?
        """ , (username,))

        try:
            return self.cursor.fetchone()[0]
        
        except TypeError:
            print("User not found")

    def isUsernameTaken(self , username):
        self.cursor.execute("""
            SELECT username FROM credentials where username = ?
        """ , (username,))

        try:
            return self.cursor.fetchone()[0]

        except TypeError:
            return False


if __name__ == "__main__":
    db = Database()
    db.insertCredentials("testuser" , "Test@123" , "test@gmail.com")
    