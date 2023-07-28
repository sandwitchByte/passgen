from tkinter import *
from tkinter import ttk
import secrets
import string

### function defs

### important variables
letters = string.ascii_letters
digits = string.digits
special = string.punctuation

alphabet = letters + digits + special

pwd_length = 12

def callback():
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
            ### checks to see if there are (at least) 2 special characters, 
            ### between 2 and 5 digits, more than 5 letters
        if (sum(char in special for char in pwd)<=2 and
            sum(char in digits for char in pwd)>=2 and
            sum(char in digits for char in pwd)<=5 and
            sum(char in letters for char in pwd)>=5):
            break
    ### copies the password to clipboard
    def copy(text):
        main.clipboard_clear()
        main.clipboard_append(text)
    ### add the generated pass to the window and add a 'copy' button
    ttk.Label(frm, text="Your new password is:").grid(column=0, row=2)
    ttk.Label(frm, text=pwd).grid(column=0, row=3)
    ttk.Button(frm, text="copy", command=copy(pwd)).grid(column=0, row=4)

### end function defs
#
### characteristics for the main window
main = Tk()
main.geometry('500x350')
main.title("Password Generator")
frm = ttk.Frame(main, padding=150, width=0)
frm.grid()

### labels
ttk.Label(frm, text="Secure password generator").grid(column=0, row=0)
ttk.Button(frm, text="Generate!", command=callback).grid(column=0, row=1)

main.mainloop()