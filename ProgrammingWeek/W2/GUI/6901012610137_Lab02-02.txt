from processing import *

x = 25
gap = 50

# ---------- LINE ----------
def L(x, y):
    line(x, y, x, y + 50)
    line(x, y + 50, x + 25, y + 50)

def I(x, y):
    line(x, y, x + 25, y)
    line(x + 12.5, y, x + 12.5, y + 50)
    line(x, y + 50, x + 25, y + 50)

def N(x, y):
    line(x, y, x, y + 50)
    line(x, y, x + 25, y + 50)
    line(x + 25, y, x + 25, y + 50)

def E(x, y):
    line(x, y, x, y + 50)
    line(x, y, x + 25, y)
    line(x, y + 25, x + 20, y + 25)
    line(x, y + 50, x + 25, y + 50)

# ---------- MAIWAA ----------
def M(x, y):
    line(x, y + 50, x, y)
    line(x, y, x + 12.5, y + 25)
    line(x + 12.5, y + 25, x + 25, y)
    line(x + 25, y, x + 25, y + 50)

def A(x, y):
    line(x, y + 50, x + 12.5, y)
    line(x + 12.5, y, x + 25, y + 50)
    line(x + 6, y + 25, x + 19, y + 25)

def W(x, y):
    line(x, y, x + 6, y + 50)
    line(x + 6, y + 50, x + 12.5, y + 25)
    line(x + 12.5, y + 25, x + 19, y + 50)
    line(x + 19, y + 50, x + 25, y)

def setup():
    size(400, 400)

def draw():
    background(255)

    # ---------- LINE ----------
    xpos = x
    top = 25

    L(xpos, top)
    xpos += gap

    I(xpos, top)
    xpos += gap

    N(xpos, top)
    xpos += gap

    E(xpos, top)

    # ---------- MAIWAA ----------
    xpos = x
    top = 150

    M(xpos, top)
    xpos += gap

    A(xpos, top)
    xpos += gap

    I(xpos, top)
    xpos += gap

    W(xpos, top)
    xpos += gap

    A(xpos, top)
    xpos += gap

    A(xpos, top)

run()

# 6901012610137
# Lab02-2