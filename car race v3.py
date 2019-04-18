from microbit import *


def update(line, speed):

    # middle line
    line[1] += speed

    if line[1] > 4:
        line[1] = 0

    # moving the car

    if button_a.was_pressed():
        isApressed = True
    if button_b.was_pressed():
        isBpressed = True


def draw(line):
    display.show(Image())
    display.set_pixel(int(line[0]), int(line[1]), 9)

    display.clear()
    display.set_pixel(carX, carY, 9)



def main():
    middleLineX = 2
    middleLineY = 0
    CarX = 0
    CarY = 4
    line = [middleLineX, middleLineY]
    speed = 1

    while True:
        # processEvents()
        update(line, speed)
        draw(line)
        sleep(100)



main()