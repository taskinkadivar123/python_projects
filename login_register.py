import tkinter as tk
import mysql.connector
import googletrans
import pyttsx3
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.withdraw()  

engine = pyttsx3.init()

fontAwesome = tkFont.Font(family=r"D:\Python\projects\FontAwesome.ttf", size=16)

root.title("Language Translator")
root.geometry("1080x400")

def create_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sayra@333"
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
    cursor.execute("USE mydatabase")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database and table created successfully.")

def register_user():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if username and email and password and confirm_password:
        if password != confirm_password:
            messagebox.showerror("Registration", "Passwords do not match!")
            return
        
        if "@" not in email or "." not in email:
            messagebox.showerror("Registration", "Invalid email address!")
            return
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sayra@333",  
            database="mydatabase"
        )
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=%s OR email=%s", (username, email))
        existing_user = c.fetchone()
        if existing_user:
            messagebox.showerror("Registration", "Username or email already exists!")
        else:
            c.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
            conn.commit()
            messagebox.showinfo("Registration", "User registered successfully!")
        conn.close()
    else:
        messagebox.showerror("Registration", "Please fill out all fields.")

# def login_user():
#     username = entry_username.get()
#     password = entry_password.get()

#     if username and password:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="sayra@333",
#             database="mydatabase"
#         )
#         c = conn.cursor()
#         c.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
#         user = c.fetchone()

#         if user:
#             messagebox.showinfo("Login", "Login successful!")
#             print("User data from the database:", user)
#             window.destroy()  
#             root.deiconify()  
#         else:
#             messagebox.showerror("Login", "Invalid username or password.")
#         conn.close()
#     else:
#         messagebox.showerror("Login", "Please fill out both fields.")
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sayra@333",
            database="mydatabase"
        )
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = c.fetchone()

        if user:
            messagebox.showinfo("Login", "Login successful!")
            print("User data from the database:", user)

            try:
                window.destroy() 
            except:
                pass  

            root.deiconify()  

        else:
            messagebox.showerror("Login", "Invalid username or password.")
        conn.close()
    else:
        messagebox.showerror("Login", "Please fill out both fields.")


def show_login_page():
    for widget in window.winfo_children():
        widget.destroy()

    frame = tk.Frame(window, bg="#f0f0f0", width=400, height=500, bd=3, relief="solid")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    inner_frame = tk.Frame(frame,  width=380, height=460, bd=5)
    inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = tk.Label(inner_frame, text="Login", font=("Arial", 24),  fg="black")
    label_title.place(relx=0.5, rely=0.1, anchor="center")

    label_username = tk.Label(inner_frame, text="Username", font=("Arial", 12))
    label_username.place(relx=0.5, rely=0.2, anchor="center")

    global entry_username
    entry_username = ttk.Entry(inner_frame, width=30)
    entry_username.place(relx=0.5, rely=0.25, anchor="center")

    label_password = tk.Label(inner_frame, text="Password", font=("Arial", 12))
    label_password.place(relx=0.5, rely=0.32, anchor="center")

    global entry_password
    entry_password = ttk.Entry(inner_frame, show="*", width=30)
    entry_password.place(relx=0.5, rely=0.37, anchor="center")

    login_button = ttk.Button(inner_frame, text="Login", command=login_user, width=15, padding=10)
    login_button.place(relx=0.5, rely=0.5, anchor="center")

    register_button = ttk.Button(inner_frame, text="Register", command=show_register_page, width=15, padding=10)
    register_button.place(relx=0.5, rely=0.6, anchor="center")

def show_register_page():
    for widget in window.winfo_children():
        widget.destroy()

    frame = tk.Frame(window, bg="#f0f0f0", width=400, height=500, bd=3, relief="solid")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    inner_frame = tk.Frame(frame, width=380, height=460, bd=5)
    inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = tk.Label(inner_frame, text="Register", font=("Arial", 24), fg="black")
    label_title.place(relx=0.5, rely=0.1, anchor="center")

    label_username = tk.Label(inner_frame, text="Username", font=("Arial", 12))
    label_username.place(relx=0.5, rely=0.2, anchor="center")

    global entry_username
    entry_username = ttk.Entry(inner_frame, width=30)
    entry_username.place(relx=0.5, rely=0.25, anchor="center")

    label_email = tk.Label(inner_frame, text="Email", font=("Arial", 12))
    label_email.place(relx=0.5, rely=0.32, anchor="center")

    global entry_email
    entry_email = ttk.Entry(inner_frame, width=30)
    entry_email.place(relx=0.5, rely=0.37, anchor="center")

    label_password = tk.Label(inner_frame, text="Password", font=("Arial", 12))
    label_password.place(relx=0.5, rely=0.44, anchor="center")

    global entry_password
    entry_password = ttk.Entry(inner_frame, show="*", width=30)
    entry_password.place(relx=0.5, rely=0.49, anchor="center")

    label_confirm_password = tk.Label(inner_frame, text="Confirm Password", font=("Arial", 12))
    label_confirm_password.place(relx=0.5, rely=0.56, anchor="center")

    global entry_confirm_password
    entry_confirm_password = ttk.Entry(inner_frame, show="*", width=30)
    entry_confirm_password.place(relx=0.5, rely=0.61, anchor="center")

    register_button = ttk.Button(inner_frame, text="Register", command=register_user, width=15, padding=10)
    register_button.place(relx=0.5, rely=0.7, anchor="center")

    login_button = ttk.Button(inner_frame, text="Back to Login", command=show_login_page, width=15, padding=10)
    login_button.place(relx=0.5, rely=0.8, anchor="center")


def speak_text():
    text = text1.get(1.0, END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

def speak_text2():
    text = text2.get(1.0, END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

def translate_now():
    global language
    try:
        text = text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()

        if text:
            translator = googletrans.Translator()
            detected_lang = translator.detect(text).lang
            translated = translator.translate(text, src=detected_lang, dest=c3)
            text2.delete(1.0, END)
            text2.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("googletrans", "Please try again. Error: " + str(e))

def paste_clipboard():
    try:
        clipboard_content = root.clipboard_get()
        text1.insert(END, clipboard_content)
    except Exception as e:
        messagebox.showerror("Error", "Failed to paste clipboard content: " + str(e))

def copy_to_clipboard(text_widget):
    try:
        text_content = text_widget.get(1.0, END).strip()
        root.clipboard_clear()
        root.clipboard_append(text_content)
        messagebox.showinfo("Copied", "Text copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy text: {str(e)}")

# Icon for the window
image_icon = PhotoImage(file="translate.png")
root.iconphoto(False, image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# ComboBox for the language selection
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")
combo1.bind("<<ComboboxSelected>>", lambda event: label1.config(text=combo1.get()))

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

volume_icon1 = tk.Label(root, text="\uf028", font=fontAwesome, fg="black", bg=None, cursor="hand2")
volume_icon1.place(x=20, y=290)
volume_icon1.bind("<Button-1>", lambda event: speak_text())

paste_button = Button(root, text="\uf0ea", font=fontAwesome, activebackground="black", activeforeground="white", cursor="hand2", bg=None, fg="black", command=paste_clipboard)
paste_button.place(x=345, y=280)

copy_button1 = Button(root, text="\uf0c5", font=fontAwesome, activebackground="black", activeforeground="white", cursor="hand2", bg=None, fg="black", command=lambda: copy_to_clipboard(text1))
copy_button1.place(x=390, y=280)

text1 = Text(f, font="Robote 20", bg="White", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Second language combo box
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGES")

label2 = Label(root, text="SELECT LANGUAGES", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)
combo2.bind("<<ComboboxSelected>>", lambda event: label2.config(text=combo2.get()))

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

volume_icon2 = tk.Label(root, text="\uf028", font=fontAwesome, fg="black", bg=None, cursor="hand2")
volume_icon2.place(x=630, y=290)
volume_icon2.bind("<Button-1>", lambda event: speak_text2())

copy_button2 = Button(root, text="\uf0c5", font=fontAwesome, activebackground="black", activeforeground="white", cursor="hand2", bg='lightgrey', fg="black", command=lambda: copy_to_clipboard(text2))
copy_button2.place(x=1000, y=280)

text2 = Text(f1, font="Robote 20", bg="White", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root,text="\uf0ec", width=4,height=2, font=fontAwesome,  activebackground="black", activeforeground="white",cursor="hand2",bd=5,bg="grey",fg="black",command= translate_now)
translate.place(x=500, y=195)

window = Tk()
window.geometry("500x600")
window.title("Login / Register")
window.configure(bg="#f0f0f0")

show_login_page()

root.mainloop()
