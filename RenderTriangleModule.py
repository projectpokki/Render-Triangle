import os
from math import ceil, floor


def renderScreen(screen):
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  for y in screen:
    line = ""
    for pixel in y:
      line += "\033[4" + str(pixel) + "m  "
    print(line)


def createScreen(xSize, ySize):
  screen = []
  for y in range(ySize):
    screen.append([])
    for _x in range(xSize):
      screen[y].append(0)
  return screen


def createTriangle(a, b, c, color, screen):
  xMin = floor(min([a[0], b[0], c[0]]))
  xMax = ceil(max([a[0], b[0], c[0]]))
  yMin = floor(min([a[1], b[1], c[1]]))
  yMax = ceil(max([a[1], b[1], c[1]]))

  if b[0] == a[0]:
    b, c = c, b

  dxb = b[0] - a[0]
  dyb = b[1] - a[1]
  dxc = c[0] - a[0]
  dyc = c[1] - a[1]
  wbDiv = 1 / dxb
  wcDiv = 1 / ((dxc * dyb) - (dyc * dxb))

  for x in range(xMin, xMax + 1):
    for y in range(yMin, yMax + 1):
      wc = (((x - a[0]) * dyb) + ((a[1] - y) * dxb)) * wcDiv
      wb = (x - a[0] - (wc * dxc)) * wbDiv
      if wc < 0 or wb < 0 or wb + wc > 1:
        continue
      screen[y][x] = color
  return screen
