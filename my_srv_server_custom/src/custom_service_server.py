#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3
# You import the service message python classes
from my_custom_srv_msg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def my_callback(request) :
    '''
    print "Request Data ==> \
        radius = " + str(request.radius) + \
        ", repetitions = "+str(request.repetitions)
    '''
    my_response = MyCustomServiceMessageResponse()

    message = Twist(
        Vector3(0.4,0,0),
        Vector3(0,0,0)
    )
    global pub  # ADDED BY IGNITE
    pub.publish(message)
    # NOTE FROM IGNITE: You should define the pub variable as global before referring to it.
    # Because pub is a global variable defined below in the main code.
    print "PUB"
    while bb8_pos <= 5.0 :
#        print "pos -> " + str(bb8_pos)
        # No hace nada...
        rate.sleep()
    #    pub.publish(message)
        
    message = Twist(
        Vector3(0,0,0),
        Vector3(0,0,0)
    )
    
    pub.publish(message)
    
    print "STOP"

    if request.radius > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    # The service Responce class
    return  my_response
    
def odom_callback(msg) :
    
#    msg.pose.pose.position.x
    global bb8_pos
    bb8_pos = abs(msg.pose.pose.position.y)
#    msg.pose.pose.orientation.z

# VARIABLE GLOBAL
bb8_pos = 0
    
rospy.init_node('service_client')
sub = rospy.Subscriber('odom', Odometry, odom_callback)
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 5)
global rate
rate = rospy.Rate(4)
# Create the Service called my_service with the defined callback
my_service = rospy.Service('/my_service', MyCustomServiceMessage, my_callback)
rospy.spin()