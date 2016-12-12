#! /usr/bin/env python

'''
We can check the correct implementation of the service using:
$ rossrv show iri_wan_reproduce_trajectory/ExecTraj

string file
---


To execute the service /execute_trajectory, type:
$ roslaunch iri_wam_reproduce_trajectory start_service.lauch
'''

import rospy
import rospkg   # To find the trajectory files in Python
from iri_wam_reproduce_trajectory.srv import ExecTraj
import sys

rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way
# as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') \
        + "/config/get_food.txt"

# Initialize ROS node with the service_client
rospy.init_node('service_client_node')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
# Creates the connection to the service
exec_trajectory_srv = rospy.ServiceProxy('/execute_trajectory', ExecTraj)

print "\nExecuting service trajectory..."

result = exec_trajectory_srv(traj)

print " * Executing service \"execute_trajectory\""

print "\nPress Ctrl + C to exit"

# Pause simulation and not kill the process
rospy.spin()

