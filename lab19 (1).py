from microbit import *
from math import *
from random import *




count = 0
lineX = 2
lineY = 0


def main():
    while True:
        begin()
        originalCar()        # process event here


        update()

        draw()

main()

def begin() :
    display.scroll("READY")
    display.show("3")
    sleep(1000)
    display.show("2")
    sleep(1000)
    display.show("1")
    sleep(1000)
    display.clear()


def originalCar() :
    originalPosition = [3,4]
    r = randint(0,1)
    carX = originalPosition[r]
    carY = 4
    return carX,carY


def getCars() :
    cars = []
    cars1 = []

    while len(cars) < 5 :
        n = randint(0,24)

        if n in cars :
            continue
        else :
            cars.append(n)
    for i in cars:
        cy = i // 5
        cx = i - (cy * 5)
        cars1.append([cx,cy])

    return cars,cars1




def movenMent() :
    if button_a.was_pressed() :
        carX -= 1
    if button_b.was_pressed() :
        carX += 1
    if button_a.was_pressed() and button_b.was_pressed():
        carY -= 1
    return carX,

def update(lineY,cx,cy):
        lineY += 0.5


        if lineY > 4 :
            lineY = 0

        for i in range(cars1) :
            for j in range(cars1[i]):



def draw():
    display.show(Image())
    display.set_pixel(carX, carY, 9)
    display.set_pixel(int(lineX),int(lineY),9)
    sleep(100)

    for i in cars :
        display.set_pixel(convertLocation(i),9)




