import tkinter 

root=tkinter.Tk()
root.title("Test")

frame=tkinter.Frame(root, width=100, height=100)
frame.pack(fill="both", expand=True)

label=tkinter.Label(frame, text="こんにちは！")
label.pack(padx=100, pady=100)

root.mainloop()