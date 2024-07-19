from tkinter import *
import webbrowser

root = Tk() 
#Title
root.title("Security Policy Management Project")
# root.configure(bg="#505050")
bg = PhotoImage(file="background.jpeg")
root.geometry('500x500')

def project_info():
    webbrowser.open('file:///C:/Users/sivay/Desktop/Security%20Policy%20Management/secuirty-policy-managemnet/sample_info.html')

btn = Button(root, 
             text = "Project Info",
             bg="blue",
             fg = "white", 
             font=("Verdana", 11, "bold"),
             padx=4,
             command=project_info)
btn.pack(pady=20)

a = Label(root, 
          bg="white", 
          fg="black", 
          padx=20,
          text="Security Policy Management Project",
          font=("Verdana", 14, "bold"))
a.pack()


root.mainloop() 