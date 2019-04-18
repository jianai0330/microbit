from microbit import *
from random import *

def originalCar():
    originalPosition = [3, 4]
    r = randint(0, 1)
    carX = originalPosition[r]
    carY = 4
    return carX, carY

def update(line, speed):

    # middle line
    line[1] += speed

    if line[1] > 4:
        line[1] = 0

    return line


def draw(line, carX,carY):
    display.show(Image())
    display.set_pixel(int(line[0]), int(line[1]), 9)
    display.set_pixel(carX, carY, 9)

def main():
    middleLineX = 2
    middleLineY = 0
    CarX = 0
    CarY = 4
    line = [middleLineX, middleLineY]
    speed = 0.5

    while True:
        # processEvents()
        update(line, speed)
        draw(line,originalCar())
        sleep(100)



main()