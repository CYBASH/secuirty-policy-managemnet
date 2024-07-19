from tkinter import *
import webbrowser

root = Tk() 
#Title
root.title("Security Policy Management Project")
root.geometry('500x500')

def clicked():
    webbrowser.open('file:///C:\Users\sivay\Desktop\Security_Policy_Management\secuirty-policy-managemnet\sample_info.html')

btn = Button(root, text = "Button", fg = "red", command=clicked)
btn.pack()
a = Label(root, 
          bg="#D3D3D3", 
          fg="black", 
          padx=20,
          text="Security Policy Management Project",
          font=("Helvetica", 12, "bold"))
a.pack()


root.mainloop() 