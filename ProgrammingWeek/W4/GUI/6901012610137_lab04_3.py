from processing import *

x = 0
i = 1

def setup():
  size(400, 400)

def draw_square(x, y, side, r, g, b):
  fill(r, g, b)
  rect(x, y, side, side)

def draw_positive(x, y, side, r, g, b):
  stroke(0)
  strokeWeight(0.25)
  rectMode(CENTER)
  draw_square(x - side, y - side, side, r, g, b)
  draw_square(x - side, y - side - side, side, g, b, r)
  draw_square(x - side, y, side, b, r, g)
  draw_square(x - side - side, y - side, side, 90, 200, 180)
  draw_square(x, y - side, side, 180, b, 90)

def draw():
  global x, i

  # ===== ส่วนที่เพิ่ม: while loop วาดหลายขนาดในเฟรมเดียว =====
  s = 10                # initialise
  while s <= x:           # condition: วนจนถึงขนาดปัจจุบัน
    draw_positive(mouseX + x, mouseY + x, s, 255, 0, 0)
    s = s + 20              # update
  # ============================================

  x = x + i
  if x >= 400:
    x = 0
    i = i + 1
  if i >= 400:
    i = 1

run()
#6901012610137
#lab4-3