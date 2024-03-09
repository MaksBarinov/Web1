import tkinter as tk
from socket import *
import threading
from PIL import ImageTk, Image

Hostname = gethostname()
Host_IP = gethostbyname(Hostname)
print(Host_IP)

def change_image():
    global image_index, label
    image_index = (image_index + 1) % len(images)
    image = images[image_index]
    label.configure(image=image)
    label.image = image

def start_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((Host_IP, 1400))
    s.listen()

    user, addr = s.accept()
    
    while True:
        data = user.recv(1)
        if not data:
            break
        change_image()

def finish():
    main.destroy()

new_thread = threading.Thread(target=start_server)
new_thread.start()

main = tk.Tk()
main.title("slidephoto")
main.geometry("600x600+240+80")
main.resizable(False, False)
img = ImageTk.PhotoImage(Image.open("image/cat1.png"))
label = tk.Label(main, image=img)
label.pack()
images = [ImageTk.PhotoImage(Image.open("image/cat1.png")), ImageTk.PhotoImage(Image.open("image/cat2.png")), ImageTk.PhotoImage(Image.open("image/cat3.png")), ImageTk.PhotoImage(Image.open("image/cat4.png"))]
image_index = 0
main.protocol("WM_DELETE_WINDOW", finish)

main.mainloop()

