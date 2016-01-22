from math import *
from random import *
from time import *
import risar


def random_color():
    return risar.barve[randint(0, 8)]


class Core:

    def __init__(self, color=risar.bela, size=10, fill=False):
        self.speed = 5
        self.wall = (risar.maxX, risar.maxY)
        self.course_x = randint(-self.speed, self.speed)
        self.course_y = sqrt(self.speed**2-self.course_x**2)
        self.coordinates = (randint(10, self.wall[0] - 5), randint(10, self.wall[1]) - 5)
        self.size = size
        self.color = color
        self.fill = fill
        self.mouse = False
        self.placed = False
        self.hit = False
        self.removed = False
        self.hit_processed = False
        self.ball = self.ball = risar.krog(self.coordinates[0], self.coordinates[1], self.size, self.color, self.fill)

    def hit_wall(self):
        wall_x, wall_y = self.wall
        x, y = self.coordinates

        # Wall X
        if (x+self.size/2 >= wall_x and not(self.course_x < 0)) or (x-self.size/2 <= 0 and not(self.course_x > 0)):
            self.course_x = -self.course_x

        # Wall Y
        if (y+self.size/2 >= wall_y and not(self.course_y < 0)) or (y-self.size/2 <= 0 and not(self.course_y > 0)):
            self.course_y = -self.course_y

    def position(self):
        if self.mouse:
            self.coordinates = risar.miska
        else:
            self.coordinates = (self.coordinates[0] + self.course_x, self.coordinates[1] + self.course_y)
        self.ball.setPos(self.coordinates[0], self.coordinates[1])

    # Check if a mouse was placed, and set placed = true, only for "mouse"
    def check_placed(self):
        if risar.klik and self.mouse:
            self.placed = True

    # Check if we hit other ball
    def check_hit_ball(self, ball):
        x, y = self.coordinates
        ball_x, ball_y = ball.coordinates
        # Calculate if distance between booth centers
        if risar.klik and not ball.removed and sqrt((ball_x - x)**2 + (ball_y - y)**2) <= ball.size+self.size:
            self.hit = True

    def run(self):
        self.check_placed()
        if self.hit or self.placed:
            pass
        else:
            self.hit_wall()
            self.position()
            risar.obnovi()
        sleep(0.002)


