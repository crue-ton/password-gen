import tkinter as tk
import pyperclip as p
from secrets import choice

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|[]:;<>?,./"

window = tk.Tk()
window.title('Password Generator')
canvas = tk.Canvas(window, width=400, height=300, highlightthickness=0, bg='#262626')

canvas.pack()

input = tk.Entry(window)
canvas.create_window(200, 140, window=input)

def genpass():
    
    length = int(input.get())
    global password 
    password = "".join(choice(chars) for _ in range(length))
    label = tk.Label(window, text=password)
    canvas.create_window(200, 230, window=label)

def copy():
    p.copy(password)

button1 = tk.Button(fg='#ffffff', bg='#735555', text='Generate Password', command=genpass)
canvas.create_window(200, 180, window=button1)

button2 = tk.Button(fg='#ffffff', bg='#735555', text='Copy to Clipboard', command=copy)
canvas.create_window(200, 205, window=button2)

window['bg']='#262626'
window.mainloop()
