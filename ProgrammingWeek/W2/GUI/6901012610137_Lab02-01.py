from processing import *
x = 10
y = 0
def setup():
  size(400,400)
def draw_balloon(x, y):
  ellipse(x, y, 100, 100)
  line(x, y+50, x, y+200)
def draw(): # will be called repeatedly
  global x
  draw_balloon(x, mouseY) # built-in
  x = x + 10
  if x > width:
    x = 10
run()

# 6901012610137
# Lab02-1