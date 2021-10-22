from pygame.constants import DROPBEGIN, SCALED
from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier
robotArm.speed = 2

for move in range(4):
    for i in range(3):
        robotArm.moveRight()
    robotArm.grab()
    for i in range(7):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(6):
        robotArm.moveLeft()
    robotArm.grab()
robotArm.moveLeft()
robotArm.grab()
for I in range(3):
    for move in range(6):
        robotArm.moveRight()
    robotArm.drop()
    for move in range(6):
        robotArm.moveLeft()
    robotArm.grab()
robotArm.moveLeft()
robotArm.grab()
for I in range(2):
    for move in range(6):
        robotArm.moveRight()
    robotArm.drop()
    for move in range(6):
        robotArm.moveLeft()
    robotArm.grab()
robotArm.moveLeft()
robotArm.grab()
for I in range(1):
    for move in range(6):
        robotArm.moveRight()
    robotArm.drop()
    for move in range(6):
        robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()