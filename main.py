# flashcard app using python and tkinter
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import Style

# create a database connection
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flashcards (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   name TEXT NOT NULL
                   )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    setId INTEGER NOT NULL,
                    topic TEXT NOT NULL, 
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    flashcard_id INTEGER NOT NULL,
                    FOREIGN KEY (setId) REFERENCES flashcards (id)
                    )''')

# add new flashcard to the database
def add_flashcard_set(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO flashcards (name) VALUES (?)', (name,))
        setId = cursor.lastrowid
        conn.commit()
        messagebox.showinfo('Success', 'Flashcard set added successfully')
    except Exception as e:
        messagebox.showerror('Error', str(e))
    finally:
        return setId


if __name__ == '__main__':
    # window setup
    root = tk.Tk()
    root.title('Flashcard App')
    root.geometry('500x400')

    # style setup
    style = Style('darkly')
    style.configure('TButton', font=('Arial', 16))

    # input fields
    topic = tk.StringVar()
    question = tk.StringVar()
    answer = tk.StringVar()

    # notebook widget to manage tabs
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # tab 1
    frame1 = ttk.Frame(notebook)
    notebook.add(frame1, text='Add Flashcard')

    # entry fields
    ttk.Label(frame1, text='Topic:').pack(pady=5, padx=5)
    ttk.Entry(frame1, textvariable=topic, width=30).pack(pady=5, padx=5)

    ttk.Label(frame1, text='Question:').pack(pady=5, padx=5)
    ttk.Entry(frame1, textvariable=question, width=30).pack(pady=5, padx=5)

    ttk.Label(frame1, text='Answer:').pack(pady=5, padx=5)
    ttk.Entry(frame1, textvariable=answer, width=30).pack(pady=5, padx=5)
    
    # add question button
    ttk.Button(frame1, text='Add question').pack(pady=5, padx=5)

    # save set button
    ttk.Button(frame1, text='Save set').pack(pady=5, padx=5)

    # tab 2
    frame2 = ttk.Frame(notebook)
    notebook.add(frame2, text='View Flashcards')

    # combobox widget
    ttk.Combobox(frame2, state='readonly').pack(pady=5, padx=5)

    # select set button
    ttk.Button(frame2, text='Select set').pack(pady=5, padx=5)

    # delete set button
    ttk.Button(frame2, text='Delete set').pack(pady=5, padx=5)

    # tab 3
    frame3 = ttk.Frame(notebook)
    notebook.add(frame3, text='Learn mode')

    # initialize variables for tracking the question on flashcards
    cardIndex = 0
    currentTabs = []

    # label to display question
    questionLabel = ttk.Label(frame3, text='', font=('Arial', 24))
    questionLabel.pack(pady=5, padx=5)

    # label to display answer
    answerLabel = ttk.Label(frame3, text='', font=('Arial', 24))
    answerLabel.pack(pady=5, padx=5)

    # flip button
    ttk.Button(frame3, text='Flip').pack(pady=5, padx=5, side='left')

    # previous flashcard button
    ttk.Button(frame3, text='Previous').pack(pady=5, padx=5, side='right')

    # next flashcard button
    ttk.Button(frame3, text='Next').pack(pady=5, padx=5, side='right')

    root.mainloop()
