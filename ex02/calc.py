import tkinter as tk
import tkinter.messagebox as tkm

def math(siki):                 #計算結果を出力する関数
    entry.delete(0, tk.END)

    #エラー表示
    try:
        entry.insert(tk.END, str(eval(siki)))
    except NameError:
        entry.insert(tk.END, "エラー")

def button_click(event):        #キーが押されたときの関数
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}ボタンがクリックされました")

    if (num == "C"):            #表示を消す
        entry.delete(0, tk.END)
    elif (num != "="):
        entry.insert(tk.END, f"{num}")
    else:
        keisan = entry.get()
        math(keisan)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify= "right", width=10, font = ("", 30))
entry.grid(row = 0, column = 0, columnspan = 2)

r, c = 1, 0

#数字ボタン作成
for num in range(9, -1, -1):

    #数字の場所入れ替え
    if num == 0:
        None
    elif num % 3 == 0:
        num -= 2
    elif num % 3 == 1:
        num += 2

    button = tk.Button(root, text = f"{num}", width = 4, height = 2, font=("", 30))
    button.grid(row = r, column = c)
    button.bind("<1>", button_click)
    c += 1
    if c% 3 == 0:
        r += 1
        c = 0

#+ボタン作成
button = tk.Button(root, text = "+", width = 4, height = 2, font = ("", 30))
button.grid(row = r, column = 1)
button.bind("<1>", button_click)

#=ボタン作成
button = tk.Button(root, text = "=", width = 4, height = 2, font = ("", 30))
button.grid(row = r, column = 2)
button.bind("<1>", button_click)

#clearボタン作成
buttn = tk.Button(root, text = "C", width = 4, height = 1, font = ("", 30))
buttn.grid(row = 0, column = 2)
buttn.bind("<1>", button_click)

root.mainloop()