#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print "(" + str(msg.pose.pose.position.x) + \
          ", " + str(msg.pose.pose.position.y) + \
          ", " + str(msg.pose.pose.position.z) + ")"
    
rospy.init_node('odometry_subscriber_node')
sub = rospy.Subscriber('odom', Odometry, callback)
rospy.spin()