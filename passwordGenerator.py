from tkinter import *
import pyperclip, random

root = Tk()
root.geometry("500x500") 
root.title("Password Generator")

passstr = StringVar()
passlen = IntVar()
passlen.set(8) 

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    password = ""

    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    passstr.set(password)

# Function to copy password to clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
    with open("generated_password.txt", "w") as file:
        file.write(f"Generated Password: {random_password}\n")
    print("Password saved to 'generated_password.txt'")
    
frame = Frame(root, bd=3, relief="solid", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=370)    

Label(frame, text="Password Generator", font="calibri 20 bold").place(relx=0.5, rely=0.1, anchor="center")

Label(frame, text="Enter Password Length:", font="calibri 12").place(relx=0.5, rely=0.22, anchor="center")
Entry(frame, textvariable=passlen, font="calibri 12", width=10).place(relx=0.5, rely=0.33, anchor="center")

Button(frame, text="Generate Password", font="calibri 12 bold", command=generate, bg="#4CAF50", fg="white").place(relx=0.5, rely=0.45, anchor="center", width=150, height=35)

Entry(frame, textvariable=passstr, font="calibri 12", width=25, bd=2).place(relx=0.5, rely=0.6, anchor="center")

Button(frame, text="Copy to Clipboard", font="calibri 12", command=copytoclipboard, bg="#2196F3", fg="white").place(relx=0.5, rely=0.73, anchor="center", width=150, height=35)

root.mainloop()
