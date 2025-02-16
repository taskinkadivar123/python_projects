from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import pyttsx3
import tkinter.font as tkFont
import tkinter as tk


root = Tk()
root.title("Language Translator")
root.geometry("1080x400")

fontAwesome = tkFont.Font(family=r"D:\Python\projects\FontAwesome.ttf", size=16)

engine = pyttsx3.init()

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)
    
def speak_text():
    text_ = text1.get(1.0, END) 
    if text_:
        engine.say(text_)  
        engine.runAndWait()    
        
def speak_text2():
    text_ = text2.get(1.0, END).strip()  
    if text_:
        engine.say(text_)  
        engine.runAndWait()

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()

        if text_:
            translator = googletrans.Translator()
            detected_lang = translator.detect(text_).lang  
            translated = translator.translate(text_, src=detected_lang, dest=c3)
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
        



image_icon = PhotoImage(file="translate.png")
root.iconphoto(False,image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1 = Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

volume_icon1 = tk.Label(root, text="\uf028", font=fontAwesome, fg="black", bg=None, cursor="hand2")
volume_icon1.place(x=20, y=290)
volume_icon1.bind("<Button-1>", lambda event: speak_text())

paste_button = Button(root, text="\uf0ea", font=fontAwesome, activebackground="black", activeforeground="white", cursor="hand2", bg=None, fg="black", command=paste_clipboard)
paste_button.place(x=345, y=280)  

copy_button1 = Button(root, text="\uf0c5", font=fontAwesome, activebackground="black", activeforeground="white", cursor="hand2", bg=None, fg="black", command=lambda: copy_to_clipboard(text1))
copy_button1.place(x=390, y=280)

text1 = Text(f,font="Robote 20",bg="White",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



combo2 = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGES")

label2 = Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

volume_icon2 = tk.Label(root, text="\uf028", font=fontAwesome, fg="black", bg=None, cursor="hand2")
volume_icon2.place(x=630, y=290)
volume_icon2.bind("<Button-1>", lambda event: speak_text2())

copy_button2 = Button(root, text="\uf0c5", font=fontAwesome, activebackground="black", activeforeground="white", cursor="hand2", bg='lightgrey', fg="black", command=lambda: copy_to_clipboard(text2))
copy_button2.place(x=1000, y=280)

text2 = Text(f1,font="Robote 20",bg="White",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)



translate = Button(root,text="\uf0ec", width=4,height=2, font=fontAwesome,  activebackground="black", activeforeground="white",cursor="hand2",bd=5,bg="grey",fg="black",command= translate_now)
translate.place(x=500, y=195)

label_change()

root.configure(bg="white")
root.mainloop()


