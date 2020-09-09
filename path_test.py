#!/usr/bin/env python3
import tkinter as tk
from lidar import *
import time

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
oval1 = canvas.create_oval(x1-D1/2, y1-D1/2, x1 + D1/2, y1 + D1/2, fill="yellow")
x2 = 620
y2 = 660
oval2 = canvas.create_oval(x2-D1/2, y2-D1/2, x2 + D1/2, y2 + D1/2, fill="yellow")
x3 = 450
y3 = 500
oval3 = canvas.create_oval(x3-D2/2, y3-D2/2, x3 + D2/2, y3 + D2/2, fill="yellow")
x4 = 600
y4 = 250
oval4 = canvas.create_oval(x4-D2/2, y4-D2/2, x4 + D2/2, y4 + D2/2, fill="yellow")
x5 = 705
y5 = 320
oval5 = canvas.create_oval(x5-D3/2, y5-D3/2, x5 + D3/2, y5 + D3/2, fill="yellow")

add_obstacle(680,680,D1/2)
add_obstacle(620,660,D1/2)
add_obstacle(450,500,D2/2)
add_obstacle(600,250,D2/2)
add_obstacle(705,320,D3/2)

# Placing the bot on the canvas
bot_x = 400
bot_y = 790
bot = canvas.create_oval(bot_x, bot_y, bot_x + 3, bot_y + 3, fill="red")

# Placing the goal on the canvas
goal_x = 700
goal_y = 100
goal = canvas.create_rectangle(goal_x, goal_y, goal_x + 5, goal_y + 5, fill="green")

add_goal(goal_x,goal_y)
'''
orientation_iterator()
for p in COLLISIONS:
    x_collide = COLLISIONS[p][0]
    y_collide = COLLISIONS[p][1]

    canvas.create_rectangle(x_collide-5,y_collide-5,x_collide+5,y_collide+5,fill="red")

canvas.pack()
'''

def lidar_scan():
    orientation_iterator(CURRENT_X,CURRENT_Y)
    for p in COLLISIONS:
        x_collide = COLLISIONS[p][0]
        y_collide = COLLISIONS[p][1]

        canvas.create_rectangle(x_collide,y_collide,x_collide,y_collide,fill="red")
        #print("seen")
    canvas.pack()
    #print("HELLO")
    

#print("SEE ME")
#print(COLLISIONS)
lidar_scan()

def moveto(x,y):
    global CURRENT_X
    global CURRENT_Y
    ydif = y - CURRENT_Y
    xdif = x - CURRENT_X
    magnitude = math.sqrt( ydif ** 2 + xdif ** 2)
    ydif /= magnitude
    xdif /= magnitude
    xdif *= 5
    ydif *= 5
    canvas.move(bot, xdif, ydif)
    CURRENT_X += xdif
    CURRENT_Y += ydif
    lidar_scan()
    canvas.update()

def move2():
    global CURRENT_X
    global CURRENT_Y
    global x1, y1
    lidar_scan()

def move(event):
    global CURRENT_X
    global CURRENT_Y
    global x1, y1
    if event.char == "a":
        canvas.move(bot, -5, 0)
        CURRENT_X -= 5
    elif event.char == "d":
        canvas.move(bot, 5, 0)
        CURRENT_X += 5
    elif event.char == "w":
        canvas.move(bot, 0, -5)
        CURRENT_Y -= 5
    elif event.char == "s":
        canvas.move(bot, 0, 5)
        CURRENT_Y += 5
    #print(CURRENT_X,CURRENT_Y)
    lidar_scan()

while True:
    moveto(goal_x,goal_y)
    time.sleep(0.01)


'''
for i in range(100):
    canvas.move(bot, 0, -5)
    CURRENT_Y -= 5
    canvas.update()
    time.sleep(0.01)
    lidar_scan()
'''



root.bind("<Key>", move)
root.mainloop()



