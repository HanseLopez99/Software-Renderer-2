from gl import Renderer, color
import random

width = 100
height = 100

rend = Renderer(width, height)

# y = mx + b

m = 1
b = int(height / 2)

for x in range(width):
  y= m-x+b
  y = int(y)

  rend.glPoint(x,y)
  
rend.glFinish("output.bmp")
