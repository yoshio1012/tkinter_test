import tkinter as tk

root=tk.Tk()
root.title("Test")

frame= tk.Frame(root, width=100, height=100)
frame.pack(fill="both", expand=True)

apple_image = tk.PhotoImage(file="apple.png")
label = tk.Label(frame, image=apple_image)
label.pack(padx=10, pady=10)

label=tk.Label(frame, text="これはリンゴです")
label.pack(padx=10, pady=10)

label2=tk.Label(frame, text="これはリンゴです", foreground="black")
label2.pack(padx=10, pady=10)

def on_button_click():
    greet.set("apple")
button1=tk.Button(frame, text="そうだね", command=on_button_click)
button1.pack(padx=10, pady=10)

greet=tk.StringVar()
greet.set("banana")
label3 = tk.Label(frame, textvariable=greet, foreground="blue", background="white")
label3.pack(padx=10, pady=10)

root.mainloop()