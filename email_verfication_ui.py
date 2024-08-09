from tkinter import *
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *
from signup_interface import *


class Email_verification_Interface:
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

        self.heading()
        self.statement()
        self.otp()
        self.verify_button()
        self.startUI()

    
    def startUI(self):
        self.root.mainloop()

    def heading(self):
        #heading
        self.heading_label = self.canvas.create_text(300, 150,
                                 text="Confirm your Email ", 
                                 font=("Verdana", 25, "bold"),
                                 fill="white")

    def statement(self):
        #statement
        self.statement_label = self.canvas.create_text(300, 210,
                                 text="Type in the OTP we sent to example@gmail.com. ", 
                                 font=("Verdana", 12, "bold"),
                                 fill="grey", justify="center")

    def otp(self):
        #otp
        self.otp_label = self.canvas.create_text(168, 270,
                                 text="Enter OTP ", 
                                 font=("Verdana", 15, "bold"),
                                 fill="white") 
        self.otp_entry = Entry(self.root, width=20, font=("Verdana", 15), justify="center")
        self.canvas.create_window(390, 270, anchor='center', window=self.otp_entry)
    
    def verify_button(self):
        #verify btn
        self.verify_btn = Button(self.root,
                    text="Verify Email",
                    bg="#12ECC0",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=10,
                    width=10,
                    command=self.verify_email) #Command to be defined
        self.verify_btn.place(relx=0.5, rely=0.6, anchor='center')  

    def verify_email(self):
        pass


if __name__ == "__main__":
    root = Tk()
    verify = Email_verification_Interface(root)
