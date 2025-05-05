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

root.mainloop()