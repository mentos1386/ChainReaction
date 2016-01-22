from Core import *
from time import time

# Naloga 9
balls = []
balls_hit = {}
coordinates = None
balls_remaining = 1

for i in range(0, 30):
    balls.append(Core(random_color()))

mouse = Core(random_color(), 30, True)
mouse.mouse = True

balls.append(mouse)

num_balls_hit = 0
num_balls_removed = 0
first_run = True

# Game runs until there are still blown up balls in game
while first_run or num_balls_hit != num_balls_removed:
    for ball in balls:
        # Check if ball was hit, not removed, and it wasn't all ready processed as hit
        if ball.hit and not ball.removed and not ball.hit_processed:
            # Make ball bigger
            ball.ball.setRect(-30, -30, 60, 60)
            ball.size = 30
            # Change Color
            color = ball.ball.pen().color().lighter()
            color.setAlpha(192)
            ball.ball.setBrush(color)
            # Add ball to balls_hit
            balls_hit[len(balls_hit)+1] = (ball, time())
            ball.hit_processed = True
            # Add number of balls hit +1
            num_balls_hit += 1
        elif ball.hit:
            pass
        else:
            ball.run()
            # Check if we hit mouse
            ball.check_hit_ball(mouse)
            # Check if we hit any other all ready destroyed balls
            for key in balls_hit.keys():
                hit_ball, hit_time = balls_hit[key]
                ball.check_hit_ball(hit_ball)

    # Remove old balls after 4 sec (in order they were created)
    for key in balls_hit.keys():
        hit_ball, hit_time = balls_hit[key]
        # If time difference is greater than 4, remove ball
        if time() - hit_time > 4 and not hit_ball.removed:
            hit_ball.ball.setRect(-0, -0, 0, 0)
            hit_ball.size = 0
            hit_ball.removed = True
            # Add number of balls removed +1
            num_balls_removed += 1

    # When we have added hit balls, we switch mode to counter..
    if num_balls_hit > 0:
        first_run = False

risar.QMessageBox.information(None, "Game Over", "You managed to destroy " + str(num_balls_hit-1) + " circles.")

