from Core import *
from time import *

# Naloga 7
start_time = time()
balls = []
for i in range(0, 30):
    balls.append(Core(random_color()))
while time() < start_time+20:
    for ball in balls:
        ball.run()
