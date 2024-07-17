import sqlite3

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
        self.insertPolicyId()
        self.saveVersion(1)
        print("Policy Added")

        conn.commit()
    
    def updatePolicy(self , newName , newDescription):

        self.id = self.getPolicyId(newName , newDescription)
        
        newVersion = self.getPolicyVersion() + 1

        cursor.execute("""
            UPDATE policies SET name = ? , description = ? , version = ? where id = ?
        """ , (newName , newDescription , newVersion , self.id))

        cursor.execute("""
            UPDATE versions SET name = ? , description = ? , version = ? where id = ?
        """ , (newName , newDescription , newVersion , self.id))

        conn.commit()    

    def saveVersion(self, version):
        conn.execute("""
            INSERT INTO versions VALUES(?,?,?,?)

        """ , (self.id , self.name , self.description , version))

        conn.commit()

    def insertPolicyId(self):
        conn.execute("""
            UPDATE policies SET id = ? WHERE name = ?
        """ , (self.id , self.name))

        conn.commit()

    def getPolicyId(self , newName , newDescription):
        cursor.execute("SELECT id FROM policies WHERE name = ? OR description = ?" , (newName , newDescription))
        return cursor.fetchone()[0]
        
    
    def getPolicyVersion(self):
        cursor.execute("SELECT version FROM versions WHERE id = ?" , (self.id,))
        return cursor.fetchone()[0]
        
        



















print("Main function")

conn = sqlite3.connect('organization.db')

cursor = conn.cursor()



