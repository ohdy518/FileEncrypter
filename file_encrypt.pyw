import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename
import getpass, pyAesCrypt, time, asyncio, os
from tkinter import messagebox
filename = 0
foldername = 0
password = 0
approved = False
def none():
    pass
def fileget(_=any):
    global filename
    filename = askopenfilename()
    if filename != "":
        labelfilename.config(text=f"File Selected: {filename}")
def locget(_=any):
    global foldername
    foldername = askdirectory()
    if filename != "":
        labellocname.config(text=f"Folder Selected: {foldername}")
def passwordprompt(_=any):
    # Passowrd Prompt
    global pwpt
    global pwptwn
    pwptwn = tk.Toplevel()
    pwptwn.iconbitmap("app.ico")
    pwpt = tk.Entry(pwptwn, show="*")
    pwpt.pack()
    pwpt.place(x=10, y=10)
    savebtn = tk.Button(pwptwn, text="Save password", font=("Arial", 16), command=savepw)
    savebtn.pack()
    savebtn.place(x=10, y=48)
def savepw(_=str):
    global pwpt, password, pwptwn
    password = pwpt.get()
    try: 
        passwordlabel.config(text=f"{[i for i in password][0]}{(len(password) - 1) * '*'}")
        pwptwn.destroy()
    except: 
        messagebox.showerror(title="Password Error", message="Cannot set password")
        password = 0
async def cont():
    global pwconfirmwn
    while True:
        if approved:
            pwconfirmwn.destroy()
            messagebox.showwarning(title="Encryption Warning", message="Encryption will start soon.\nDo not close this window")
            root.protocol("WM_DELETE_WINDOW", none)
            pyAesCrypt.encryptFile(filename, foldername + "\\" + filename.split('/')[-1:][0] + ".aes", password)
            messagebox.showinfo(title="Encryption success", message="Done Encrypting")
            root.protocol("WM_DELETE_WINDOW", root.destroy)
            break
        else: 
            pass
def is_app(): 
    global pwcn, approved
    pwcn.get()
    if pwcn.get() == password:
        approved = True
        asyncio.run(cont())
    else:
        messagebox.showerror(title="Password Error", message="Password does not match")
        approved == False
    approved
def encrypt(_=any):
    global pwcn, pwconfirmwn
    if filename and password and foldername != 0:
        pwconfirmwn = tk.Toplevel()
        pwconfirmwn.iconbitmap("app.ico")
        pwcn = tk.Entry(pwconfirmwn, show="*")
        pwcn.pack()
        pwcn.place(x=10, y=10)
        deslabel = tk.Label(pwconfirmwn, text="Enter password", font=("Arial", 12))
        deslabel.pack()
        deslabel.place(x=10, y=40)
        ckbtn = tk.Button(pwconfirmwn, text="Encrypt", font=("Arial", 16), command=is_app)
        ckbtn.pack()
        ckbtn.place(x=10, y=72)
        
        pwconfirmwn.mainloop()
    else:
        pass
root = tk.Tk()
root.title("File Encrypt by codingPro01")
root.iconbitmap("app.ico")
root.geometry("512x512+32+32")
title = tk.Label(text="File Encrypt", font=("Arial", 32))
title.pack()
title.place(x=10, y=10)
getfile = tk.Button(text="Select file\nto encrypt", width=12, font=("Arial", 16), command=fileget)
getfile.pack()
getfile.place(x=20, y=72)
labelfilename = tk.Label(text="No file selected", font=("Arial", 12))
labelfilename.pack()
labelfilename.place(x=200, y=80)
getlocation = tk.Button(text="Select folder\nto save", width=12, font=("Arial", 16), command=locget)
getlocation.pack()
getlocation.place(x=20, y=160)
labellocname = tk.Label(text="No folder selected", font=("Arial", 12))
labellocname.pack()
labellocname.place(x=200, y=168)
passwordwindowopenbutton = tk.Button(text="Open Password Prompt", font=("Arial", 16),command=passwordprompt)
passwordwindowopenbutton.pack()
passwordwindowopenbutton.place(x=20, y=240)
passwordlabel = tk.Label(text="Password not set", font=("Arial", 12))
passwordlabel.pack()
passwordlabel.place(x=280, y=248)
encryptbutton = tk.Button(text="Encrypt", font=("Arial", 16), command=encrypt)
encryptbutton.pack()
encryptbutton.place(x=20, y=360)
root.protocol("WM_DELETE_WINDOW", root.destroy)
#
# filename = askopenfilename()
# password = getpass.getpass()
# pyAesCrypt.encryptFile(filename, f"{filename}.aes", password)
root.mainloop()