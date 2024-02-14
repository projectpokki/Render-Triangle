# How To Use
There are 3 functions: ```createScreen()```, ```createTriangle()```, and ```renderScreen()```.

```createScreen()``` is used to create a 2d array of empty (black) pixels. There are 2 parameters: the width of the screen (x) and height of the screen (y). It returns a variable, which is the screen it created. It should be used like this:
``` python
import RenderTriangleModule
screenSizeX = 7
screenSizeY = 7
emptyScreen = RenderTriangle(screenSizeX, screenSizeY)
```
This code will not print anything. The variable ```screen``` is for other functions to use. In this screen, [0, 0] is the top left corner of the screen. The positive x direction is right, and the positive y direction is down.

```createTriangle()``` is used to draw a triangle on the screen. There are 5 parameters: three points for the corners of the triangle, the colour of the triangle, and the screen to draw on. It returns a variable, which is the screen after the triangle has been drawn. The points of a triangle do not need to be integers. It should be used like this:
``` python
import RenderTriangleModule
emptyScreen = RenderTriangle(7, 7)

pointA = [1, 1]
pointB = [1, 5]
pointC = [5, 5]
colour = 1
screenWithTriangle = createTriangle(pointA, pointB, pointC, colour, emptyScreen)
```
The function ```createTriangle()``` can be used multiple times, to draw multiple triangles on a screen. the ```colour``` parameter uses enums, where:

- 0 = black
- 1 = red
- 2 = green
- 3 = yellow
- 4 = blue
- 5 = purple
- 6 = cyan
- 7 = white

```renderScreen()``` is used to print the screen on the console. It also clears the console before printing the screen. There is 1 parameter: a variable representing the screen. It should be used like this:
``` python
import RenderTriangleModule
emptyScreen = RenderTriangle(7, 7)
screenWithTriangle = createTriangle([1, 1], [1, 5], [5, 5], 1, emptyScreen)

renderScreen(screenWithTriangle)
```
This module only allows for rendering triangles on a 2d screen. However, triangles can be joined together to create more complex polygons. And using some trigonometry, it is possible to render entire 3d objects. Animations can also be created, because ```renderScreen()``` clears the console before printing.
