from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# 90 = 1.525

l_sence = robot.left_sonar()
r_sence = robot.right_sonar()

def nav_wall():
    global l_sence
    global r_sence
    while l_sence and r_sence > 11:
        l_sence = robot.left_sonar()
        r_sence = robot.right_sonar()
        robot.motors(FORWARD, FORWARD, 0.1)
        print(f"left = {robot.left_sonar()}, right = {robot.right_sonar()}")
    robot.motors(STOP, STOP, 0.1)

def turn_perf():
    global l_sence
    global r_sence
    original_right_sence = r_sence
    original_left_sence = l_sence
    while l_sence and r_sence != original_left_sence and original_r_sence:
        robot.motors(FORWARD, FORWARD, 0.1)
    robot.motors(STOP, STOP, 0.1)

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
    global l_sence
    global r_sence
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

def weave():
    global l_sence
    global r_sence
    way = input("would you like a long weve(l) or a short weave?(s)")
    print("the robot is goin weave")
    if way == "l":
        print("long, ok")
        nav_wall()
        robot.motors(FORWARD, BACKWARD, 1.499999999999999999999)
        print("now to weave")
    elif way == "s":
        print("shork, got ti")
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

# 90 = 1.525
# ~360 = 6.124999999999999

def circle():
    print("the robot is goinf circle")
    robot.motors(FORWARD, BACKWARD, 4*1.49999999999999999999)
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
    global l_sence
    global r_sence
    print(f"the left sonar sences {l_sence} cm from the wall")
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