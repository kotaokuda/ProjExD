import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up" and maze_list[mx][my - 1] == 0:      #上が入力されかつ、移動先が道なら
        my -= 1
    if key == "Down" and maze_list[mx][my + 1] == 0:        #下が入力されかつ、移動先が道なら
        my += 1
    if key == "Left" and maze_list[mx - 1][my] == 0:        #左が入力されかつ、移動先が道なら
        mx -= 1
    if key == "Right" and maze_list[mx + 1][my] == 0:       #右が入力され、移動先が道なら
        mx += 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.coords("kokaton", cx, cy)
    root.after(300, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    maze_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze_list)    

    key = ""

    kokaton = tk.PhotoImage(file = "fig/0.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.create_image(cx, cy, image = kokaton, tag = "kokaton")

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()