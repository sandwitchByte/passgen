from tkinter import *
from tkinter import ttk
import secrets
import string
import pyperclip

'''

#define main window
main = Tk() 
main.title("super strong password generator <3")
main.geometry("500x100+200+200")

test = ttk.Label(text="aaaaaaaaaaaaa")
test.pack(side = ttk.left)

#function to make text copy-able
def focusText(event):
    w.config(state='normal')
    w.focus()
    w.config(state='disabled')

w = Text(main, height=1, borderwidth=0, )
w.insert(1.0, "Hello, world!")
w.pack()


'''


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
    print(pwd)

root = Tk()
root.geometry('500x350')
root.title("super strong password generator <3")
frm = ttk.Frame(root, padding=155, width=0, height=500)
frm.grid()



ttk.Label(frm, text="Secure password generator.").grid(column=0, row=0)
ttk.Button(frm, text="Generate!", command=callback).grid(column=0, row=1)


root = Tk()
frm1 = ttk.Frame(root, padding=100, width=1000, height=500)
frm1.grid()
ttk.Label(frm1, text="Your new password is:").grid(column=0, row=0)
ttk.Label(frm1, text=pwd).grid(column=0, row=1)
ttk.Button(frm1, text="OK", command=root.quit).grid(column=0, row=2)



letters = string.ascii_letters
digits = string.digits
special = string.punctuation

alphabet = letters + digits + special

pwd_length = 13



root.mainloop()


