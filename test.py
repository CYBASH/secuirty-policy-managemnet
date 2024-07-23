import sqlite3
from securitypolicy import Policy
from hash import Password

#connect to the database.
conn = sqlite3.connect('organization.db')
print("","Database Connected")

#Creater a cursor
cursor = conn.cursor()


#Create a Policy table
'''
cursor.execute("""
    CREATE TABLE policies(id INT , name text , description text)
""")

print("","Table Created")
'''


#Creating Credentials table
'''
cursor.execute("""
    CREATE TABLE credentials(id INT , username text , password text , email text , verified text)
""")
print("Credentails table created")
'''

#Insert a single policy
'''
cursor.execute("","""
    INSERT INTO policies VALUES('Password Policy' , 'Enforce strong passwords with minimum length and complexity.')
""")

print("","Inserted 'Password Policy' into the table.")
'''

#Insert a user credentials
'''
cursor.execute("""
    INSERT INTO credentials VALUES(1 , 'CYBASH' , 'test@123' , 'test123@gmail.com' , 'yes')
""")
print("Created a account for 'CYBASH'")
'''

#Sample Policies
sample_policies = [
    ("1","Password Policy", "Enforce strong passwords with minimum length and complexity."),
    ("2","Data Encryption Policy", "Encrypt sensitive data both in transit and at rest."),
    ("3","Access Control Policy", "Define and enforce access permissions based on roles."),
    ("4","Backup Policy", "Regularly backup critical data and verify integrity."),
    ("5","Incident Response Policy", "Establish procedures for responding to security incidents."),
    ("6","Network Security Policy", "Implement firewalls and intrusion detection systems."),
    ("7","Software Patching Policy", "Regularly update and patch software to mitigate vulnerabilities."),
    ("8","Physical Security Policy", "Secure physical access to data centers and server rooms."),
    ("9","Remote Access Policy", "Regulate remote access to corporate networks and resources."),
    ("10","Social Engineering Policy", "Educate employees to recognize and report social engineering attacks.")
]


#Inserting List of policies
'''
cursor.executemany("""
    INSERT INTO policies VALUES(?,?,?)
""" , sample_policies)

print("Inserted List of policies")
'''

#Retrieving Policies
'''
cursor.execute("""
    SELECT * FROM policies
""")

print(cursor.fetchall())
'''

#Removing table from database
'''
cursor.execute("""
    DROP TABLE policies
""")
'''

#Update existing policy

#Static update command
'''
cursor.execute("""
    UPDATE policies set description = 'updated text' where ID = 1
""")
print("Row updated")
'''

#Dynamic update command

'''
newPolicyName = 'testName'
newPolicyDescription = 'testDiscription'
policyId = 1

cursor.execute("""
    UPDATE policies set description = ? where ID = ?
""" , (newPolicyDescription , policyId))

cursor.execute("""
    UPDATE policies set name = ? where ID = ?
""" , (newPolicyName , policyId))

print("Row updated")
'''

#test
'''
newName="a"
newDescription = "testDiscription"
cursor.execute("SELECT id,name,description FROM policies WHERE name = ? OR description = ?" , (newName , newDescription))
print(cursor.fetchmany()[0])
'''
'''
cursor.execute("""
    INSERT INTO policies VALUES(0, 'XYZ' , 'TEST1234')
""")

print("Inserted 'Password Policy' into the table.")
policyId = cursor.lastrowid
print(policyId)
'''

#Commit the command
"conn.commit()"

#Close the connection
"conn.close()"

'''
cursor.execute("""
    CREATE TABLE versions(id INT , name text, description text, version INT)
""")

print("Query Executed")

'''
if __name__ == "__main__":
    #policy = Policy("Data Encryption Policy" , "Encrypt sensitive data both in transit and at rest.")
    #policy.insertPolicy()

    #policy = Policy("Password Policy" , "Enforce strong passwords with minimum length and complexity.")
    #policy.updatePolicy("Data Encryption Policy" , "New  Password description 123456")
    
    #policy.displayPolicies()
    '''
    cursor.execute("""
        UPDATE versions SET name = "Password Policy" WHERE id = 1
    """)

    conn.commit()
    '''

    cursor.execute("DROP TABLE policies")
    cursor.execute("""
        CREATE TABLE policies(name text , description text , version INT)
    """)
    

    #Name and Description Validation Code
    '''
    cursor.execute("""
        SELECT true FROM policies where description = 'New  Password description 123456'
    """)

    print(cursor.fetchall())
    '''
    '''
    cursor.execute("""
        UPDATE credentials SET password = ? WHERE username = ?
    """ , ('8776f108e247ab1e2b323042c049c266407c81fbad41bde1e8dfc1bb66fd267e' , 'testuser'))
'''
    conn.commit()

    




#p = Password("Test@123")
#print(p.encrypt())


#p.login("Test@123")