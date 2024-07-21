from tkinter import *
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *

class User_Interface:
    #Login Btn Definition
    def __init__(self, root):
        self.root = root
        self.root.title("Security Policy Management Project")
        self.root.configure(bg="#505050")
        self.root.geometry('500x500')
        self.root.resizable(False, False)

        #Project Info Button 
        self.info_btn = Button(self.root,
                    text="Project Info",
                    bg="blue",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=4,
                    command=self.project_info)
        self.info_btn.grid(row=0, column=0, padx=20, pady=20, columnspan=2) 

        #Project Heading
        self.heading = Label(self.root,
                bg="white",
                fg="black",
                padx=20,
                text="Security Policy Management Project",
                font=("Verdana", 14, "bold"))
        self.heading.grid(row=1, column=0, columnspan=2, padx=40, pady=10) 

        #Picture
        self.image = Image.open("Security_Policy_manage_pic.png")
        self.dim = (200, 200)
        self.adj_img = self.image.resize(self.dim)
        self.photo = ImageTk.PhotoImage(self.adj_img)
        self.image_label = Label(self.root, bg="#505050", image=self.photo)
        self.image_label.grid(row=2, column=0, padx=50, pady=10, columnspan=2, sticky=EW)

        #username
        self.username_label = Label(self.root, text="Username:", padx=9, font=("Verdana", 11, "bold"))
        self.username_label.grid(row=3, column=0, padx=40, pady=10, sticky=E)  
        self.username_entry = Entry(self.root)
        self.username_entry.grid(row=3, column=1, padx=40, pady=10, sticky=W)  

        #password
        self.password_label = Label(self.root, text="Password:", padx=10, font=("Verdana", 11, "bold"))
        self.password_label.grid(row=4, column=0, padx=40, pady=10, sticky=E)  
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(row=4, column=1, padx=40, pady=10, sticky=W)

        #Login Btn
        self.login_btn = Button(self.root,
                    text="Login",
                    bg="blue",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=4,
                    command=self.login) #Command to be defined
        self.login_btn.grid(row=5, column=1, padx=20, pady=10, columnspan=2, sticky=W)

        #signup btn
        self.signup_btn = Button(self.root,
                    text="Sign Up",
                    bg="blue",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=4,
                    command=self.signup) #Command to be defined
        self.signup_btn.grid(row=5, column=0, padx=150, pady=10, columnspan=2, sticky=W)

    #Start UI
    def startUI(self):
        self.root.mainloop()

    def login(self):
        print("Login Btn CLicked")

        self.p = Password(self.password_entry.get())
        self.p.encrypt()

        self.d = Database()
        if (self.p.getHashCode()) == (self.d.getPassword(self.username_entry.get())):
            print("Logged in")
        else:
            print("Wrong password")

    #Signup Btn Definition   
    def signup(self):
        print("Sign Up Btn CLicked")

        self.d = Database()
        self.d.insertCredentials(self.username_entry.get(), self.password_entry.get()) #also need to pass email_entry.get()

    #Project Info Btn definition
    def project_info(self):
        self.html_content = """
            <html>
                <head>
                    <title>Project Info</title>
                </head>
            <body>
                <h1>Project Info</h1>
                    <p>This is a sample project info page.</p>
                </body>
            </html>
        """

        self.project_info = ProjectInfo(self.html_content)
        self.project_info.openTempFileInThread()

if __name__ == "__main__":
    root = Tk()
    app = User_Interface(root)
    app.startUI()  