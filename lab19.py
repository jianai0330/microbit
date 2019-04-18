from microbit import *
import random
import math

def main():

    """
    This is the main function where the game loop resides
    """

    collectorx = 2
    collectory = 2

    coins = makeCoins()
    #是一个list
    startScreen(3)
    #是个倒数计时321
    shine = 0.0
    #光亮
    angle = 0

    while True:

        gx, gy = processEvents()

        collectorx, collectory = update(collectorx, collectory, gx, gy, coins)

        angle += 0.3
        if angle > 3.14:
            angle = 0.0

        shine = math.sin(angle)
        draw(collectorx, collectory, coins, shine)

        sleep(150)


def processEvents():

    """
    This function gets the acceleration measurements for the x and y axes

    :return: G-force along the x and y axes
    """

    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    return x,y


def update(collectorx, collectory, gx, gy, coins):

    """
    This function updates the position of the balls and removes any coins
    that have been picked up

    :param collectorx: x coordinate of collector
    :param collectory: y coordinate of collector
    :param gx: G-force on the x axes
    :param gy: G-force on the y axes
    :param coins: List of coordinates of coins, each item is in the form: [x,y]
    :return: New position of collector
    """

    incr=1.5
    
    px = gx / 1024.0
    py = gy / 1024.0
    
    dx = py * incr
    dy = py * incr
    
    x = collertorx + dx
    y = collertory + dy
    
    if 
    
    
    
    return x,y


def draw(collectorx, collectory, coins, shine):

    """
    This function displays the collector and coins on the LED display

    :param collectorx: x coordinate of collector
    :param collectory: y coordinate of collector
    :param coins: List of coordinates of coins, each item is in the form: [x,y]
    :param shine: Value between 0 and 1.  Determines brightness of coins.
    """

    # Write your code here


def startScreen(x):

    """
    This function displays a countdown倒数计数秒

    :param x: Starting value of the countdown
    """

    for i in range(x, 0, -1):
        display.show(i)
        sleep(1000)


def makeCoins():

    """
    This function creates 'coins'.  The coins are random placed.  The center LED cannot be a coin,
    that's where the collector starts.

    :return: List of coordinates of coins, each item is in the form: [x,y]
    """

    tmp = []
    while len(tmp) < 6:
        rx = random.randint(0, 4)
        ry = random.randint(0, 4)

        if (rx != 2 and ry != 2) and ([rx, ry] not in tmp):
            tmp.append([rx, ry])

    return tmp


def validate(x):

    """
    This function makes sure a coordinate value (on the LED display) is valid.

    :param x: A value for x or y
    :return: A value between 0 and 4
    """

    if x < 0:
        return 0

    if x > 4:
        return 4

    return x


main()
