from pygame.constants import DROPBEGIN
from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for move in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(6):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(5):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(4):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(3):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(2):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(1):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()