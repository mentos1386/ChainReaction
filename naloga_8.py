from Core import *
from time import *

# Naloga 8
start_time = time()
balls = []
coordinates = None

for i in range(0, 30):
    balls.append(Core(random_color()))

mouse = Core(random_color(), 30, True)
mouse.mouse = True

balls.append(mouse)

hit = False

while not hit:
    for ball in balls:
        if ball.hit and not ball.mouse:
            hit = True
        ball.run()
        ball.check_hit_ball(mouse)

