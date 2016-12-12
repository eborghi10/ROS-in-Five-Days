# ::ROS in Five Days - Mini Project

# Publisher

You'll need to create a Publisher that writes
into the /cmd_vel topic in order to move the robot.

# Subscriber

You'll need to create a Subscriber that reads
from the /kobuki/laser/scan topic. 
This is the topic where the laser publishes its data.

HINTS: 

The data that is published into the 
/kobuki/laser/scan topic has a large structure.
For this project, you just have to pay attention
to the 'ranges' array.

The 'ranges' array has a lot of values. 
The ones that are in the middle represent the
readings that the laser is doing right in front of
him. This means that the values in the middle of
the array will be the ones that detect the square.
So in order to avoid the square, you just have to
read these values.

The laser has a range of 30m. When you get
readings of values around 30, it means that the
laser isn't detecting anything. If you get a
value that is under 30, this will mean that the
laser is detecting some kind of obstacle in that
direction.

The scope of the laser is of about 180 degrees.
This means that the values at the beginning and
at the end of the 'ranges' array will be the ones
related to the readings at the sides of the laser,
while the values in the middle of the array will
be the ones related to the front of the laser.

# General

Depending on the readings you receive from the 
laser's topic, you'll have to change the data 
you're sending to the /cmd_vel topic, in order 
to avoid the square.