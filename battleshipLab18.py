import radio
import random
from microbit import *

radio.on()
radio.config(channel=70, address=0x4056FFAA, group=100)

# To keep track of the location of ships and the cross-hairs a
# number from 0 to 24 is assigned to each LED.  The top left
# LED is 0 and the bottom right is 24.  The function, convertLocation()
# takes a number (from 0 to 24) and returns the x, y coordinate
# of the LED.  The y coordinate is the row (0 - 4) and
# the x coordinate is the column (0 - 4)
def main():

    loc = 0
    ships = getShips()

    # Main game loop
    while True:

        loc, hit = processEvents(loc);

        update(ships, hit);
        draw(ships, loc);

        sleep(250)


# This function responds to button presses and receives messages from the radio
# param loc       Current location of cross-hairs
# return loc, hit An update location and the message from the opponent
def processEvents(loc):

    # Write your code here


# This function updates the list of ships; removing any ships that have been hit
# param ships    List of ship locations, a location is a number between 0 and 24
# param hit      A location as a string sent from the opponent.
def update(ships, hit):

    # Write your code here


# This functions updates the LED display
# param ships    List of ship locations, a location is a number between 0 and 24
# param loc      Current location of cross-hairs
def draw(ships, loc):

    # Write your code here


# This function creates 5 random ships
# return ships A list containing 5 number, each from 0 to 24
def getShips():

    ships = []

    while len(ships) < 5:
        r = random.randint(0, 24)

        if r in ships:
            continue
        else:
            ships.append(r)

    return ships


# This function converts a location (single integer from 0 to 24) to
# an x, y coordinate ---a specific LED on the display
# param loc Current location of cross-hairs
# return x, y column x and row y of LED on the display
def convertLocation(loc):

    y = loc // 5
    x = loc - (y * 5)

    return x, y


# Call main to start game
main()