from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
def off():
    print("the robot is off")
    press = input("would you like to: turn it on(o), or leave (l)?")
    if press == "o":
        print("the robot is on")
        on()
    elif press == "l":
        robot.exit()
    else:
        off()

def on():
    print("the robot is holding")
    press = input("would you like to: turn it off(o), spiral(sp), weave(w), circle(c), sence(se), or hold(h)?")
    if press == "o":
        off()
    elif press == "sp":
        spiral()
    elif press == "w":
        weave()
    elif press == "c":
        circle()
    elif press == "se":
        sence()
    elif press == "h":
        on()
    else:
        again()

def spiral():
    print("the robot is going spiral")
    press = input("would you like to: turn it off(o), spiral again(sp), weave(w), circle(c), sence(se), or hold(h)?")
    if press == "o":
        off()
    elif press == "sp":
        spiral()
    elif press == "w":
        weave()
    elif press == "c":
        circle()
    elif press == "se":
        sence()
    elif press == "h":
        on()
    else:
        again()

def weave(way):
    way = input("would you like a long weve or a short weave?")
    print("the robot is goin weave")
    press = input("would you like to: turn it off(o), spiral(sp), weave again(w), circle(c), sence(se), or hold(h)?")
    if press == "o":
        off()
    elif press == "sp":
        spiral()
    elif press == "w":
        weave()
    elif press == "c":
        circle()
    elif press == "se":
        sence()
    elif press == "h":
        on()
    else:
        again()

def circle():
    print("the robot is goinf circle")
    robot.motors(FORWARD, BACKWARD, 6.122334455)
    press = input("would you like to: turn it off(o), spiral(sp), weave(w), circle again(c), sence,(se), or hold(h)?")
    if press == "o":
        off()
    elif press == "sp":
        spiral()
    elif press == "w":
        weave()
    elif press == "c":
        circle()
    elif press == "se":
        sence()
    elif press == "h":
        on()
    else:
        again()

def sence():
    print("the robot is going sence")
    left_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    print(f"the left sonar sences {left_sence} from the wall")
    print(f"the right sonar sences {r_sence}")
    press = input("would you like to: turn it off(o), spiral(sp), weave(w), circle(c), sence again(se), or hold(h)?")
    if press == "o":
        off()
    elif press == "sp":
        spiral()
    elif press == "w":
        weave()
    elif press == "c":
        circle()
    elif press == "se":
        sence()
    elif press == "h":
        on()
    else:
        again()
    
def again():
    press = input("we ask again, would you like to: turn it off(o), spiral(sp), weave(w), circle(c), sence(se), or hold(h)?")
    if press == "o":
        off()
    elif press == "sp":
        spiral()
    elif press == "w":
        weave()
    elif press == "c":
        circle()
    elif press == "se":
        sence()
    elif press == "h":
        on()
    else:
        again()

off()

# # When you're done, close the simulator
# robot.exit()