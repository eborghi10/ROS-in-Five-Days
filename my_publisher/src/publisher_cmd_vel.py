#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
import numpy.random as np

rospy.init_node('velocity_publisher_node')
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)

rate = rospy.Rate(1000)

while not rospy.is_shutdown():
    linear_x = np.rand()
    angular_z = np.rand()
    var = Twist(Vector3(linear_x,0,0),Vector3(0,0,angular_z))
    pub.publish(var)
    rate.sleep()