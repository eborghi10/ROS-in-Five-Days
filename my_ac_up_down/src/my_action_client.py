#! /usr/bin/env python

import time
import rospy
import actionlib
from my_custom_action_msg.msg import MyActionMsgFeedback, MyActionMsgResult, MyActionMsgAction, MyActionMsgGoal

DONE = 2
WARN = 3
ERROR = 4

# definition of the feedback callback. This will be called when feedback
# is received from the action server
def feedback_callback(feedback) :
#    print "> feedback: " + str(feedback)
    pass

# initializes the action client node
rospy.init_node('MyActionClient')
# create the connection to the action server
client = actionlib.SimpleActionClient('my_action_server', MyActionMsgAction)
# waits until the action server is up and running
client.wait_for_server()

direction = MyActionMsgGoal()
#print ">> Move Parrot AR.DRONE [UP] or [DOWN]? "
#direction.goal = raw_input()
direction.goal = "DOWN" # Option by default
# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(direction, feedback_cb=feedback_callback)

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
status = client.get_state()

while status < DONE :
    print ">> Move Parrot AR.DRONE [UP] or [DOWN]? "
    var = raw_input()
    direction.goal = var
    client.send_goal(direction, feedback_cb=feedback_callback)
    
    status = client.get_state()
    
status = client.get_state()

if status == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if status == WARN:
    rospy.logwarn("There is a warning in the Server Side")