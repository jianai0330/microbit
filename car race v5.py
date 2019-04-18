from microbit import *
import random

def update(line, speed, car):

    # middle line
    line[1] += speed

    if line[1] > 4:
        line[1] = 0

    # moving the car
    if car[0] < 2:
        carIsLeft = True
    else:
        carIsLeft = False

    if button_a.was_pressed():
        car[0] -= 1
    if button_b.was_pressed():
        car[0] += 1
    pin0.write_digital(1)
    if not pin0.read_digital():
        car[1] -= 1
    # creat random cars
    rcars = []



    if car[0] == 2 and carIsLeft:
        car[0] += 1
    if car[0] == 2 and not carIsLeft:
        car[0] -= 1

    for i in range(len(car)):
        if car[i] > 4:
            car[i] = 0
        if car[i] < 0:
            car[i] = 4
    return car



def draw(line, car):
    display.show(Image())
    # middle line
    display.set_pixel(int(line[0]), int(line[1]), 9)
    # the car
    display.set_pixel(int(car[0]), int(car[1]), 9)
    sleep(100)


def main():
    middleLineX = 2
    middleLineY = 0
    line = [middleLineX, middleLineY]
    carX = 0
    carY = 4
    car = [carX, carY]
    speed = 1

    while True:
        # processEvents()
        update(line, speed, car)
        draw(line, car)
        sleep(100)

main()