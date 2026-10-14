from processing import *
x=0
i=1
def setup():
  size(400, 400)
    
def draw_square(x, y, side, r, g, b):
  fill(r, g, b)
  rect(x, y, side, side)

def draw_positive(x, y, side, r, g, b):
  stroke(0)
  strokeWeight(0.25)
  # Center
  draw_square(x , y, side, r, g, b)
  # Top
  draw_square(x, y - side, side, g, b, r)
  # Bottom
  draw_square(x, y + side, side, b, r, g)
  # Left
  draw_square(x - side, y, side, 90, 200, 180)
  # Right
  draw_square(x + side, y, side, 180, b, 90)
    
def draw():
  global x,i
  draw_positive(x,x,x,255,0,0)
  x=x+i
  if(x>=400):
    x=0
    i=i+1
  if(i>=400):
    i=1

run()
#6901012610133
#Lab03-2