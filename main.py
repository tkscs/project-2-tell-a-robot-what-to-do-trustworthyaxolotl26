from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
def off():
    print("the robot is off")
    press = input("would you like to: turn it on(o), or do nothing (n)?")
    if press == "o":
        on()
    else:
        off()

def on():
    print("the robot is on")

def spiral():
    print("the robot is going spiral")

def weave(way):
    print("the robot is goin weave")

def circle():
    print("the robot is goinf circle")

def sence():
    print("the robot is going sence")

# When you're done, close the simulator
robot.exit()