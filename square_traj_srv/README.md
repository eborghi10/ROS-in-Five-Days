# ::ROS in Five Days - My Service Server

Create a pkg that makes BB-8 move in a square. 
To move BB-8, you just have to write in the /cmd_vel
Topic as you did in the previous Unit. Bare in mind
that although this is a simulation, BB-8 has weight
and therefore it won't stop immediately due to 
inertia. Also when turning there will be friction
and inertia playing a role. Also bare in mind that
by only moving through /cmd_vel, you don't have a
way of checking if it turned what you wanted. 
It's an open loop system. Unless of course you
find a way to have some positional feedback 
information.

Add a service that accepts an Empty Service message
and activates the square movement. For that you have
to create a very similar python file as the example
above.

Create a new pkg that has a launch that calls the
service you just created.