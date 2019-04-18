# startScreen(3)

def startScreen(x):

    """
    This function displays a countdown

    :param x: Starting value of the countdown
    """

    for i in range(x, 0, -1):
        display.show(i)
        sleep(1000)