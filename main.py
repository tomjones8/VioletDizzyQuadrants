import tkinter as tk

root = tk.Tk()

root.title("Simple Counter")
root.geometry("250x100")

root.counter = 0


def clicked():
  root.counter += 1
  L["text"] = "Button clicked: " + str(root.counter)


b = tk.Button(root, text="Click Me", command=clicked)
b.pack()

L = tk.Label(root, text="No clicks yet.")
L.pack()

root.mainloop()

#name = input('What is your name, sonny?\n')
#print('Hi, %s.' % name)
