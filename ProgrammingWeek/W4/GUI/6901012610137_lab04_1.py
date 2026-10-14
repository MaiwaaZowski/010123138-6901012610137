from processing import *

def setup():
    size(600, 400)

def draw():
    background(255)
    draw_rain_drops(100)
    fill(0)

def draw_rain_drops(n):
    i = 0
    while i < n:
        rx = random(50, 550)
        ry = random(50, 350)
        r = random(3, 30)
        fill(0, 120, 255)
        noStroke()
        ellipse(rx, ry, r, r)
        i = i + 1

run()

#6901012610137
#lab4-1