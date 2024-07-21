from tkinter import *

class Policies_Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Policy Management Project")
        self.root.configure(bg="#505050")
        self.root.geometry('500x500')
        self.root.resizable(False, False)

        #Policy Name
        self.policy_label = Label(self.root, text="Policy Name:", padx=5, font=("Verdana", 11))
        self.policy_label.grid(row=0, column=0, padx=(100, 10), pady=(25, 10), sticky=E)  
        self.policy_entry = Entry(self.root)
        self.policy_entry.grid(row=0, column=1, padx=(10, 100), pady=(25, 10), sticky=W) 

        #Description
        self.desc_label = Label(self.root, text="Description:", padx=10, font=("Verdana", 11))
        self.desc_label.grid(row=1, column=0, padx=(100, 10), pady=10, sticky=E)  
        self.desc_entry = Entry(self.root)
        self.desc_entry.grid(row=1, column=1, padx=(10, 100), pady=10, sticky=W) 

        #Add_policy Btn
        add_policy_btn = Button(self.root,
                    text="Add Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=2,
                    command=self.add_policy)
        add_policy_btn.grid(row=2, column=0, padx=20, pady=10, sticky=E) 

        #Update_policy btn
        self.update_policy_btn = Button(self.root,
                    text="Update Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.update_policy)
        self.update_policy_btn.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        #Policies_list
        self.policies_frame = Frame(self.root)
        self.policies_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky=NSEW)
        self.policies_list = Text(self.policies_frame, wrap="none", font=("Verdana", 11), height=10)
        self.policies_list.grid(row=0, column=0, sticky=NSEW)
        self.yscrollbar = Scrollbar(self.policies_frame, orient="vertical", command=self.policies_list.yview)
        self.yscrollbar.grid(row=0, column=1, sticky=NS)
        self.xscrollbar = Scrollbar(self.policies_frame, orient="horizontal", command=self.policies_list.xview)
        self.xscrollbar.grid(row=1, column=0, sticky=EW)
        self.policies_list.config(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)

        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=5)
        self.root.grid_rowconfigure(4, weight=5)
        self.policies_frame.grid_rowconfigure(0, weight=1)
        self.policies_frame.grid_columnconfigure(0, weight=1)

        self.load_file()

        #Enforce Policy Btn
        self.enforce_policy_btn = Button(self.root,
                    text="Enforce Policy",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.enforce_policy)
        self.enforce_policy_btn.grid(row=4, column=0, padx=20, pady=5, columnspan=2)

        #Logout Btn
        self.logout_btn = Button(self.root,
                    text="Logout",
                    bg="white",
                    fg="black",
                    font=("Verdana", 11),
                    padx=4,
                    command=self.logout)
        self.logout_btn.grid(row=5, column=0, padx=20, pady=(0,40), columnspan=2, sticky=N)
    
    def startUI(self):
        self.root.mainloop()

    #add policy btn definition
    def add_policy(self):
        print("Add Policy Btn clicked")

    #update policy btn definition
    def update_policy(self):
        print("Update Policy Btn clicked")

    #load text file
    def load_file(self):
        policies = []
        with open("policies.txt", "r") as file:
            self.policies = file.readlines()
            self.policies_list.config(state="normal")
            self.policies_list.delete("1.0", END)
            for self.policy in self.policies:
                self.policies_list.insert(END, self.policy) 
            self.policies_list.config(state="disabled")  

    #enforce policy btn definition
    def enforce_policy(self):
        print("Enforce Policy Btn clicked")

    #Logout btn definition
    def logout(self):
        print("Logout Btn clicked")     

if __name__ == "__main__":
    root = Tk()
    app = Policies_Interface(root)
    app.startUI()  