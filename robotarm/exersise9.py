from pygame.constants import DROPBEGIN, SCALED
from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier
robotArm.grab()
for move in range(0, 9):
    robotArm.moveRight()
robotArm.drop()
for move in range(0, 9):
    robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()