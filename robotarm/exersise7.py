from pygame.constants import DROPBEGIN
from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier
robotArm.speed = 2

for I in range(8):
    robotArm.moveRight()
    robotArm.grab()
    for I in range(7):
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()