'''
Name: Maxime Foucault
Name: Ai Jian
Groupe: 12
project: Avoid Obstacles (car race)
'''

'''
game rules:
Avoid the cars coming from the top as long as posible. Your car is at the bottom of the screen.
The middle column is used for to display the road broken line. No car can be on it.
When crashing with an enemy your score scrolls on the screen.
game manual:
starts with reset button
tap A to go left
tap B to go right
lean forward to accelerate
lean backward to slow down
keep the device horizontal to go at normal speed (speed increases with time)
'''

from microbit import *
import random


def updateEnemy(enemy, speed):
    '''
    creates randomly and updates the position of an enemy each time the function is called
    controls the flow of enemies and make sure there are not too many enemies (with the random function test)
    delete the enemy when it is gone
    param enemy: is a list regrouping the x and y of the enemies positions and enemy[2] indicates if the car already exists
    param speed: is the coefficient for the speed of movement of all on the elements on the board
    return: the new list for the enemy car description
    '''
    if enemy[2] == 1:
        enemySpeed = 0.1
        enemy[1] += speed-enemySpeed
        if int(enemy[1]) < 0:
            enemy[2] = 0
        if int(enemy[1]) > 4 :
            enemy[2] = 0

    if enemy[2] != 1:
        isCar = random.randint(0, 10)
        enemyX = random.randint(0, 4)
        enemyY = 0
        if isCar < 3 and enemyX != 2:
            enemy[0] = enemyX
            enemy[1] = enemyY
            enemy[2] = 1
    return enemy


def update(updateLine, updateSpeed, updateCar, updateEnemy1, updateEnemy2, speedBoost, updateGameOver):
    '''
    updates the whole board:
    adjusts the speed of the player depending on the inclination
    moves the middle line
    updates the player's car if the player is turning right or left (according to the buttons)
    calls the function updating the enemy (for each enemy)
    checks if there is an accident (enemy and player on the same pixel) to update the gameover variable
    param updateLine: list with all the values of middle line in order to know where it is and how to change it
    param updateSpeed: is the coefficient serving to know how fast things should move
    param updateCar: list with all necessary values about the player's car
    param updateEnemy(1/2): lists with all necessary values about the enemies
    param speedBoost: speed adjustment used to increase speed throughout time to make the game more difficult with time
    param updateGameOver: boolean value to know if the the game should stop because of an accident
    return: all the updated values of the variables for the middle line, the speed of the player according to the inclination and time elapsed, the car of the player, the enemies and gameOver boolean if there was an accident
    '''
    if accelerometer.is_gesture('up'):
        updateSpeed = 0
    elif accelerometer.is_gesture('down'):
        updateSpeed = 1
    else:
        updateSpeed = min((0.5 + speedBoost), 1)

    updateLine[1] += updateSpeed

    if updateLine[1] > 4:
        updateLine[1] = 0


    if updateCar[0] < 2:
        updateCarIsLeft = True
    else:
        updateCarIsLeft = False

    if button_a.was_pressed() and updateCar[0] != 0:
        updateCar[0] -= 1
    if button_b.was_pressed() and updateCar[0] != 4:
        updateCar[0] += 1

    if updateCar[0] == 2 and updateCarIsLeft:
        updateCar[0] += 1
    if updateCar[0] == 2 and not updateCarIsLeft:
        updateCar[0] -= 1

    updateEnemy1 = updateEnemy(updateEnemy1, updateSpeed)
    updateEnemy2 = updateEnemy(updateEnemy2, updateSpeed)

    if int(updateEnemy1[0]) == int(updateCar[0]) and int(updateEnemy1[1]) == int(updateCar[1]):
        updateGameOver = 1
    if int(updateEnemy2[0]) == int(updateCar[0]) and int(updateEnemy2[1]) == int(updateCar[1]):
        updateGameOver = 1

    return updateLine, updateSpeed, updateCar, updateEnemy1, updateEnemy2, updateGameOver


def draw(drawLine, drawCar, drawEnemy1, drawEnemy2):
    '''
    prints on the screen all of the visible elements of the game (middle line, player's car, enemies)
    param drawLine: list of the values about the middle line
    param drawCar: list of the x and y of the player's car
    param drawEnemy(1/2): list of values about the enemies (the x, the y, and boolean value for if the enemy exists already)
    returns: nothing
    '''
    display.show(Image())

    display.set_pixel(int(drawLine[0]), int(drawLine[1]), 5)

    display.set_pixel(int(drawCar[0]), int(drawCar[1]), 9)

    if drawEnemy1[2] == 1 and drawEnemy1[1] >0 and drawEnemy1[1] <5 :
        display.set_pixel(int(drawEnemy1[0]), int(drawEnemy1[1]), 9)

    if drawEnemy2[2]==1 and drawEnemy2[1] >0 and drawEnemy2[1] <5 :
        display.set_pixel(int(drawEnemy2[0]), int(drawEnemy2[1]), 9)


def main():
    '''
    main function
    initiates the variables and calls every other function required for the game to work properly
    '''
    middleLineX = 2
    middleLineY = 0
    line = [middleLineX, middleLineY]
    car = [0, 4]
    speed = 0.5
    enemy1 = [1, 0, 1]
    enemy2 = [0, 0, 0]

    GameOver = 0
    startTime = running_time()


    while GameOver == 0:
        '''
        while loop made to make the game go on until game over
        and calls the two principal functions to update data and display
        '''
        line, speed, car, enemy1, enemy2, GameOver = update(line, speed, car, enemy1, enemy2, (running_time()-startTime)/100000, GameOver)
        draw(line, car, enemy1, enemy2)
        sleep(100)

    endTime = running_time()
    score = int((endTime - startTime) / 1000)
    display.clear()
    display.scroll(score)

'''
makes the game start
'''
main()
