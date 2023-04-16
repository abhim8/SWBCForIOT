import tkinter as tk

def function1():
    print("Function 1 called!")

def function2():
    print("Function 2 called!")

root = tk.Tk()

button1 = tk.Button(root, text="Call Function 1", command=function1)
button1.pack()

button2 = tk.Button(root, text="Call Function 2", command=function2)
button2.pack()

root.mainloop()
