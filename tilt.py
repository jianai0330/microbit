# Author: J. Raphael
# Version: 1.0

from microbit import *

def main():

    alpha = 50

    while True:

        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()
        print("x, y, z:", x, y, z)

        if pos(x, alpha) == -1 and pos(y, alpha) == 0:
            display.show(Image.ARROW_W)
        elif pos(x, alpha) == 1 and pos(y, alpha) == 0:
            display.show(Image.ARROW_E)
        elif pos(x, alpha) == 0 and pos(y, alpha) == -1:
            display.show(Image.ARROW_N)
        elif pos(x, alpha) == 0 and pos(y, alpha) == 1:
            display.show(Image.ARROW_S)
        elif pos(x, alpha) == -1 and pos(y, alpha) == -1:
            display.show(Image.ARROW_NW)
        elif pos(x, alpha) == 1 and pos(y, alpha) == -1:
            display.show(Image.ARROW_NE)
        elif pos(x, alpha) == -1 and pos(y, alpha) == 1:
            display.show(Image.ARROW_SW)
        elif pos(x, alpha) == 1 and pos(y, alpha) == 1:
            display.show(Image.ARROW_SE)
        else:
            display.show(Image.TRIANGLE)

        sleep(500)


def pos(value, alpha):

    if (-1.0*alpha) <= value <= alpha:
        return 0

    if value < (-1.0*alpha):
        return -1.0

    return 1.0


main()