from simulator import robot, FORWARD, BACKWARD, STOP

# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# 90 = 1.525

l_sence = robot.left_sonar()
r_sence = robot.right_sonar()

def nav_wall():
    '''
    this function makes it so the robot goes near the wall.
    '''
    global l_sence
    global r_sence
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    while l_sence and r_sence > 11:
        l_sence = robot.left_sonar()
        r_sence = robot.right_sonar()
        robot.motors(FORWARD, FORWARD, 0.5)
        #print(f"left = {robot.left_sonar()}, right = {robot.right_sonar()}")
    robot.motors(STOP, STOP, 0.1)

def turn_perf():
    '''
    this function is supposed to turn a perfect 360 degrees but it tkes FOREVBERRR!!! UGGGGHHHHHHHHHHHH
    '''
    global l_sence
    global r_sence
    original_right_sence = robot.right_sonar()
    original_left_sence = robot.left_sonar()
    print(f"{l_sence, r_sence} <- curent. og -> {original_right_sence, original_left_sence} ")
    robot.motors(FORWARD, BACKWARD, 0.2)
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    robot.motors(FORWARD, BACKWARD, 4*1.49999999999999999999)
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()

#------------------------------------------#

    # while l_sence != original_left_sence or r_sence != original_right_sence:
    #     robot.motors(FORWARD, BACKWARD, 0.001)
    #     l_sence = robot.left_sonar()
    #     r_sence = robot.right_sonar()
    #     print(f"{l_sence, r_sence} <curent, og> {original_right_sence, original_left_sence} ")
    # robot.motors(STOP, STOP, 0.1)

    '''
    What if you try turning right a big amount that's approximately 
    how long it takes to turn 360, then see if your sonar readings
    suggest you should turn right or left to get to the original
    sonar readings. Then spin that direction by small amounts,
    until you overshoot. Then go the other direction by even 
    smaller amounts until you overshoot. Then go the opposite 
    direction by EVEN SMALLER amounts. Pick how close you want 
    to be when you stop. (It's impossible to get the exact same 
    amount as before, but you can get within a couple decimal 
    points, which is pretty good!)
    '''

    on()

def off():
    '''
    a silly little state that is kinda annoying but im not changing.

    its also a little pointless...
    *shrugs*
    '''
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
    '''
    the function for the main state
    '''
    print("the robot is holding")
    press = input("would you like to: turn it off(o), spiral(sp), weave(w), circle(c), sense(se), or hold(h)?")
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
    """
    makes the robot spiral an ok spiral
    """
    print("the robot is going spiral")
    global l_sence
    global r_sence
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    x = 23
    y = 9
    print("Careful! if this is not the first thing you do with the robot it will probobly crash into the wall. i dont know why or how to fix it. YOuv'E bEeN wARn3d!!!")
    warning = input("do you want to continue (y/n)")
    if warning == "n":
        on()
    elif warning == "y":
        print("ok then...")
    #inital loop thingy
    nav_wall()
    robot.motors(FORWARD, BACKWARD, 1.525)
    nav_wall()
    robot.motors(FORWARD, BACKWARD, 1.525)
    nav_wall()
    robot.motors(FORWARD, BACKWARD, 1.525)
    nav_wall()
    #now need to shrink
    #TODO this might not work and is prob bad
    for i in range(7):
        robot.motors(FORWARD, BACKWARD, 1.525)
        robot.motors(STOP, STOP, 0.1)
        robot.motors(FORWARD, FORWARD, x)
        robot.motors(FORWARD, BACKWARD, 1.525)
        robot.motors(STOP, STOP, 0.1)
        robot.motors(FORWARD, FORWARD, y)
        x = x-6
        y = y-2.5
    on()

def weave(way):
    '''
    the important weave func
    '''
    global l_sence
    global r_sence
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    #nav to corner
    if way == "l":
        print("long, ok")
        nav_wall()
        robot.motors(FORWARD, BACKWARD, 1.525)
        nav_wall()
        #print("now to weave")
        for i in range(5):
            nav_wall()
            robot.motors(FORWARD, BACKWARD, 1.525)
            robot.motors(FORWARD, FORWARD, 1)
            robot.motors(FORWARD, BACKWARD, 1.525)
            nav_wall()
            robot.motors(BACKWARD, FORWARD, 1.525)
            robot.motors(FORWARD, FORWARD, 1)
            robot.motors(BACKWARD, FORWARD, 1.525)
    elif way == "s":
        print("shork, got ti")
        nav_wall()
        robot.motors(FORWARD, BACKWARD, 1.525)
        nav_wall()
        for i in range(5):
            nav_wall()
            robot.motors(FORWARD, BACKWARD, 1.525)
            robot.motors(FORWARD, FORWARD, 1)
            robot.motors(FORWARD, BACKWARD, 1.525)
            nav_wall()
            robot.motors(BACKWARD, FORWARD, 1.525)
            robot.motors(FORWARD, FORWARD, 1)
            robot.motors(BACKWARD, FORWARD, 1.525)
       #print("sorry thos feature is under construction. please try again in 10 years. or never. *shrug*")
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
    '''
    the robot makes an ALMOST circle perfect circle
    '''
    print("the robot is goinf circle")
    robot.motors(FORWARD, BACKWARD, 4*1.4999999999999999999999999999999999999999999)
    on()

def sence():
    '''
    gives you sonar readings.

    
    
    I CANT SPELL OK?!?!?
    '''
    print("the robot is going sense")
    global l_sence
    global r_sence
    l_sence = robot.left_sonar()
    r_sence = robot.right_sonar()
    print(f"the left sonar senses {l_sence} cm from the wall")
    print(f"the right sonar senses {r_sence}")
    on()
    
def again():
    '''
    if you typo or somethin
    '''
    press = input("we ask again, would you like to: turn it off(o), spiral(sp), weave(w), circle(c), sense(se), or hold(h)?")
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

on()

# # When you're done, close the simulator
# robot.exit()