#! /usr/bin/env python

# This line will ensure the interpreter used is the first one on your environment's $PATH.
# Always we create a Python file we'll need to start it with this line at the top.

# We import the rospy, which is a Python library for ROS.
import rospy

# We initiate a node called ObiWan
rospy.init_node('ObiWan')

# We create a Rate object
rate = rospy.Rate(2)

# We prevent the program to end until Ctrl + C
while not rospy.is_shutdown():
    # A simple Python print
    print "Help me Obi-Wan Kenobi, you're my only hope"
    # We sleep the needed time to mantain the Rate fixed above
    rate.sleep()