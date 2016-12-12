#! /usr/bin/env python

import rospy
import actionlib
# To move up and down the AR Drone
from geometry_msgs.msg import Twist, Vector3, PoseStamped
# Custom Action Library
from my_custom_action_msg.msg import MyActionMsgFeedback, MyActionMsgResult, MyActionMsgAction

def stopDrone() :
    print "> Drone stopped <"
    global pub
    pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))


class MyActionServerClass(object):
    
    # create messages that are used to publish feedback/result
    _feedback = MyActionMsgFeedback()
    _result   = MyActionMsgResult()

    def __init__(self):
        global pub
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    
        # creates the action server
        self._as = actionlib.SimpleActionServer('my_action_server', MyActionMsgAction, self.goal_callback, False)
        self._as.start()
    
    def goal_callback(self, goal):
        # this callback is called when the action server is called.
    
        # helper variables
        r = rospy.Rate(4)
    
        direction = goal.goal
        self._feedback.feedback = direction
        # publish info to the console for the user

        while True == True:
        
            # check that preempt (cancelation) has not been requested by the action client
            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                # the following line, sets the client in preempted state (goal cancelled)
                self._as.set_preempted()
                break
      
            if direction == "DOWN":
#                print "> DOWN"
                pub.publish(Twist(
                    Vector3(0,0,-0.3),
                    Vector3(0,0,0)))
            elif direction == "UP":
#                print "> UP"
                pub.publish(Twist(
                    Vector3(0,0,0.3),
                    Vector3(0,0,0)))
            else:
                print "> Error sending direction: [UP, DOWN]"
                stopDrone()
      
            # publish the feedback
            self._as.publish_feedback(self._feedback)
      
            r.sleep()

        stopDrone()
        # If success, don't print anything
      
if __name__ == '__main__':
    rospy.init_node('MyActionServer')
    MyActionServerClass()
    rospy.spin()