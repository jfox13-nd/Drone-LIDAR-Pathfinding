'''
pathfinding.py
Tools for the pathfinding algorithim
'''
import math

BOT_RADIUS = 1.5
GOALS = []
# obstacles are in the format (x,y,r)
OBSTACLES = []


def add_goal(x: float,y: float) -> None:
    ''' Add new subgoal '''
    GOALS.insert(0,(x,y))

def pathfinding_complete() -> None:
    ''' returns True if pathfinding complete '''
    if GOALS:
        return False
    else:
        return True
    
def find_subgoal(x: float, y: float):
    ''' determines if a subgoal is needed, adds subgoal as necessary '''
    if not GOALS:
        return
    goalx = GOALS[0][0]
    goaly = GOALS[0][1]

    collision_point = collision(x,y,goalx,goaly)
    # return if no need for subgoal, path is clear
    if not collision_point:
        return

    increment = BOT_RADIUS
    while increment < 20 * BOT_RADIUS:
        # find m and b again for y = mx + b
        m = slope_calculator(x,y,collision_point[0],collision_point[1])
        b = b_calculator(x,y,m)
        b_max = b + increment
        b_min = b - increment
        b_max_subgoal = detect_blocking_circle(x,y,m,b_max)
        b_min_subgoal = detect_blocking_circle(x,y,m,b_min)

        # if a valid subgoal is found at it to goals
        if not b_max_subgoal:
            add_goal(collision_point[0], collision_point[1] + increment)
            return
        if not b_min_subgoal:
            add_goal(collision_point[0], collision_point[1] - increment)
            return
        increment += BOT_RADIUS


    print("FAILED TO FIND PATH")
    GOALS = []
    return

def detect_blocking_circle(x:float, y: float, m: float, b: float):
    ''' Checks against every obstacle to determine if there will be a collison '''
    for obstacle in OBSTACLES:
        # calculate the y coordinate along the line at x = center of obstacle
        closest_y = m * obstacle[0] + b
        # if that y coordinate is within the radius of the obstacle then return collision point
        if abs(closest_y - obstacle[1]) < obstacle[2]:
            return (obstacle[0],closest_y)
    return None
        
def distance_between_points(x1: float,y1: float,x2: float,y2: float) -> float:
    ''' Returns distance between two points '''
    return math.sqrt( (x1-x2) ** 2 + (y1-y2) ** 2)

def slope_calculator(x: float, y: float, goalx: float, goaly: float) -> float:
    ''' Find the slope of the line y = mx + b '''
    return (goaly - y) / (goalx - x)

def b_calculator(x: float, y: float, m: float) -> float:
    ''' calculate b from y = mx + b '''
    return y - m * x

def collision(x: float, y: float, goalx: float, goaly: float):
    ''' 
    Detects if object will collide, return point of collision 
    Currently does not take into account drone hitbox
    Returns tuple with collison points or None if no collision
    '''
    central_m = slope_calculator(x,y,goalx,goaly)
    central_b = b_calculator(x,y,central_m)
    return detect_blocking_circle(x,y,central_m,central_b)