import tkinter as tk

root = tk.Tk()

WIDTH=800
HEIGHT=800
D1 = 20
D2 = 30
D3 = 40

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

text = canvas.create_text(400, 10, text="Keys to move = a,d,w,s")

# Placing obstacles on the canvas
x1 = 680
y1 = 680
oval1 = canvas.create_oval(x1, y1, x1 + D1, y1 + D1, fill="yellow")
x2 = 620
y2 = 660
oval2 = canvas.create_oval(x2, y2, x2 + D1, y2 + D1, fill="yellow")
x3 = 450
y3 = 500
oval3 = canvas.create_oval(x3, y3, x3 + D2, y3 + D2, fill="yellow")
x4 = 600
y4 = 250
oval4 = canvas.create_oval(x4, y4, x4 + D2, y4 + D2, fill="yellow")
x5 = 705
y5 = 320
oval5 = canvas.create_oval(x5, y5, x5 + D3, y5 + D3, fill="yellow")

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


