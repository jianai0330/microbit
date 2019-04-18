from microbit import *

carX = 0
carY = 4


while True:
    isApressed = False
    isBpressed = False
    display.clear()
    display.set_pixel(carX, carY, 9)

    if button_a.was_pressed():
        isApressed = True
    if button_b.was_pressed():
        isBpressed = True


    if isApressed and not isBpressed:
        carX -= 1

    if isBpressed and not isApressed:
        carX +=1

