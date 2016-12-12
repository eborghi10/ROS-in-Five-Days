#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

def robot_control(msg):
    
    # CW (rotates right): negative
    # CCW (rotates left): positive
    
    left = msg.ranges[:360]
    front = msg.ranges[360:481]
    right = msg.ranges[481:]
        
    if min(left) < 0.9 and min(front) >= 1.0 :
        # If it's close to the wall, go forward
        # and keep closing to the wall
        message = Twist(
            Vector3(0.3, 0, 0),
            Vector3(0, 0, 0.45)
        )
        
    if min(right) < 0.9 and min(front) >= 1.0 :
        # If it's close to the wall, go forward
        # and keep closing to the wall
        message = Twist(
            Vector3(0.3, 0, 0),
            Vector3(0, 0, -0.45)
        )
        
    elif min(left) < 0.5 :
        # If the robot is very close to the wall,
        # only rotates to the other side
        message = Twist(
            Vector3(0, 0, 0),
            Vector3(0, 0, -0.25)
        )
        
    elif min(right) < 0.5 :
        # If the robot is very close to the wall,
        # only rotates to the other side
        message = Twist(
            Vector3(0, 0, 0),
            Vector3(0, 0, 0.25)
        )
        
    elif min(left) < 2.0 and min(front) < 2.0 :
        # If it's closing to the wall,
        # slows the velocity and rotate agressively
        message = Twist(
            Vector3(0.25, 0, 0),
            Vector3(0, 0, 0.65)
        )
        
    elif min(right) < 2.0 and min(front) < 2.0 :
        message = Twist(
            Vector3(0.35, 0, 0),
            Vector3(0, 0, -0.65)
        )
        
    else :
        # Move forward
        message = Twist(
            Vector3(0.55,0,0),
            Vector3(0,0,0)
        )
        
    pub.publish(message)

# Subscriber node
rospy.init_node('mini_project_01')

# The topic "/cmd_vel" manages messages of "geometry_msgs/Twist" type.
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
# The node is subscribed to the topic "/kobuki/laser/scan"
sub = rospy.Subscriber('kobuki/laser/scan', LaserScan, robot_control)

rospy.spin()    # Blocks until ROS node is shutdown