from tkinter import *
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *
from email_verfication_ui import Email_verification_Interface
from emailverification import EmailVerification



class Signup_Interface:
    def __init__(self, root):
        self.root = root

    def signupInterfaceClosed(self):
        self.signupUI.destroy()
        self.showWindow(self.root)
    
    def startUI(self):
        #self.root.mainloop()
        signupUI = Toplevel(self.root)
        signupUI.protocol("WM_DELETE_WINDOW", self.signupInterfaceClosed)
        self.signupUI = signupUI
        self.hideWindow(self.root)
        
        self.signupUI.title("Security Policy Management Project")
        self.signupUI.configure(bg="#505050")
        self.signupUI.geometry('600x600')
        self.signupUI.resizable(False, False)
        self.signupUI.iconbitmap("images/icon.ico")
        self.background_image = ImageTk.PhotoImage(Image.open("images/background.jpeg"))
        self.canvas = Canvas(self.signupUI, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        self.background_color = self.background_image._PhotoImage__photo.get(0, 0)

        self.heading()
        self.username()
        self.email()
        self.password()
        self.confirm_password()
        self.signup_button()

    def heading(self):
        #Project Heading
        self.heading_label = self.canvas.create_text(300, 110, 
                                                     text="Create a new account!", 
                                                     font=("Verdana", 24, "bold"),
                                                     fill="white", 
                                                     justify="center")

    def username(self):
        #username
        self.username_label = self.canvas.create_text(128, 200,
                                                  text="Username ", 
                                                  font=("Verdana", 12, "bold"),
                                                  fill="#12ECC0")
        self.username_entry = Entry(self.signupUI, width=25, font=("Verdana", 12))
        self.canvas.create_window(390, 200, anchor='center', window=self.username_entry) 

    def email(self):
        #email
        self.email_label = self.canvas.create_text(107, 260,
                                 text="Email ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="#12ECC0")
        self.email_entry = Entry(self.signupUI, width=25, font=("Verdana", 12))
        self.canvas.create_window(390, 260, anchor='center', window=self.email_entry)

    def password(self):
        #password
        self.password_label = self.canvas.create_text(128, 320,
                                 text="Password ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="#12ECC0") 
        self.password_entry = Entry(self.signupUI, width=25, font=("Verdana", 12), show="*")
        self.canvas.create_window(390, 320, anchor='center', window=self.password_entry)

    def confirm_password(self):
        #password
        self.confirm_password_label = self.canvas.create_text(165, 380,
                                 text="Confirm Password ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="#12ECC0") 
        self.confirm_password_entry = Entry(self.signupUI, width=25, font=("Verdana", 12), show="*")
        self.canvas.create_window(390, 380, anchor='center', window=self.confirm_password_entry)
    
    def signup_button(self):
        #signup btn
        border_frame = Frame(self.signupUI,
                         bg="#12ECC0", 
                         bd=2) 
        border_frame.place(relx=0.5, rely=0.8, anchor='center')

        self.signup_btn = Button(border_frame,
                    text="Sign Up",
                    bg="black",
                    fg="#12ECC0",
                    font=("Verdana", 11, "bold"),
                    width=10,
                    command=self.compare_password) #Command to be defined
        self.signup_btn.pack()

    def compare_password(self):
        if(self.password_entry.get() == self.confirm_password_entry.get()):
            self.sendOTP()
            self.openVerifyWindow()
        
        else:
            print('not same')
    
    def hideWindow(self,window):
        window.withdraw()

    def showWindow(self,window):
        window.deiconify()
    
    def verifyInterfaceClosed(self):
        self.root.destroy()
    
    def openVerifyWindow(self):
        self.emailVerifyUI = Email_verification_Interface(self.signupUI , self.emailVerify)
        email = self.email_entry.get()
        self.emailVerifyUI.startUI(email)
        print("Verify window opened")
        
        
        
        
        
    def sendOTP(self):
        message = '''
            Thank you for Signing up for Security Policy Management Tool.
            
        '''
        
        self.emailVerify = EmailVerification(self.email_entry.get())
        self.emailVerify.generateOTP()
        self.emailVerify.sendOTP(message)
        

if __name__ == "__main__":
    root = Tk()
    signup = Signup_Interface(root)
