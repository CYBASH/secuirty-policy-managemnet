from tkinter import *
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *
import re


class Signup_Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Policy Management Project")
        self.root.configure(bg="#505050")
        self.root.geometry('600x600')
        self.root.resizable(False, False)
        self.root.iconbitmap("images/icon.ico")
        self.background_image = ImageTk.PhotoImage(Image.open("images/background.jpeg"))
        self.canvas = Canvas(self.root, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        self.background_color = self.background_image._PhotoImage__photo.get(0, 0)

        self.username()
        self.email()
        self.password()
        self.confirm_password()
        self.signup_button()
        self.startUI()

    def startUI(self):
        self.root.mainloop()

    def username(self):
        #username
        self.username_label = self.canvas.create_text(128, 90,
                                                  text="Username ", 
                                                  font=("Verdana", 12, "bold"),
                                                  fill="white")
        self.username_entry = Entry(self.root, width=30, font=("Verdana", 10))
        self.canvas.create_window(390, 90, anchor='center', window=self.username_entry) 

    def email(self):
        #email
        self.email_label = self.canvas.create_text(107, 140,
                                 text="Email ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="white")
        self.email_entry = Entry(self.root, width=30, font=("Verdana", 10))
        self.canvas.create_window(390, 140, anchor='center', window=self.email_entry)

    def password(self):
        #password
        self.password_label = self.canvas.create_text(128, 190,
                                 text="Password ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="white") 
        self.password_entry = Entry(self.root, width=30, font=("Verdana", 10))
        self.canvas.create_window(390, 190, anchor='center', window=self.password_entry)

    def confirm_password(self):
        #password
        self.confirm_password_label = self.canvas.create_text(165, 240,
                                 text="Confirm Password ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="white") 
        self.confirm_password_entry = Entry(self.root, width=30, font=("Verdana", 10))
        self.canvas.create_window(390, 240, anchor='center', window=self.confirm_password_entry)
    
    def signup_button(self):
        #signup btn
        self.signup_btn = Button(self.root,
                    text="Sign Up",
                    bg="blue",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=10,
                    width=10,
                    command=self.compare_password) #Command to be defined
        self.signup_btn.place(relx=0.5, rely=0.6, anchor='center')  

    def compare_password(self):
        if(self.password_entry.get() == self.confirm_password_entry.get()):
            print('same')
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
        self.hideWindow(self.root)
        verifyInterface = Toplevel(self.root)
        
        verifyInterface.protocol("WM_DELETE_WINDOW", self.verifyInterfaceClosed)
        self.verifyInterface = verifyInterface
        
        self.verifyInterface.title("Security Policy Management Project")
        self.verifyInterface.configure(bg="#505050")
        self.verifyInterface.geometry('600x600')
        self.verifyInterface.resizable(False, False)
        self.verifyInterface.iconbitmap("images/icon.ico")

        self.background_image = ImageTk.PhotoImage(Image.open("images/background.jpeg"))
        self.canvas = Canvas(self.verifyInterface, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        self.background_color = self.background_image._PhotoImage__photo.get(0, 0)

if __name__ == "__main__":
    root = Tk()
    signup = Signup_Interface(root)
