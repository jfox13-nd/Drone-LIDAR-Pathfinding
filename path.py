#!/usr/bin/env python3
import tkinter as tk

root = tk.Tk()

WIDTH=800
HEIGHT=800
R1 = 10
R2 = 15
R3 = 20

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

text = canvas.create_text(400, 10, text="Keys to move = a,d,w,s")

# Placing obstacles on the canvas
# Oval 1 radius of 10 
x1 = 680
y1 = 680
oval1 = canvas.create_oval(x1 - R1, y1 - R1, x1 + R1, y1 + R1, fill="yellow")
# Oval 2 radius of 10
x2 = 620
y2 = 660
oval2 = canvas.create_oval(x2 - R1, y2 - R1, x2 + R1, y2 + R1, fill="yellow")
# Oval 3 radius of 15
x3 = 450
y3 = 500
oval3 = canvas.create_oval(x3 - R2, y3 - R2, x3 + R2, y3 + R2, fill="yellow")
# Oval 4 radius of 15
x4 = 600
y4 = 250
oval4 = canvas.create_oval(x4 - R2, y4 - R2, x4 + R2, y4 + R2, fill="yellow")
# Oval 5 radius of 20
x5 = 705
y5 = 320
oval5 = canvas.create_oval(x5- R3, y5 - R3, x5 + R3, y5 + R3, fill="yellow")

# Placing the bot on the canvas
bot_x = 400
bot_y = 790
bot = canvas.create_oval(bot_x, bot_y, bot_x + 3, bot_y + 3, fill="red")

# Placing the goal on the canvas
goal_x = 700
goal_y = 100
goal = canvas.create_rectangle(goal_x, goal_y, goal_x + 5, goal_y + 5, fill="green")

def move(event):
    global x1, y1
    if event.char == "a":
        canvas.move(bot, -5, 0)
    elif event.char == "d":
        canvas.move(bot, 5, 0)
    elif event.char == "w":
        canvas.move(bot, 0, -5)
    elif event.char == "s":
        canvas.move(bot, 0, 5)

root.bind("<Key>", move)
root.mainloop()


