from tkinter import *

#UI Starter
def startUI():
    root.mainloop()

#add policy btn definition
def add_policy():
    print("Add Policy Btn clicked")

#update policy btn definition
def update_policy():
    print("Update Policy Btn clicked")

#load text file
def load_file():
    policies = []
    with open("policies.txt", "r") as file:
        policies = file.readlines()
        policies_list.config(state="normal")
        policies_list.delete("1.0", END)
        for policy in policies:
            policies_list.insert(END, policy)   

#enforce policy btn definition
def enforce_policy():
    print("Enforce Policy Btn clicked")

#Logout btn definition
def logout():
    print("Logout Btn clicked")        
    
#Window dim specification
root = Tk()
root.title("Security Policy Management Project")
root.configure(bg="#505050")
root.geometry('500x500')
root.resizable(False, False)

#Policy Name
policy_label = Label(root, text="Policy Name:", padx=5, font=("Verdana", 11))
policy_label.grid(row=0, column=0, padx=(100, 10), pady=(25, 10), sticky=E)  
policy_entry = Entry(root)
policy_entry.grid(row=0, column=1, padx=(10, 100), pady=(25, 10), sticky=W) 

#Description
desc_label = Label(root, text="Description:", padx=10, font=("Verdana", 11))
desc_label.grid(row=1, column=0, padx=(100, 10), pady=10, sticky=E)  
desc_entry = Entry(root)
desc_entry.grid(row=1, column=1, padx=(10, 100), pady=10, sticky=W) 

#Add_policy Btn
add_policy_btn = Button(root,
             text="Add Policy",
             bg="white",
             fg="black",
             font=("Verdana", 11),
             padx=2,
             command=add_policy)
add_policy_btn.grid(row=2, column=0, padx=20, pady=10, sticky=E) 

#Update_policy btn
update_policy_btn = Button(root,
             text="Update Policy",
             bg="white",
             fg="black",
             font=("Verdana", 11),
             padx=4,
             command=update_policy)
update_policy_btn.grid(row=2, column=1, padx=20, pady=10, sticky=W)

#Policies_list
policies_frame = Frame(root)
policies_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky=NSEW)
policies_list = Text(policies_frame, wrap="none", font=("Verdana", 11), height=10)
policies_list.grid(row=0, column=0, sticky=NSEW)
yscrollbar = Scrollbar(policies_frame, orient="vertical", command=policies_list.yview)
yscrollbar.grid(row=0, column=1, sticky=NS)
xscrollbar = Scrollbar(policies_frame, orient="horizontal", command=policies_list.xview)
xscrollbar.grid(row=1, column=0, sticky=EW)
policies_list.config(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=5)
root.grid_rowconfigure(4, weight=5)
policies_frame.grid_rowconfigure(0, weight=1)
policies_frame.grid_columnconfigure(0, weight=1)

load_file()

#Enforce Policy Btn
enforce_policy_btn = Button(root,
             text="Enforce Policy",
             bg="white",
             fg="black",
             font=("Verdana", 11),
             padx=4,
             command=enforce_policy)
enforce_policy_btn.grid(row=4, column=0, padx=20, pady=5, columnspan=2)

#Logout Btn
logout_btn = Button(root,
             text="Logout",
             bg="white",
             fg="black",
             font=("Verdana", 11),
             padx=4,
             command=logout)
logout_btn.grid(row=5, column=0, padx=20, pady=(0,40), columnspan=2, sticky=N)

startUI()