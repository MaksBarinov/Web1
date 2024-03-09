import tkinter as tk
import socket
from tkinter import ttk

def click():
    client.send(bytes("\00", 'ascii'))

def finish():
    win.destroy()

win = tk.Tk()

#фон
bg_image = tk.PhotoImage(file="bg.png")
bg = ttk.Label(image=bg_image)
bg.place(x=-2, y=0)

#экран
win.title('Button Photo')
win.iconbitmap(default= "1.ico")
win.geometry("600x550+120+80")
win.resizable(False, False)

#кнопка
btn = tk.Button(win, text='push me \U0001F975', font=20, width=15, height=3, command= click)
btn.pack(expand=True)

#текст
text = ttk.Label(text="Нажми на эту кнопку", foreground="black", padding=10, font=("Tahoma", 20))
text.place(x=160, y=150)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.23.13.108", 1400))

win.mainloop()
client.close()