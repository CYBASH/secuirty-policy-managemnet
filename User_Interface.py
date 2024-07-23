from tkinter import *
from PIL import Image, ImageTk
from securitypolicy import *
from hash import *
from ProjectInfo import *
import re

class User_Interface:
    #Login Btn Definition
    def __init__(self, root, tempfile):
        self.root = root
        self.policyInterface = None
        self.root.title("Security Policy Management Project")
        self.root.configure(bg="#505050")
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.policyTempFile = tempfile


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
            
            policyUI = Policies_Interface(self.root, self.policyInterface, self.policyTempFile)
            policyUI.openPolicyInterface()
            
            

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
        policyInterface.geometry('500x500')
        policyInterface.resizable(False, False)

        self.policyNameLabel()
        self.policyDescriptionLabel()
        self.addPolicyButton()
        self.updatePolicyButton()
        self.displayPolicyList()
        self.enforcePolicyButton()
        self.logoutButton()

    def policyNameLabel(self):
        #Policy Name
        policy_label = Label(self.policyInterface, text="Policy Name:", padx=5, font=("Verdana", 11))
        policy_label.grid(row=0, column=0, padx=(100, 10), pady=(25, 10), sticky=E)  
        self.policy_entry = Entry(self.policyInterface)
        self.policy_entry.grid(row=0, column=1, padx=(10, 100), pady=(25, 10), sticky=W) 
    
    def policyDescriptionLabel(self):
        #Policy Description
        desc_label = Label(self.policyInterface, text="Description:", padx=10, font=("Verdana", 11))
        desc_label.grid(row=1, column=0, padx=(100, 10), pady=10, sticky=E)  
        self.desc_entry = Entry(self.policyInterface)
        self.desc_entry.grid(row=1, column=1, padx=(10, 100), pady=10, sticky=W) 

    def addPolicyButton(self):
        #Add_policy Btn
        add_policy_btn = Button(self.policyInterface,
                    text="Add Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=2,
                    command=self.addPolicy)
        add_policy_btn.grid(row=2, column=0, padx=20, pady=10, sticky=E)
    
    def updatePolicyButton(self):
        #Update_policy btn
        self.update_policy_btn = Button(self.policyInterface,
                    text="Update Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.updatePolicy)
        self.update_policy_btn.grid(row=2, column=1, padx=20, pady=10, sticky=W)

    def displayPolicyList(self):
        #Policies_list
        policies_frame = Frame(self.policyInterface)
        policies_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky=NSEW)
        self.policies_list = Text(policies_frame, wrap="none", font=("Verdana", 11), height=10)
        self.policies_list.grid(row=0, column=0, sticky=NSEW)
        yscrollbar = Scrollbar(policies_frame, orient="vertical", command=self.policies_list.yview)
        yscrollbar.grid(row=0, column=1, sticky=NS)
        xscrollbar = Scrollbar(policies_frame, orient="horizontal", command=self.policies_list.xview)
        xscrollbar.grid(row=1, column=0, sticky=EW)
        self.policies_list.config(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

        self.policyInterface.grid_rowconfigure(3, weight=1)
        self.policyInterface.grid_columnconfigure(0, weight=1)
        self.policyInterface.grid_columnconfigure(1, weight=5)
        self.policyInterface.grid_rowconfigure(4, weight=5)
        policies_frame.grid_rowconfigure(0, weight=1)
        policies_frame.grid_columnconfigure(0, weight=1)

        self.load_file()
    

    def enforcePolicyButton(self):
        #Enforce Policy Btn
        self.enforce_policy_btn = Button(self.policyInterface,
                    text="Enforce Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.enforcePolicy)
        self.enforce_policy_btn.grid(row=4, column=0, padx=20, pady=5, columnspan=2)

    def logoutButton(self):
        #Logout Btn
        self.logout_btn = Button(self.policyInterface,
                    text="Logout",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.logout)
        self.logout_btn.grid(row=5, column=0, padx=20, pady=(0,40), columnspan=2, sticky=N)

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