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
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    while l_sence and r_sence > 11:
        l_sence = robot.left_sonar()
        r_sence = robot.right_sonar()
        robot.motors(FORWARD, FORWARD, 0.1)
        #print(f"left = {robot.left_sonar()}, right = {robot.right_sonar()}")
    robot.motors(STOP, STOP, 0.1)

def turn_perf():
    '''
    this funchtion is supposed to turn a perfect 360 degrees but it tkes FOREVBERRR!!! UGGGGHHHHHHHHHHHH
    '''
    global l_sence
    global r_sence
    original_right_sence = robot.right_sonar()
    original_left_sence = robot.left_sonar()
    print(f"{l_sence, r_sence} <curent, og> {original_right_sence, original_left_sence} ")
    robot.motors(FORWARD, BACKWARD, 0.2)
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    while l_sence != original_left_sence or r_sence != original_right_sence:
        robot.motors(FORWARD, BACKWARD, 1)
        l_sence = robot.left_sonar()
        r_sence = robot.right_sonar()
        print(f"{l_sence, r_sence} <curent, og> {original_right_sence, original_left_sence} ")
    robot.motors(STOP, STOP, 0.1)
    on()

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
        inter_weave()
    elif press == "c":
        circle()
    elif press == "se":
        sence()
    elif press == "h":
        on()
    elif press == "pain":
        turn_perf()
    else:
        again()

def spiral():
    print("the robot is going spiral")
    global l_sence
    global r_sence
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    nav_wall()
    robot.motors(FORWARD, BACKWARD, 1.49999999999999999999)
    nav_wall()

    on()

def weave(way):
    global l_sence
    global r_sence
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    if way == "l":
        print("long, ok")
        nav_wall()
        robot.motors(FORWARD, BACKWARD, 1.525)
        print("now to weave")
    elif way == "s":
        print("shork, got ti")
    on()

def inter_weave():
    '''
    so i can make a fuction with a variable
    '''
    way = input("would you like a long weve(l) or a short weave?(s)")
    print("the robot is goin weave")
    if way == "l":
        weave("l")
    elif way == "s":
        weave("s")

# 90 = 1.525 ???
# ~360 = 6.124999999999999

def circle():
    print("the robot is goinf circle")
    robot.motors(FORWARD, BACKWARD, 4*1.49999999999999999999)
    on()

def sence():
    print("the robot is going sence")
    global l_sence
    global r_sence
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    print(f"the left sonar sences {l_sence} cm from the wall")
    print(f"the right sonar sences {r_sence}")
    on()
    
def again():
    press = input("we ask again, would you like to: turn it off(o), spiral(sp), weave(w), circle(c), sence(se), or hold(h)?")
    if press == "o":
        off()
    elif press == "sp":
        spiral()
    elif press == "w":
        inter_weave()
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