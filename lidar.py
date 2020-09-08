#!/usr/bin/env python3

import math
import pprint
import tkinter as tk

HYPOTENUSE = 1000
CURRENT_X = 0.3
CURRENT_Y = 0.3
COLLISIONS = {}
WIDTH = 800
HEIGHT = 800

BOT_RADIUS = 1.5
GOALS = []
# obstacles are in the format (x,y,r)
OBSTACLES = []


def collision(x: float, y: float, goal_x: float, goal_y: float):
    '''
    Detects if object will collide, return point of collision
    Currently does not take into account drone hitbox
    Returns tuple with collison points or None if no collision
    '''
    central_m = slope_calculator(x, y, goal_x, goal_y)
    central_b = b_calculator(x, y, central_m)
    return detect_blocking_circle(x, y, central_m, central_b)


def detect_blocking_circle(x: float, y: float, m: float, b: float):
    ''' Checks against every obstacle to determine if there will be a collison '''
    global OBSTACLES
    for obstacle in OBSTACLES:
        # calculate the y coordinate along the line at x = center of obstacle
        closest_y = m * obstacle[0] + b
        # if that y coordinate is within the radius of the obstacle then return collision point
        if abs(closest_y - obstacle[1]) < obstacle[2]:
            return (obstacle[0], closest_y)
    return None


def slope_calculator(x: float, y: float, goalx: float, goaly: float) -> float:
    ''' Find the slope of the line y = mx + b '''
    return (goaly - y) / (goalx - x)


def b_calculator(x: float, y: float, m: float) -> float:
    ''' calculate b from y = mx + b '''
    return y - m * x


def add_obstacle(x: float, y: float, r: float) -> None:
    """ Add new subgoal """
    global OBSTACLES
    OBSTACLES.insert(0, (x, y, r))


def calculate_goals(theta):
    """
    determines the destination to use to look for a collision
    multiply by HYPOTENUSE = 1000 to account for the fact that the
    canvas is a square
    """
    return HYPOTENUSE * math.sin(math.radians(theta)), HYPOTENUSE * math.cos(math.radians(theta))


def orientation_iterator():
    global COLLISIONS
    """
    iterates through degrees 0-360 and finds collisions with objects
    """
    for degree in range(0, 360, 3):
        goal_x, goal_y = calculate_goals(degree)
        print("goal x: ", goal_x, " goal_y: ", goal_y)
        if collision(CURRENT_X, CURRENT_Y, goal_x, goal_y):
            COLLISIONS[degree] = collision(CURRENT_X, CURRENT_Y, goal_x, goal_y)


def collision_plotter(canvas):
    global COLLISIONS
    """
    iterates through all the collisions in the dictionary and plots them on the page
    """
    radius = 10
    for key in COLLISIONS.keys():
        collision_x, collision_y = COLLISIONS[key]
        canvas.create_rectangle(collision_x - radius * 0.5, collision_y + radius * 0.5, collision_x + 0.5 * radius,
                                collision_y - 0.5 * radius, fill="red")


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    add_obstacle(1, 1, 1)
    orientation_iterator()
    collision_plotter(canvas)
    pprint.pprint(COLLISIONS)
    root.mainloop()
