from processing import *

def setup():
    size(400, 400)
    noStroke()

def draw():
    background(76, 175, 80)   # Creeper green

    fill(0)                   # Black face

    # Eyes
    rect(80, 80, 80, 80)      # Left eye
    rect(240, 80, 80, 80)     # Right eye

    # Nose
    rect(160, 160, 80, 80)

    # Mouth
    rect(120, 200, 160, 80)   # Top of mouth
    rect(120, 280, 40, 40)    # Left leg
    rect(240, 280, 40, 40)    # Right leg

run()

#6901012610137
#Lab1 Ex3