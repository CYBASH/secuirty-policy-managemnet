from tkinter import *
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *

#Login Btn Definition
def login():
    print("Login Btn CLicked")

    p = Password(password_entry.get())
    p.encrypt()

    d = Database()
    if (p.getHashCode()) == (d.getPassword(username_entry.get())):
        print("Logged in")
    else:
        print("Wrong password")

#Signup Btn Definition   
def signup():
    print("Sign Up Btn CLicked")

    d = Database()
    d.insertCredentials(username_entry.get(), password_entry.get()) #also need to pass email_entry.get()

#Project Info Btn definition
def project_info():
    html_content = """
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

    project_info = ProjectInfo(html_content)
    project_info.openTempFileInThread()

#Start UI
def startUI():
    root.mainloop()

root = Tk()
root.title("Security Policy Management Project")
root.configure(bg="#505050")
root.geometry('500x550')
root.resizable(False, False)

#Project Info Button 
info_btn = Button(root,
             text="Project Info",
             bg="blue",
             fg="white",
             font=("Verdana", 11, "bold"),
             padx=4,
             command=project_info)
info_btn.grid(row=0, column=0, padx=20, pady=20, columnspan=2) 

#Project Heading
a = Label(root,
          bg="white",
          fg="black",
          padx=20,
          text="Security Policy Management Project",
          font=("Verdana", 14, "bold"))
a.grid(row=1, column=0, columnspan=2, padx=40, pady=10) 

#Picture
image = Image.open("Security_Policy_manage_pic.png")
dim = (200, 200)
adj_img = image.resize(dim)
photo = ImageTk.PhotoImage(adj_img)
image_label = Label(root, bg="#505050", image=photo)
image_label.grid(row=2, column=0, padx=50, pady=10, columnspan=2, sticky=EW)

#username
username_label = Label(root, text="Username:", padx=9, font=("Verdana", 11, "bold"))
username_label.grid(row=3, column=0, padx=40, pady=10, sticky=E)  
username_entry = Entry(root)
username_entry.grid(row=3, column=1, padx=40, pady=10, sticky=W)  

#password
password_label = Label(root, text="Password:", padx=10, font=("Verdana", 11, "bold"))
password_label.grid(row=4, column=0, padx=40, pady=10, sticky=E)  
password_entry = Entry(root, show="*")
password_entry.grid(row=4, column=1, padx=40, pady=10, sticky=W)

#Login Btn
login_btn = Button(root,
             text="Login",
             bg="blue",
             fg="white",
             font=("Verdana", 11, "bold"),
             padx=4,
             command=login) #Command to be defined
login_btn.grid(row=5, column=1, padx=20, pady=10, columnspan=2, sticky=W)

#signup btn
signup_btn = Button(root,
             text="Sign Up",
             bg="blue",
             fg="white",
             font=("Verdana", 11, "bold"),
             padx=4,
             command=signup) #Command to be defined
signup_btn.grid(row=5, column=0, padx=150, pady=10, columnspan=2, sticky=W)

startUI()