import hashlib as h

class Password:
    def __init__(self, user_Password):
        self.user_Password = user_Password
        self.hashcode = None

    #checking the password is valid or not

    def validation(self):
        if len(self.user_Password) < 8:
            return False
        elif not self.has_capital_letter():
            return False
        elif not self.has_lower_letter():
            return False
        elif not self.has_special_char():
            return False
        else:
            self.encrypt(self.user_Password)
            return True

    #checking the password cotaining atleast a uppercase letter
    def has_capital_letter(self):
        return any(char.isupper() for char in self.user_Password)

    #checking the password cotaining atleast a lowercase letter        
    def has_lower_letter(self):
        return any(char.islower() for char in self.user_Password)

    #checking the password cotaining atleast a special character
    def has_special_char(self):
        special_char="!@#$%^&*()_-+={}[]?/.,';:|~`"
        return any(char in special_char for char in self.user_Password)

    #encrypting the password to hash codes
    def encrypt(self, password):
        hashing=h.new('SHA256')
        hashing.update(password.encode())
        self.hashcode = hashing.hexdigest()
        print("Encrypting password:",self.hashcode)
        
    
    def login(self , password):
        hashing=h.new('SHA256')
        hashing.update(password.encode())
        if(self.hashcode == hashing.hexdigest()):
            print("Login Success")
        else:
            print("Wrong Password")

