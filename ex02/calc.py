import tkinter as tk
import tkinter.messagebox as tkm

rireki = 0

def math(siki):                 #計算結果を出力する関数
    global rireki

    entry.delete(0, tk.END)

    #エラー表示
    try:
        entry.insert(tk.END, str(eval(siki)))
        rireki = eval(siki)     #履歴のために結果をを保持
    except NameError:
        entry.insert(tk.END, "エラー 文字列です")
    except ZeroDivisionError:
        entry.insert(tk.END, "エラー 0では割れません")
    except:
        entry.insert(tk.END, "エラー")

def button_click(event):        #キーが押されたときの関数
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}ボタンがクリックされました")

    if (num == "C"):            #表示を消す
        entry.delete(0, tk.END)
    elif (num == "="):
        keisan = entry.get()
        math(keisan)
    elif (num == "履歴"):
        tkm.showinfo("", f"前回の結果{rireki}")
    else:
        entry.insert(tk.END, f"{num}")
        

root = tk.Tk()
root.geometry("300x690")

entry = tk.Entry(root, justify= "right", width=10, font = ("", 30))
entry.grid(row = 0, column = 0, columnspan = 2, rowspan = 2)

r, c = 2, 0

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

#四則演算の符号ボタン
sisoku = ["+", "=", "-", "*", "/"]

for kei in sisoku:
    button = tk.Button(root, text = f"{kei}", width = 4, height = 2, font = ("", 30))
    button.grid(row = r, column = c)
    button.bind("<1>", button_click)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

#四則演算以外のボタン作成
tokusyu = ["C", "履歴"]
tokusyu_row = 0

for toku in tokusyu:
    button = tk.Button(root, text = f"{toku}", width = 4, height = 1, font = ("", 30))
    button.grid(row = tokusyu_row, column = 2)
    button.bind("<1>", button_click)
    tokusyu_row += 1

root.mainloop()