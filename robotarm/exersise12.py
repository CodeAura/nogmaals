from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 3
for move in range(9, 0, -1):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for I in range(move):
            robotArm.moveRight()
        robotArm.drop()
        for I in range(move):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()