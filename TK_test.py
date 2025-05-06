from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Test")

frame=ttk.Frame(root, padding=100)
frame.pack(fill="both", expand=True)

apple_image = PhotoImage(file="apple.png")
label = ttk.Label(frame, image=apple_image)
label.pack(padx=10, pady=10)

label2=ttk.Label(frame, text="これはリンゴです", foreground="black")
label2.pack(padx=10, pady=10)

def on_button_click():
    greet.set("apple")
button1=ttk.Button(frame, text="そうだね", command=on_button_click)
button1.pack(padx=10, pady=10)

greet=StringVar()
greet.set("banana")
label3 = ttk.Label(frame, textvariable=greet, foreground="blue", background="white")
label3.pack(padx=10, pady=10)

root.mainloop()