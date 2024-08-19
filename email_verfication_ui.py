from tkinter import *
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *
import os
import sys
from securitypolicy import Database
from emailverification import EmailVerification


class Email_verification_Interface:
    UIclosed = False
    
    def __init__(self, root , emailVerify , username , password):
        self.root = root
        self.emailVerify = emailVerify
        self.username = username
        self.password = password

    def emailVerifyInterfaceClosed(self):
        self.emailVerifyUI.destroy()
        self.showWindow(self.root)
    
    def hideWindow(self,window):
        window.withdraw()

    def showWindow(self,window):
        window.deiconify()
    
    def verifyInterfaceClosed(self):
        self.root.destroy()
    
    def startUI(self,email):
        
        self.email = email
        
        emailVerifyUI = Toplevel(self.root)
        emailVerifyUI.protocol("WM_DELETE_WINDOW", self.emailVerifyInterfaceClosed)
        self.emailVerifyUI = emailVerifyUI
        self.hideWindow(self.root)
        
        self.emailVerifyUI.title("Security Policy Management Project")
        self.emailVerifyUI.configure(bg="#505050")
        self.emailVerifyUI.geometry('600x600')
        self.emailVerifyUI.resizable(False, False)
        self.emailVerifyUI.iconbitmap("images/icon.ico")
        self.background_image = ImageTk.PhotoImage(Image.open("images/background.jpeg"))
        self.canvas = Canvas(self.emailVerifyUI, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        self.background_color = self.background_image._PhotoImage__photo.get(0, 0)

        self.backbtn()
        self.heading()
        self.statement()
        self.otp()
        self.verify_button()
        self.resend_btn()

    def backbtn(self):
        back_img = Image.open('images/back_btn_image.png').resize((25, 25))
        self.backbtn_img = ImageTk.PhotoImage(back_img)
        backbutton = Button(self.emailVerifyUI, 
                            image=self.backbtn_img, 
                            bg="black",
                            borderwidth=0,
                            activebackground="black",
                            width="18px",
                            height="18px",
                            command=self.emailVerifyInterfaceClosed)
        backbutton.place(relx=0.03, rely=0.03)

    def heading(self):
        #heading
        self.heading_label = self.canvas.create_text(300, 160,
                                 text="Confirm your Email!", 
                                 font=("Verdana", 25, "bold"),
                                 fill="white")

    def statement(self):
        #statement
        self.statement_label = self.canvas.create_text(300, 220,
                                 text="OTP is sent to "  + self.email, 
                                 font=("Verdana", 12, "bold"),
                                 fill="#12ECC0", justify="center")


    def otp(self):
        #otp
        self.otp_label = self.canvas.create_text(168, 280,
                                 text="Enter OTP ", 
                                 font=("Verdana", 15, "bold"),
                                 fill="white")
        vcmd = (self.emailVerifyUI.register(validate_numeric_input), '%P')
        self.otp_entry = Entry(self.emailVerifyUI, width=18, font=("Verdana", 15), justify="center", validate="key", validatecommand=vcmd) 
        self.canvas.create_window(390, 280, anchor='center', window=self.otp_entry)
    
    def verify_button(self):
        #verify btn
        border_frame = Frame(self.emailVerifyUI,
                         bg="#12ECC0", 
                         bd=2) 
        border_frame.place(relx=0.5, rely=0.6, anchor='center')

        self.verify_btn = Button(border_frame,
                    text="Verify Email",
                    bg="black",
                    fg="#12ECC0",
                    font=("Verdana", 11, "bold"),
                    activebackground="#12ECC0",
                    activeforeground="black",
                    width=10,
                    command=self.verify_email) #Command to be defined
        self.verify_btn.pack() 

    def resend_btn(self):
        self.question_label = self.canvas.create_text(250, 420, 
                                                      text="Didn't receive the code? ",
                                                      font=("Verdana", 12),
                                                      fill="white", 
                                                      justify="center")
        
        self.resend_label = self.canvas.create_text(400, 420,
                                                    text=" Resend code",
                                                    font=("Verdana", 12),
                                                    fill="#12ECC0",
                                                    justify="center")
        
        self.canvas.tag_bind(self.resend_label, "<Button-1>", self.on_resend_label_click)

    def on_resend_label_click(self, event):
        message = '''
            Thank you for Signing up for Security Policy Management Tool.
            
        '''
        
        self.emailVerify = EmailVerification(self.email)
        self.emailVerify.generateOTP()
        self.emailVerify.sendOTP(message)

    def restart_program(self):
        print("Restarting script...")
        os.execv(sys.executable, ['python'] + sys.argv)    
    
    def verify_email(self):
        if self.emailVerify.validateOTP(self.otp_entry.get()):
            d = Database()
            d.insertCredentials(self.username , self.password , self.email)
            self.restart_program()

def validate_numeric_input(input):
    return input.isdigit() and len(input) <= 8 or input == ""

if __name__ == "__main__":
    root = Tk()
    verify = Email_verification_Interface(root)
