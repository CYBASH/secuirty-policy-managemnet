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
        self.username_label = self.canvas.create_text(175, 90,
                                                  text="Username ", 
                                                  font=("Verdana", 12, "bold"),
                                                  fill="white")
        self.username_entry = Entry(self.root, width=30, font=("Verdana", 10))
        self.canvas.create_window(370, 90, anchor='center', window=self.username_entry) 

    def email(self):
        #email
        self.email_label = self.canvas.create_text(155, 140,
                                 text="Email ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="white")
        self.email_entry = Entry(self.root, width=30, font=("Verdana", 10))
        self.canvas.create_window(370, 140, anchor='center', window=self.email_entry)

    def password(self):
        #password
        self.password_label = Label(self.root, 
                                    text="Password:", 
                                    padx=44, 
                                    font=("Verdana", 11, "bold"))
        self.password_label.place(relx=0.27, rely=0.35, anchor='center')   
        self.password_entry = Entry(self.root, show="*", width=35)
        self.password_entry.place(relx=0.9, rely=0.35, anchor='e')  

    def confirm_password(self):
        #password
        self.confirm_password_label = Label(self.root, 
                                            text="Confirm Password:", 
                                            padx=10, 
                                            font=("Verdana", 11, "bold"))
        self.confirm_password_label.place(relx=0.27, rely=0.45, anchor='center')   
        self.confirm_password_entry = Entry(self.root, show="*", width=35)
        self.confirm_password_entry.place(relx=0.9, rely=0.45, anchor='e')  
    
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
        
        else:
            print('not same')

if __name__ == "__main__":
    root = Tk()
    signup = Signup_Interface(root)
