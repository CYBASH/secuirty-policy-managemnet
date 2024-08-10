#   https://youtu.be/HZqfyFA-xfk?si=eCKsUM4WetPMBEJZ        ->  Reference
#   nnqg pbdp ojsg cklj     ->  App Password for 22kt1a0595@gmail.com

#   SPM - mqot ougz ojjl vwcl   ->  App Password FOR spmproject66@gmail.com

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox


class EmailVerification():
    def __init__(self , mail):
        self.otp = None
        self.fromMail = 'spmproject66@gmail.com' 
        self.toMail = mail
    
    def generateOTP(self):
        self.otp = ""
        for i in range(0,8):
            self.otp += str(random.randint(0,9))
        print(self.otp)
        
        
    def sendOTP(self , message):
        server = smtplib.SMTP('smtp.gmail.com' , 587)
        server.starttls()
        
        server.login(self.fromMail, 'mqot ougz ojjl vwcl')
        
        html_content = f"""
        <html>
        <body>
            <p style="font-size:15px; font-weight: bold;">{message}</p>
            <p style="font-size:20px; font-weight: bold;">Your OTP is: {self.otp}</p>
        </body>
        </html>
        """
        
        msg = MIMEMultipart()
        msg['Subject'] = "OTP Verification"
        msg['From'] = self.fromMail
        msg['To'] = self.toMail
        msg.attach(MIMEText(html_content, 'html'))
        
        server.sendmail(self.fromMail, self.toMail, msg.as_string())
        server.quit()
        print("Email Sent")
        messagebox.showinfo( "Information", "OTP sent successfully")
    
    def validateOTP(self , enteredOTP):
        if self.otp == str(enteredOTP):
            print("Correct OTP")
            messagebox.showinfo( "Information", "Sign up successfully")
        else:
            print("Wrong OTP")
            messagebox.showinfo( "Warning", "Please enter correct OTP")
        





if __name__ == "__main__":
    
    message = '''
        Thank you for Signing up for Security Policy Management Tool.
        
    '''
    
    emailVerify = EmailVerification("sasidhardaicy@gmail.com")
    emailVerify.generateOTP()
    emailVerify.sendOTP(message)
    x = input("Enter OTP: ")
    emailVerify.validateOTP(x)
            