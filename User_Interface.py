from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *
import re
from signup_interface import *

class User_Interface:
    #Login Btn Definition
    def __init__(self, root, tempfile):
        self.root = root
        self.policyInterface = None
        self.root.title("Security Policy Management Project")
        self.root.configure(bg="#505050")
        self.root.geometry('600x600')
        self.root.resizable(False, False)
        self.root.iconbitmap("images/icon.ico")
        self.background_image = ImageTk.PhotoImage(Image.open("images/background.jpeg"))
        self.canvas = Canvas(self.root , width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        self.background_color = self.background_image._PhotoImage__photo.get(0, 0)
        
        self.policyTempFile = tempfile
        self.info_button()
        self.heading()
        self.picture()
        self.username()
        self.password()
        self.login_button()
        self.signup_button()


    #Project Info Button 
    def info_button(self):        
        self.info_btn = Button(self.root,
                    text="Project Info",
                    bg="blue",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=4,
                    command=self.project_info)
        self.info_btn.place(relx=0.5, rely=0.05, anchor='center')  

    def heading(self):
        #Project Heading
        self.heading_lbl = Label(self.root,
                bg="white",
                fg="black",
                padx=20,
                text="Security Policy Management Project",
                font=("Verdana", 14, "bold"))
        self.heading_lbl.place(relx=0.5, rely=0.15, anchor='center')

    def picture(self):
        #Picture
        self.image = Image.open("images/Security_Policy_manage_pic.png")
        self.dim = (200, 200)
        self.adj_img = self.image.resize(self.dim)
        self.photo = ImageTk.PhotoImage(self.adj_img)
        self.image_label = Label(self.root, bg="#505050", image=self.photo)
        self.image_label.place(relx=0.5, rely=0.45, anchor='center')

    def username(self):
        #username
        self.username_label = Label(self.root, text="Username:", padx=9, font=("Verdana", 11, "bold"))
        self.username_label.place(relx=0.35, rely=0.7, anchor='center')  
        self.username_entry = Entry(self.root)
        self.username_entry.place(relx=0.65, rely=0.7, anchor='center') 

    def password(self):
        #password
        self.password_label = Label(self.root, text="Password:", padx=10, font=("Verdana", 11, "bold"))
        self.password_label.place(relx=0.35, rely=0.8, anchor='center')   
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.place(relx=0.65, rely=0.8, anchor='center')  

    def login_button(self):
        #Login Btn
        self.login_btn = Button(self.root,
                    text="Login",
                    bg="blue",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=4,
                    command=self.login) #Command to be defined
        self.login_btn.place(relx=0.6, rely=0.9, anchor='center')  

    def signup_button(self):
        #signup btn
        self.signup_btn = Button(self.root,
                    text="Sign Up",
                    bg="blue",
                    fg="white",
                    font=("Verdana", 11, "bold"),
                    padx=4,
                    command=self.signup) #Command to be defined
        self.signup_btn.place(relx=0.4, rely=0.9, anchor='center')  

    #Start UI
    def startUI(self):
        self.root.mainloop()

    
    def matchPasswords():
        pass
    
    
    def login(self):
        print("Login Btn CLicked")

        if self.username_entry.get() == "":
            messagebox.showinfo( "Warning", "Please enter USERNAME")
        
        elif self.password_entry.get() == "":
            messagebox.showinfo( "Warning", "Please enter PASSWORD")
        
        else:
            self.p = Password(self.password_entry.get())
            self.p.encrypt()

            self.d = Database()
        
        
        
        
            if (self.p.getHashCode()) == (self.d.getPassword(self.username_entry.get())):
                print("Logged in")
                #messagebox.showinfo( "Warning", "Logged in")
                policyUI = Policies_Interface(self.root, self.policyInterface, self.policyTempFile)
                policyUI.openPolicyInterface()
                
                

            else:
                print("Wrong password")
                messagebox.showinfo( "Warning", "Wrong Username or Password")

    #Signup Btn Definition   
    def signup(self):
        print("Sign Up Btn CLicked")
        
        self.d = Database()
        #self.d.insertCredentials(self.username_entry.get(), self.password_entry.get()) #also need to pass email_entry.get()
        signupUI = Signup_Interface(self.root)
        signupUI.startUI()

    #Project Info Btn definition
    def project_info(self):
        self.html_content = """
            <html>
                <head>
                    <title>
                        Project Information
                    </title>

                    <style>
                        .container{
                        width: 60%;
                        height: 180%;
                        background-color:white;
                        position: absolute;
                        left: 270px;
                        padding-left: 25px;
                        padding-right: 25px;
                        padding-top: 60px;
                        border-color: grey 20px;
                        }
                        table,th,td{
                        height: 60px;
                        border: 1px solid black;
                        border-collapse: collapse;
                        text-align:left;
                        padding: 13px;
                        
                        }
                        img{
                        width: 100;
                        height: 100;
                        position: absolute;
                        top: 35px;;
                        right: 35px; 
                        border-radius: 50%;
                        }
                        .container{
                        box-shadow: 5px 5px 5px 5px  gray;
                        }
                        th{
                        
                        background-color: hsla(120, 4%, 74%, 0.3);
                        }
                    </style>

                </head>
                    <body style="background-color: aliceblue;">
                        <div class="container">
                        <img src="pro4.jpeg" style="width:13%;height:10%;">
                            <h1> Project Information </h1>
                            <br>
                                    <p>This project was developed  by <b> Anonymous Hacker </b>as a part of a <b>Cyber Security Internship</b>.This 
                                    project is designed to <b>Secure the Organizations in Real World from Cyber Frauds performed by
                                        Hackers.</b></p>
                                <table style="width: 100%;">
                                    <tr>
                                    <th> Project Details </th>
                                    <th> Value</th>
                                    </tr>
                                    <tr>
                                    <td>Project Name</td>
                                    <td>Security Policy Management</td>
                                </tr>
                                <tr>
                                    <td>Project Description</td>
                                    <td> It involves creating, implement,and maintain policies that govern the Security
                                        measures and practices within an organization to protect its information and resources.
                                    </td>
                                </tr>
                                <tr>
                                    <td>Project Start Date</td>
                                    <td>01-July-2024</td>
                                </tr>
                                <tr>
                                    <td> Project End Date</td>
                                    <td>24-August-2024</td>
                                    
                                </tr>
                                <tr>
                                    <td>Project Status</td>
                                    <td><b>Completed</b></td>
                                </tr>
                            </table >
                            <h2> Developer Details</h2>
                            <table style="width: 100%;">
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                </tr>
                            
                                <tr>
                                    <td>Akurathi Sasidhar</td>
                                    <td>sasidhardaicy@gmail.com</td>
                                </tr>
                                <tr>
                                    <td>Thota Satish Babu</td>
                                    <td>22ktsatish5b6@gmail.com</td>
                                </tr>
                            <tr>
                                <td> Gajivelli Venkata Jaya Sivaram</td>
                                <td>sivaramgajivelli@gmail.com</td>
                            </tr>
                            <tr>
                                <td>Mamidi jovel</td>
                                <td>jovelmamidi20@gmail.com</td>
                            </tr>
                            <tr>
                                <td>Gogula Sri Supriya</td>
                                <td>srisupriyagogula@gmail.com</td>
                            </tr> 
                            </table>
                            <h2>Company Details</h2>
                            <table style="width: 100%;">
                                <tr>
                                    <th>Name</th>
                                    <th>Supraja Technologies</th>
                                </tr>
                                <tr> 
                                    <td>Email</td>
                                    <td> contact@suprajatechnologies.com</td>

                                </tr>
                            </table>
                        </div>
                    </body>
            </html>
        """

        self.project_info = ProjectInfo(self.html_content)
        self.project_info.openTempFileInThread()

def hideWindow(window):
    window.withdraw()

def showWindow(window):
    window.deiconify()

def clear_entries(window):
    # Iterate over all widgets in the root window
    for widget in window.winfo_children():
        # Check if the widget is an instance of Entry
        if isinstance(widget, Entry):
            widget.delete(0, END) 


class Policies_Interface:
    def __init__(self, root ,policyInterface, policyTempFile):
        self.root = root
        self.policyInterface = policyInterface
        self.policyTempFile = policyTempFile

    def policyInterfaceClosed(self):
        self.root.destroy()

    def openPolicyInterface(self):
        hideWindow(self.root)

        policyInterface = Toplevel(self.root)
        policyInterface.protocol("WM_DELETE_WINDOW", self.policyInterfaceClosed)
        self.policyInterface = policyInterface
        policyInterface.title("Security Policy Management Project")
        policyInterface.configure(bg="#505050")
        policyInterface.geometry('600x600')
        policyInterface.resizable(True, True)
        policyInterface.iconbitmap("images/icon.ico")
        self.background_image = ImageTk.PhotoImage(Image.open("images/background.jpeg"))
        self.canvas = Canvas(self.policyInterface, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        self.background_color = self.background_image._PhotoImage__photo.get(0, 0)

        self.policyNameLabel()
        self.policyDescriptionLabel()
        self.addPolicyButton()
        self.updatePolicyButton()
        self.displayPolicyList()
        self.enforcePolicyButton()
        self.logoutButton()

    def policyNameLabel(self):
        #Policy Name
        self.policy_label = Label(self.policyInterface, text="Policy Name:", padx=5, font=("Verdana", 11))
        self.policy_label.place(relx=0.35, rely=0.05, anchor='center')   
        self.policy_entry = Entry(self.policyInterface)
        self.policy_entry.place(relx=0.65, rely=0.05, anchor='center')  
    
    def policyDescriptionLabel(self):
        #Policy Description
        self.desc_label = Label(self.policyInterface, text="Description:", padx=10, font=("Verdana", 11))
        self.desc_label.place(relx=0.35, rely=0.15, anchor='center')  
        self.desc_entry = Entry(self.policyInterface)
        self.desc_entry.place(relx=0.65, rely=0.15, anchor='center')  

    def addPolicyButton(self):
        #Add_policy Btn
        self.add_policy_btn = Button(self.policyInterface,
                    text="Add Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=2,
                    command=self.addPolicy)
        self.add_policy_btn.place(relx=0.35, rely=0.25, anchor='center')  
    
    def updatePolicyButton(self):
        #Update_policy btn
        self.update_policy_btn = Button(self.policyInterface,
                    text="Update Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.updatePolicy)
        self.update_policy_btn.place(relx=0.65, rely=0.25, anchor='center')  

    def displayPolicyList(self):
        # Policies_list
        policies_frame = Frame(self.policyInterface, bg="#505050")
        policies_frame.place(relx=0.5, rely=0.55, anchor='center')

        self.policies_list = Text(policies_frame, wrap="none", font=("Verdana", 11), height=10, width=40)
        self.policies_list.grid(row=0, column=0, sticky='nsew')

        yscrollbar = Scrollbar(policies_frame, orient="vertical", command=self.policies_list.yview)
        yscrollbar.grid(row=0, column=1, sticky='ns')

        xscrollbar = Scrollbar(policies_frame, orient="horizontal", command=self.policies_list.xview)
        xscrollbar.grid(row=1, column=0, sticky='ew')

        self.policies_list.config(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

        policies_frame.grid_rowconfigure(0, weight=1)
        policies_frame.grid_columnconfigure(0, weight=1)

        self.policyInterface.grid_rowconfigure(3, weight=1)
        self.policyInterface.grid_columnconfigure(1, weight=1)
        self.policyInterface.grid_columnconfigure(1, weight=5)
        self.policyInterface.grid_rowconfigure(4, weight=5)
        self.policyInterface.bind('<Configure>', lambda event: self.resize_policy_frame(policies_frame))
        self.load_file()

    def resize_policy_frame(self, frame):
        width = self.policyInterface.winfo_width()
        height = self.policyInterface.winfo_height()
        frame.place_configure(width=width*0.8, height=height*0.4)    

    def enforcePolicyButton(self):
        #Enforce Policy Btn
        self.enforce_policy_btn = Button(self.policyInterface,
                    text="Enforce Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.enforcePolicy)
        self.enforce_policy_btn.place(relx=0.5, rely=0.85, anchor='center')

    def logoutButton(self):
        #Logout Btn
        self.logout_btn = Button(self.policyInterface,
                    text="Logout",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.logout)
        self.logout_btn.place(relx=0.5, rely=0.95, anchor='center')

    def load_file(self):
        with open(self.policyTempFile, "r") as file:
            i = 0
            self.policies = file.readlines()
            self.policies_list.config(state="normal")
            self.policies_list.delete("1.0", END)
            for policy in self.policies:
                i += 1
                x = str(i) + ". " + policy
                self.policies_list.insert(END, policy)
            self.policies_list.config(state="disabled")  

    #add policy btn definition
    def addPolicy(self):
        print("Add Policy Btn clicked")
        if (self.policy_entry.get()=="" or self.desc_entry.get()==""):
            print("Please enter policy and description")
        else:
            self.addPolicyToFile()
            self.load_file()
        

    #update policy btn definition
    def updatePolicy(self):
        print("Update Policy Btn clicked")
        if (self.policy_entry.get()=="" or self.desc_entry.get()==""):
            print("Please enter policy and description")
        else:
            self.updatePolicyToFile()
            self.load_file()

    #enforce policy btn definition
    def enforcePolicy(self):
        print("Enforce Policy Btn clicked")
        p = Policy(self.policy_entry.get(), self.desc_entry.get())
        x = self.parsePolicies(self.policyTempFile)
        p.enforcePolicies(x)


    #Logout btn definition
    def logout(self):
        print("Logout Btn clicked")
        clear_entries(self.root)
        hideWindow(self.policyInterface)
        showWindow(self.root)
    
    def updatePolicyToFile(self):
        policyFound = False
        with open(self.policyTempFile, 'r') as file:
            lines = file.readlines()
        
        # Modify the content
        with open(self.policyTempFile, 'w') as file:
            for line in lines:
                if self.policy_entry.get() in line:
                    match = re.match(r"^(\d+)\. (.*?): (.*?) \((v\d+)\)$", line.strip())
                    if match:
                        id, name, description, version = match.groups()
                        version = int(version[1:])+1
                        sentence = f"{id}. " + self.policy_entry.get() + ": " + self.desc_entry.get() + f" (v{version})"
                        file.write(sentence + '\n')
                        policyFound = True
                else:
                    file.write(line)
                
        if not policyFound:
            print("Policy not found.")

    
    def parsePolicies(self, file_path):
        policies = []
        with open(file_path, 'r') as file:
            for line in file:
                match = re.match(r"^(\d+)\. (.*?): (.*?) \((v\d+)\)$", line.strip())
                if match:
                    id, name, description, version = match.groups()
                    version = int(version[1:])
                    policies.append((id, name, description, version))
        return policies
    
    def addPolicyToFile(self):
        sentence = ""

        with open(self.policyTempFile, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                if self.policy_entry.get() in line:
                    print("Policy already exists")
                    return


        with open(self.policyTempFile, 'r') as file:
            lines = file.readlines()
            if lines:
                match = re.match(r"^(\d+)\. (.*?): (.*?) \((v\d+)\)$", lines[-1].strip())
                if match:
                    id, name, description, version = match.groups()
                    id = int(id) + 1
                    sentence = f"{id}. " + self.policy_entry.get() + ": " + self.desc_entry.get() + " (v1)"
                    
        with open(self.policyTempFile, 'a') as file:
            file.write(sentence + '\n')


def startMainUI(tempFileName):
    root = Tk()
    app = User_Interface(root, tempFileName)
    app.startUI()