::: ROS in Five Days - Action Server with Custom Message

The action server will receive as a goal two words: 
UP or DOWN.

When the action server receives the UP word, 
it will move the drone 1 meter up.

When the action server receives the DOWN word,
it will move the drone 1 meter down.

As a feedback, it publishes once a second what
action it is doing (going up or going down).

When finishes the action, the result will return
nothing.

DATA:

You need to create a new action message with the
specified values as String. This type can be
imported from the std_msgs package 
(my_custom_action_msg package).

The result part of the action message will be
empty.

Since we are talking about a drone, you can
specify velocities in the three axes. You will
need to do that in order to move the robot up
and down.