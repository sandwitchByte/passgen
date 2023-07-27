from tkinter import *
from tkinter import ttk
import secrets
import string
import time
import pyperclip

root = Tk()
root.geometry('500x350')
root.title("super strong password generator <3")
frm = ttk.Frame(root, padding=150, width=0, height=500)
frm.grid()

def copy():
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(pwd)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()


letters = string.ascii_letters
digits = string.digits
special = string.punctuation

alphabet = letters + digits + special

pwd_length = 13
pwd = ''
def callback():
    while True:
        pwd = ' '
        for i in range(pwd_length):
            pwd += ' '.join(secrets.choice(alphabet))
        if (sum(char in special for char in pwd)<=2 and
            sum(char in digits for char in pwd)>=2 and
            sum(char in digits for char in pwd)<=5 and
            sum(char in letters for char in pwd)>=5):
            break
    #frm1 = ttk.Frame(root, padding=100, width=1000, height=500)
    #frm1.grid()
    ttk.Label(frm, text="Your new password is:").grid(column=0, row=2)
    ttk.Label(frm, text=pwd).grid(column=0, row=3)
    ttk.Button(frm, text="copy", command=copy()).grid(column=0, row=4)


#    print(pwd)




#copy()

#root = Tk()
ttk.Label(frm, text="Secure password generator.").grid(column=0, row=0)
ttk.Button(frm, text="Generate!", command=callback).grid(column=0, row=1)


root.mainloop()
