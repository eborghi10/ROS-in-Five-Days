#! /usr/bin/env python 
#This line will ensure the interpreter used is the first one on your environment's $PATH.   Always we create a Python file we'll need to start it with this line at the top.

import rospy # We import the rospy, which is a Python library for ROS.

rospy.init_node('ObiWan') # We initiate a node called ObiWan
rate = rospy.Rate(2) # We create a Rate object
while not rospy.is_shutdown():
    print "Help me Obi-Wan Kenobi, you're my only hope" # A simple Python print
    rate.sleep()