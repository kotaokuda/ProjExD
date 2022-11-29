import tkinter as tk
import tkinter.messagebox as tkm

def math(siki):
    entry.delete(0, tk.END)
    if(type(eval(siki)) is int):
        entry.insert(tk.END, str(eval(siki)))
    else:
        entry.insert(tk.END, "エラー")

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}ボタンがクリックされました")

    if (num != "="):
        entry.insert(tk.END, f"{num}")
    else:
        keisan = entry.get()
        math(keisan)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify= "right", width=10, font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

r, c = 1, 0

for num in range(9, -1, -1):
    button = tk.Button(root, text = f"{num}", width = 4, height = 2, font=("", 30))
    button.grid(row = r, column = c)
    button.bind("<1>", button_click)
    c += 1
    if c% 3 == 0:
        r += 1
        c = 0

button = tk.Button(root, text = "+", width = 4, height = 2, font = ("", 30))
button.grid(row = r, column = 1)
button.bind("<1>", button_click)
button = tk.Button(root, text = "=", width = 4, height = 2, font = ("", 30))
button.grid(row = r, column = 2)
button.bind("<1>", button_click)

root.mainloop()