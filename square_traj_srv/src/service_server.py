#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist, Vector3

def my_callback(request):
    print "Generating the square trajectory"
    return EmptyResponse()

rospy.init_node('square_traj_service_server_node')
# Creates a service called /my_service with the defined callback
my_service = rospy.Service('square_trajectory', Empty, my_callback)
rospy.spin()  # Maintain the service open
