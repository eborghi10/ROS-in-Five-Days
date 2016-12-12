# :::ROS in Five Days - My Action Server

Create a package with an action server that makes
the drone move doing a square when called.

Call the action server through the topics and
observe the result and feedback.

DATA:

The size of each side of the square should be
specified in the goal message as an integer.

The feedback should publish the current second at
which the robot is while doing the square.

The result should publish the total number of
seconds it took to the drone to do the square.

Use the Test.action message for that action
server. Use the shell command locate Test.action
to find where it is defined that message.

NOTES:

int32 goal
---
int32 result
---
int32 feedback