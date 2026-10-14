from processing import *

x = 25
y = 25
gap = 50

def setup():
    size(400, 400)

def draw():
    background(255)

    # ---------- LINE ----------
    xpos = x
    top = y

    # L
    line(xpos, top, xpos, top * 3)                   # Left side
    line(xpos, top * 3, xpos + 25, top * 3)          # Bottom

    # I
    xpos = xpos + gap
    line(xpos, top, xpos + 25, top)                  # Top
    line(xpos + 25/2, top, xpos + 25/2, top * 3)     # Middle
    line(xpos, top * 3, xpos + 25, top * 3)          # Bottom

    # N
    xpos = xpos + gap
    line(xpos, top, xpos, top * 3)                   # Left
    line(xpos, top, xpos + 25, top * 3)              # Diagonal
    line(xpos + 25, top, xpos + 25, top * 3)         # Right

    # E
    xpos = xpos + gap
    line(xpos, top, xpos, top * 3)                   # Left
    line(xpos, top, xpos + 25, top)                  # Top
    line(xpos, top * 2, xpos + 20, top * 2)          # Middle
    line(xpos, top * 3, xpos + 25, top * 3)          # Bottom

    # ---------- MAIWAA ----------
    xpos = x
    top = 150
    bottom = top + 50
    middle = top + 25

    # M
    line(xpos, bottom, xpos, top)                    # Left
    line(xpos, top, xpos + 12.5, middle)             # Left diagonal
    line(xpos + 12.5, middle, xpos + 25, top)        # Right diagonal
    line(xpos + 25, top, xpos + 25, bottom)          # Right

    # A
    xpos = xpos + gap
    line(xpos, bottom, xpos + 12.5, top)             # Left diagonal
    line(xpos + 12.5, top, xpos + 25, bottom)        # Right diagonal
    line(xpos + 6, middle, xpos + 19, middle)        # Middle

    # I
    xpos = xpos + gap
    line(xpos, top, xpos + 25, top)                  # Top
    line(xpos + 25/2, top, xpos + 25/2, bottom)      # Middle
    line(xpos, bottom, xpos + 25, bottom)            # Bottom

    # W
    xpos = xpos + gap
    line(xpos, top, xpos + 6, bottom)                # Left
    line(xpos + 6, bottom, xpos + 12.5, middle)      # Left middle
    line(xpos + 12.5, middle, xpos + 19, bottom)     # Right middle
    line(xpos + 19, bottom, xpos + 25, top)          # Right

    # A
    xpos = xpos + gap
    line(xpos, bottom, xpos + 12.5, top)             # Left diagonal
    line(xpos + 12.5, top, xpos + 25, bottom)        # Right diagonal
    line(xpos + 6, middle, xpos + 19, middle)        # Middle

    # A
    xpos = xpos + gap
    line(xpos, bottom, xpos + 12.5, top)             # Left diagonal
    line(xpos + 12.5, top, xpos + 25, bottom)        # Right diagonal
    line(xpos + 6, middle, xpos + 19, middle)        # Middle

run()

#6901012610137
#Lab1 Ex2