from processing import *

def setup():
  size(400, 400)
  
def draw_circle(x,y,z):
  ellipse(x,y,z,z)

def draw():
  x = random(0,400)
  y = random(0,400)
  draw_circle(x,y,40)

run()
#6901012610133
#Lab03-1