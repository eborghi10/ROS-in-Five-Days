#! /usr/bin/env python

import time
import rospy
import actionlib
from actionlib.msg import TestFeedback, TestResult, TestAction, TestGoal

DONE = 2
WARN = 3
ERROR = 4

# definition of the feedback callback. This will be called when feedback
# is received from the action server
def feedback_callback(feedback) :
    print "> feedback: " + str(feedback)

# initializes the action client node
rospy.init_node('drone_square_ac')
# create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_square_as', TestAction)
# waits until the action server is up and running
client.wait_for_server()

goal = TestGoal()
print "Enter distance to move: "
goal.goal = float(raw_input())

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
status = client.get_state()

while status < DONE :
    status = client.get_state()
    time.sleep(0.5)
    
status = client.get_state()
rospy.loginfo("[Result] State: "+str(status))
if status == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if status == WARN:
    rospy.logwarn("There is a warning in the Server Side")