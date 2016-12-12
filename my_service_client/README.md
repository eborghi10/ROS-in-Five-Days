# ::ROS in Five Days - My Service Client

Create a package with a launch and a Python file.
For the Python file, modify the previous code that
called /gazebo/delete_model, to call the
/execute_trajectory service instead.

Make sure that the /execute_trajectory service is
running, otherwise launch it manually.

HINT:

Check the launch file of the iri_wam_aff_demo, 
and use what you learned about roslaunch.

WARNING:

You should have killed the start_demo.launch. 
You only need the /execute_trajectory service, 
if you have the start_demo launched, there will
be a service already using execute_traj, which is
the work that you want YOUR launch to perform.

Get the type of service message.

Modify the program with the proper service types.

Fill the service message with the proper data
(the name of the file that describes the
trajectory of the robot arm).

Call the service.

DATA FOR EXERCISE

You need to know how to find the trajectory 
files with Python:

import rospkg
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way
# as $(find name_of_package) in the launch files.
traj = rospack.get_path(
    'iri_wam_reproduce_trajectory') +
    "/config/get_food.txt"