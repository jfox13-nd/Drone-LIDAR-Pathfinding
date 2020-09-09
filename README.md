# Drone-LIDAR-Pathfinding



## Sources
https://fei.edu.br/rcs/2014/RegularPapers/robocupsymposium2014_submission_55.pdf

##Running Instructions
`pip install -r requirements.txt`

##Write-up
Jack Fox, Jack Morgan, Sean Crotty <br>
CSE 40773: Software Development for Unmanned Aerial Systems <br>
Prof. Cleland-Huang <br>
8 September 2020 <br>
LIDAR Lab Project Document<br><br>
	For this assignment, we created a LIDAR system for our robot, as well as a GUI to visualize it performing the necessary calculations.  Our LIDAR Algorithm works as follows: it first performs a 360 degree scan of its environment from its starting point, and prints out in the GUI all of the collisions that it records.  We used an open source collision detection library called shapely to perform the necessary math to determine the point of intersection between the bot and the obstacle.  In order to determine the point of intersection between the bot and any given obstacle, we need two points to form the path of travel: a starting point and an endpoint.  The start point that is given is the current x and current y of the bot, and the endpoint is calculated as (1000*cos(Θ), 1000*sin(Θ)).  We put the 1000 as the value of the “radius” in this case to account for the fact that we are using a circle to scan a square, and thus we need the bounds of our circle to always exceed the bounds of the square to ensure that we pickup and register all the obstacles on the canvas.  After determining the locations of various collisions, our algorithm travels to the collision that is nearest to our goal destination, and at each step of travel, re-reruns the lidar function to determine where any new collisions might appear.  Once it reaches the location of the collision, LIDAR is re-run and our new goal is calculated in the same way that the old goal was. We run this algorithm until it reaches the goal.  We did not detect any edge cases, although we did have trouble resetting the canvas upon each movement of the bot so that it only reflected the collisions at that step.  Currently, the canvas doesn’t reset so all collisions that occur at each step are simply stacked on top of one another.  We also do not take into account the radius of the bot, we are still treating it as a singular point.  There are no other known edge cases at this time.
