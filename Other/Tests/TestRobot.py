from RobotGUI.Logic import Robot
from time import sleep
import sys

# Get all plugged in uArms
connecteduArms = Robot.getConnectedRobots()


# If no robots were found, exit the script
if len(connecteduArms) == 0:
    print("No robots found!")
    sys.exit()




robot = Robot.Robot()


# Set the uArm. This process is threaded, usually so that a GUI can run.
robot.setUArm(connecteduArms[0][0])


# Wait for the thread to finish.
while not robot.connected(): sleep(.1)
print("Robot connected! ")

# Prepare a move. Nothing will happen until robot.Refresh() is called
robot.setSpeed(10)
robot.setPos(x=0, y=-15, z=15)
robot.setWrist(90)
robot.setGripper(True)
robot.refresh()


robot.setPos(x=10, relative=True)
robot.refresh()
robot.setPos(x=-20, relative=True)
robot.refresh()
robot.setPos(x=0, y=-15, z=15)
robot.refresh()


# Wait for robot to finish
robot.wait()

# Turn off the gripper
robot.setGripper(False)
robot.refresh()

