from processing import *
X, Y, SIZE, SPEED, R, G, B = range(7)

balloons = []


def setup():
    size(600, 600)
    global balloons
    balloons = [
        [100, 550, 60, 1.5, 255,  80,  80],
        [200, 580, 50, 1.2,  80, 150, 255],
        [300, 560, 70, 1.8, 255, 220,  80],
        [400, 590, 55, 1.0, 120, 220, 120],
        [500, 570, 65, 1.4, 220, 120, 255],
    ]


def draw_balloon(b):
    fill(b[R], b[G], b[B])
    noStroke()
    ellipse(b[X], b[Y], b[SIZE], b[SIZE] * 1.2)
    stroke(80)
    line(b[X], b[Y] + b[SIZE] * 0.6, b[X], b[Y] + b[SIZE] * 0.6 + 40)


def draw():
    background(230, 250, 255)
    for b in balloons:
        draw_balloon(b)
        b[Y] -= b[SPEED]
        if b[Y] < -50:
            b[Y] = height + 50
            
run()
#6901012610137
#lab8-1