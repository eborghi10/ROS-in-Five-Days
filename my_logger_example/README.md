# ::: ROS in Five Days - Logger Example

Create a package that has a launch that launches a
python file with the messages with all the debugging
levels.

Try changing the LOG level in the rospy.init_node 
and see how the different messages are printed or
not in /rosout topic, depending on the level
selected (rostopic echo /rosout).