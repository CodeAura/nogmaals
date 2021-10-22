from pygame.constants import DROPBEGIN
from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier
robotArm.speed = 3

for move in range(7):
    robotArm.moveRight()
for grab in range(7):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
for x in range(3):
    for move in range(2):
        robotArm.moveLeft()
    for grab in range(7):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
for move in range(9):
    robotArm.moveRight()
for grab in range(7):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()