# flashcard app using python and tkinter
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import Style

if __name__ == '__main__':
    # create a connection to the database
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()

    # create a table
    c.execute('''CREATE TABLE IF NOT EXISTS flashcards
                 (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

    # create a tkinter window
    root = tk.Tk()
    root.title('Flashcard App')
    root.geometry('400x400')
    style = Style('cyborg')
    style.configure('TButton', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TLabel', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TEntry', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TFrame', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TNotebook', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TNotebook.Tab', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TCombobox', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TCheckbutton', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('TRadiobutton', padding=6, relief='flat', background='#343a40', foreground='white')
    style.configure('Vertical.TScrollbar', padding=6, relief='flat', background='#343a40', foreground='white')

    # create a notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # create a frame for the flashcards
    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text='Flashcards')

    # create a frame for the add flashcard form
    add_flashcard_frame = ttk.Frame(notebook)
    notebook.add(add_flashcard_frame, text='Add Flashcard')

    # create a frame for the delete flashcard form
    delete_flashcard_frame = ttk.Frame(notebook)
    notebook.add(delete_flashcard_frame, text='Delete Flashcard')

    # create a label for the question
    question_label = ttk.Label
    question_label = ttk.Label(flashcards_frame, text='Question')
    question_label.pack(pady=10)
    root.mainloop()