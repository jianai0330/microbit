from microbit import *
import random


def main():
    carX = 0
    carY = 4
    while True:
        x = accelerometer.get_x()
        y = accelerometer.get_y()


        incr = 1.5
        px = x/1024.0
        py = y/1024.0

        x = validate(carX + px * incr)
        y = validate(carY + py * incr)



        display.show(Image())
        display.set_pixel(int(x), int(y), 9)



def validate(x):

    if x < 0:
        return 0

    if x > 4:
        return 4

    return x
main()