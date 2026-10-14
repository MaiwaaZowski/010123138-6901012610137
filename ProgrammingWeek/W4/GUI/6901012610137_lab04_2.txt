from processing import *

def setup():
    size(750, 220)


def draw():
    background(200)

    x = 90
    spacing = 140
    i = 0
    while i < 5:
        draw_positive(x, height / 2, 80)
        x = x + spacing
        i = i + 1


def draw_positive(x, y, s):

    fill(255)
    stroke(0)
    rectMode(CENTER)
    rect(x, y, s, s / 3)
    rect(x, y, s / 3, s)
    rect(x, y, s / 3, s / 3)

run()

#6901012610137
#lab4-2