#! /usr/bin/env python

'''
Before running this code is necessary to execute
the Action Server with:
$ roslaunch ardrone_as TAB-TAB
'''

import rospy
import time
import actionlib
from geometry_msgs.msg import Twist, Vector3
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

nImage = 1
motion = 0
DONE = 2
WARN = 3
ERROR = 4

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

def moveArdrone() :
    global motion
    motion += 1
    if motion <= 10:
        # MOVE UP
        pub.publish(Twist(
            Vector3(0,0,1),
            Vector3(0,0,0)))
    elif motion <= 20 :
        pub.publish(Twist(
            Vector3(0.5,-0.8,0),
            Vector3(0,0,0.5)))
    else :
        pub.publish(Twist(
            Vector3(0,0,-0.5),
            Vector3(0,0,-1)))

# initializes the action client node
rospy.init_node('drone_action_client')
pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
# create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 15 # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
status = client.get_state()
print "status: " + str(status)

while status < DONE :
    moveArdrone()
    status = client.get_state()
    time.sleep(0.5) # medio segundo

# Stop Ardrone
pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))
status = client.get_state()
rospy.loginfo("[Result] State: "+str(status))
if status == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if status == WARN:
    rospy.logwarn("There is a warning in the Server Side")