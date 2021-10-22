from pygame.constants import GL_RED_SIZE
from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 2
for x in range(7):
    robotArm.moveRight()
robotArm.grab()
color = robotArm.scan()
for x in range(9):  
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()
robotArm.drop()
robotArm.wait()