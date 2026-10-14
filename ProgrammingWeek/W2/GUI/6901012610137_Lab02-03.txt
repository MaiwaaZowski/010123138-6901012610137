from processing import *
x=0
y=x
i=1
def setup():
    size(400, 400)
def draw():
  global x,y,i
  ellipse(x,y,x,y)
  x=x+i
  y=x
  if(x>=620):
    i=i+1
    x=0
  if(i>=620):
    i=1
run()

# 6901012610137
# Lab02-3