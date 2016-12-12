#! /usr/bin/env python

'''
* IT'S NOT NECESSARY TO EXECUTE THE FIRST COMMAND

To test this program it has to be running a service server:
$ roslaunch my_srv_server_custom TAB-TAB

Then, run this package:
$ roslaunch srv_and_pub TAB-TAB
'''

import rospy
from my_custom_srv_msg.srv import MyCustomServiceMessage

rospy.init_node('srv_and_pub')
rate = rospy.Rate(0.16)

while not rospy.is_shutdown() :
    
    # It don't use Rate() because waits for the service response.
    rospy.wait_for_service('my_service')
    
    service_message = rospy.ServiceProxy('/my_service', MyCustomServiceMessage)

    MyCustomServiceMessage.radius = 5.0
    MyCustomServiceMessage.repetitions = 1

    success = service_message(MyCustomServiceMessage.radius, MyCustomServiceMessage.repetitions)
    rate.sleep()
#    print "Success?: " + str(success)