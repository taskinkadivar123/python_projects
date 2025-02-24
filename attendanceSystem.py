import speech_recognition as sr
import datetime
import pyttsx3
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar

engine = pyttsx3.init()

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="sayra@333",  
    database="mydatabase"  
)
db_cursor = db_connection.cursor()

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your name...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        name = recognizer.recognize_google(audio)
        print(f"Recognized name: {name}")
        current_time = datetime.datetime.now()
        date = current_time.strftime("%Y-%m-%d")
        time = current_time.strftime("%H:%M:%S")
        engine.say(f"Attendance marked for {name} at {time} on {date}.")
        engine.runAndWait()
        return name
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech service; {e}")
        return None

def mark_attendance():
    student_name = recognize_voice()
    if student_name:
        current_time = datetime.datetime.now()
        date = current_time.strftime("%Y-%m-%d")
        time = current_time.strftime("%H:%M:%S")
        try:
            insert_query = "INSERT INTO attendance (student_name, date, time) VALUES (%s, %s, %s)"
            db_cursor.execute(insert_query, (student_name, date, time))  
            db_connection.commit()
            feedback_label.config(text=f"Attendance marked for {student_name} at {time} on {date}.")
            # engine.say(f"Attendance marked for {student_name} at {time} on {date}.")
            # engine.runAndWait()
            print(f"Attendance marked for: {student_name} on {date} at {time}")
        except mysql.connector.Error as err:
            print(f"Error inserting data into MySQL: {err}")
            feedback_label.config(text="Error marking attendance.")
    else:
        print("No name recognized, attendance not marked.")
        feedback_label.config(text="No name recognized, attendance not marked.")

def generate_report():
    try:
        select_query = "SELECT student_name, date, time FROM attendance"
        db_cursor.execute(select_query)
        records = db_cursor.fetchall()
        
        if records:
            report_text = "Attendance Report:\n"
            report_text = "Name \t \t  Date  \t \t  Time \n "
            for record in records:
                student_name, date, time = record
                report_text += f"{student_name} \t\t {date} \t {time} \n"
            report_label.config(text=report_text)
        else:
            report_label.config(text="No attendance records found.")
    except mysql.connector.Error as err:
        print(f"Error retrieving data from MySQL: {err}")
        report_label.config(text="Error retrieving attendance records.")

root = tk.Tk()
root.title("Voice Attendance System")
root.geometry("600x500")

title_label = tk.Label(root, text="Voice Attendance System", font=("Arial", 20), bg="lightblue", width=30)
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=20)

mark_button = tk.Button(frame, text="Mark Attendance", font=("Arial", 14), command=mark_attendance)
mark_button.grid(row=0, column=0, padx=10)

generate_button = tk.Button(frame, text="Generate Report", font=("Arial", 14), command=generate_report)
generate_button.grid(row=0, column=1, padx=10)

feedback_label = tk.Label(root, text="Real-time feedback will appear here.", font=("Arial", 12), bg="lightgray", width=50, height=2 ,  relief="solid", bd=2,)
feedback_label.pack(pady=10)

report_label = tk.Label(root, text="Attendance report will appear here.", font=("Arial", 12), bg="lightgray", width=50, height=8, anchor="w", relief="solid", bd=2,  padx=5,  pady=5,highlightcolor="grey",highlightbackground="red")
report_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
