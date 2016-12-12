#! /usr/bin/env python

import rospy
import actionlib
from geometry_msgs.msg import Twist, Vector3, PoseStamped
# Uses Test.action from actionlib as action messages
from actionlib.msg import TestFeedback, TestResult, TestAction

cnt = 0
posX_0 = 0
posY_0 = 0
posX = 0
posY = 0
movingUp = True

def stopDrone() :
    print "> Drone stopped <"
    global pub
    pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))

def drone_pos_handler(msg):
    global cnt, posX_0, posY_0, posX, posY, movingUp
    
    if cnt == 0 :
        cnt += 1
        stopDrone()
        print "> Setting posX_0 and posY_0"
        # Takes initial position
        posX_0 = msg.pose.position.x
        posY_0 = msg.pose.position.y
    elif cnt == 1 :
        posX = msg.pose.position.x - posX_0
        posY = msg.pose.position.y - posY_0
    
    if msg.pose.position.z < 5 :
        # MOVE UP
        pub.publish(Twist(
                Vector3(0,0,0.5),
                Vector3(0,0,0)))
    elif movingUp == True :
        movingUp = False
        cnt = 0
        stopDrone()

class ArdroneSquareClass(object):
    
  # create messages that are used to publish feedback/result
  _feedback = TestFeedback()
  _result   = TestResult()

  def __init__(self):
    global sub, pub
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber('ground_truth_to_tf/pose', PoseStamped, drone_pos_handler)
    
    # creates the action server
    self._as = actionlib.SimpleActionServer("ardrone_square_as", TestAction, self.goal_callback, False)
    self._as.start()
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called.
    
    # helper variables
    r = rospy.Rate(4)
    success = True
    
    self._feedback.feedback = 0
    tmp = 0
    
    # publish info to the console for the user
    rospy.loginfo('"ardron_square_as": Executing, moving drone at time %i' % ( self._feedback.feedback ))
    
    # MOVES THE DRONE
    distance = goal.goal
    i = 1
    while success == True:
        
        if movingUp == False: 
    
          # check that preempt (cancelation) has not been requested by the action client
          if self._as.is_preempt_requested():
            rospy.loginfo('The goal has been cancelled/preempted')
            # the following line, sets the client in preempted state (goal cancelled)
            self._as.set_preempted()
            success = False
            # we end the calculation of the Fibonacci sequence
            break
        
          global posX_0, posY_0, posX, posY
          
          if i == 1:
              print "1 > (%d,%d) -> (%d,%d) | %d" %(posX_0, posY_0, posX, posY, distance)
              pub.publish(Twist(
                  Vector3(0.6,0,0),
                  Vector3(0,0,0)))
          elif i == 2:
              print "2 > (%d,%d) -> (%d,%d) | %d" %(posX_0, posY_0, posX, posY, distance)
              pub.publish(Twist(
                  Vector3(0,0.6,0),
                  Vector3(0,0,0)))
          elif i == 3:
              print "3 > (%d,%d) -> (%d,%d) | %d" %(posX_0, posY_0, posX, posY, distance)
              pub.publish(Twist(
                  Vector3(-0.6,0,0),
                  Vector3(0,0,0)))
          elif i == 4:
              print "4 > (%d,%d) -> (%d,%d) | %d" %(posX_0,posY_0, posX,posY, distance)
              pub.publish(Twist(
                  Vector3(0,-0.6,0),
                  Vector3(0,0,0)))
          # builds the next feedback msg to be sent
          tmp += 1
          if tmp >= 4 :
              tmp = 0
              self._feedback.feedback += 1
              # publish the feedback
              self._as.publish_feedback(self._feedback)
          # the sequence is computed at 1 Hz frequency
          r.sleep()
          
          if (posX >= distance and i == 1) \
          or (posY >= distance and i == 2) \
          or (abs(posX) >= distance and i == 3) \
          or (abs(posY) >= distance and i == 4) :
              i += 1
              stopDrone()
              global cnt
              cnt = 0
              posX = 0  # For security and avoid fast success
              posY = 0
          if i > 4 :
              break
    
    stopDrone()
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
    if success:
      self._result.result = self._feedback.feedback
      rospy.loginfo('Total spent time moving the drone %d' % self._result.result )
      self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('ardrone_as')
  ArdroneSquareClass()
  rospy.spin()