
from pathfinding import *

if __name__ == '__main__':
    add_goal(5,5)
    add_obstacle(2,2,1)

    print(find_subgoal(0,0))
    print(GOALS)