#! /usr/bin/env python
import rospy
import time

from common_dir.common_things import cool, CmdVelPub


if __name__ == '__main__':
    cool('TheConstruct')
    
    stop_time = 1
    move_time = 3
    
    rospy.init_node('test_import', log_level=rospy.INFO)
    
    move_object = CmdVelPub()
    rospy.loginfo("Starting...")
    move_object.move_robot(direction="stop")
    time.sleep(stop_time)
    
    rospy.loginfo("Forwards...")
    move_object.move_robot(direction="forwards")
    time.sleep(move_time)
    
    rospy.loginfo("Stopping...")
    move_object.move_robot(direction="stop")
    time.sleep(stop_time)
    
    rospy.loginfo("Forwards...")
    move_object.move_robot(direction="backwards")
    time.sleep(move_time)
    
    rospy.loginfo("Stopping...")
    move_object.move_robot(direction="stop")