# Let's consider one place during the competition where functions might be useful.

# We are programming our robot to move forward and then stop three times
# move forward -> stop -> move forward -> stop -> move forward -> stop

# To control our robot we set the motor values with the following functions
def set_left_motor(speed):
    print("Set left motor to", speed)

def set_right_motor(speed):
    print("Set right motor to", speed)

# Now let's do our movement now!

# Move forward 
set_left_motor(1)
set_right_motor(1)

# Stop
set_left_motor(0)
set_right_motor(0)

# Move forward 
set_left_motor(1)
set_right_motor(1)

# Stop
set_left_motor(0)
set_right_motor(0)

# Move forward 
set_left_motor(1)
set_right_motor(1)

# Stop
set_left_motor(0)
set_right_motor(0)

# Great!
# Now, we've changed our robot to use 4 motors. We must now set all four motors to move

# We can use these two new functions to control the new motors
def set_back_left_motor(speed):
    print("Set left motor to", speed)

def set_back_right_motor(speed):
    print("Set right motor to", speed)

# To reimplement the motion of our robot, we'd have to use twice as many lines.
# Then what if we added even more motors? This will take more and more work to
# keep up to date.

# Perhaps we can we use functions! Fill in the move_forward and stop functions
# to make the following code make our robot move correctly.

def move_forward():
    # Your code below

    # Your code above

def stop():
    # Your code below

    # Your code above

# Now let's do our robot movement:

move_forward()
stop()
move_forward()
stop()
move_forward()
stop()

# By using functions to define moving forward and stopping, we can make it much
# easier to manage our code.
