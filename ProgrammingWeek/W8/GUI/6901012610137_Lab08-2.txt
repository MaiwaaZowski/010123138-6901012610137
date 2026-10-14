from processing import *

class Balloon:
    def __init__(self, x, y, size, speed, col):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.col = col

    def show(self):
        fill(self.col)
        noStroke()
        ellipse(self.x, self.y, self.size, self.size * 1.2)
        stroke(80)
        line(self.x, self.y + self.size * 0.6, self.x, self.y + self.size * 0.6 + 40)

        self.y -= self.speed
        if self.y < -50:
            self.y = height + 50


balloons = []


def setup():
    size(600, 600)
    global balloons
    balloons = [
        Balloon(100, 550, 60, 1.5, color(255, 80, 80)),
        Balloon(200, 580, 50, 1.2, color(80, 150, 255)),
        Balloon(300, 560, 70, 1.8, color(255, 220, 80)),
        Balloon(400, 590, 55, 1.0, color(120, 220, 120)),
        Balloon(500, 570, 65, 1.4, color(220, 120, 255)),
    ]


def draw():
    background(230, 250, 255)
    for b in balloons:
        b.show()
run()

#6901012610137
#lab8-2