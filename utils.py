import tkinter as tk
from tkinter import messagebox
#from PIL import Image, ImageTk


def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
        window,
        text=text,
        activebackground="black",
        activeforeground="white",
        fg=fg,
        bg=color,
        command=command,
        height=2,
        width=20,
        font=('Helvetica', 20, 'bold')
    )
    
    return button

