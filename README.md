# Fire_Extinguisher_Bot_Using_ROS
This repository consists of all the work done on the Aries project Fire Extinguisher Bot using ROS.

DESCRIPTION:

We have to create an autonomous fire extinguisher bot using Robot Operating System (ROS) and Gazebo software for simulation.
We detect the fire using image-processing and detection using open-cv2. After detecting it our bot uses SLAM algorithm to reach the target area using g-mapping.

OUR ACCOMPLISHMENTS ->

1)	Firstly, we have made the detection of fire (or flame) using image_processing and fire detection techniques.
2)	We have also made the turtle bot to move automatically to desired location once the location is provided to the bot.


FILES ->
This repository consists of the following files:

Turtlebot3_slam.zip ->

SLAM (simultaneous localization and mapping) is a method used for autonomous vehicles that lets you build a map and localize your vehicle in that map at the same time. SLAM algorithms allow the vehicle to map out unknown environments.
The turtlebot3_slam package provides roslaunch scripts for starting the SLAM

Flame_Detection.py -

This file contains the information about the basic code for detection of flame (or fire)

Turtlebot3_navigation.zip -

Navigation is to move the robot from one location to the specified destination in a given environment. For this purpose, a map that contains geometry information of furniture, objects, and walls of the given environment is required. The Navigation enables a robot to move from the current pose to the designated goal pose on the map 
The turtlebot3_navigation provides roslaunch scripts for starting the navigation.
turtlebot3_teleop.zip -
Once SLAM node is successfully up and running, TurtleBot3 will be exploring an unknown area of the map using teleoperation. It contains scripts which provide teleoperation using the keyboard for TurtleBot3.

screen_capture_1 .webm -

This is a live demonstration of making a map for our turtlebot using SLAM and g_mapping.

Screen_capture_2.webm -

This is a live demonstration of navigation of our bot to a given location point.

Working photos.docx -

This word document consists of some of the live working pics of our project, for example making a map for our turtlebot and about the navigation of the bot to a desired location.


Procedure->

Install ROS on Remote PC

$ sudo apt update
$ sudo apt upgrade
$ wget  https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_melodic.sh
$ chmod 755 ./install_ros_melodic.sh 
$ bash ./install_ros_melodic.sh


Install TurtleBot3 via Debian Packages.

$ sudo apt-get install ros-melodic-dynamixel-sdk
$ sudo apt-get install ros-melodic-turtlebot3-msgs
$ sudo apt-get install ros-melodic-turtlebot3


Part 1 Builiding the Map
Run SLAM Node:

Run roscore from Remote PC->
$ roscore

Open a new terminal and launch turtle bot->
roslaunch turtlebot3_bringup turtlebot3_robot.launch

Open a new terminal to launch slam->
roslaunch turtlebot3_slam turtlebot3_slam.launch


Run Teleoperation Node:

Open a new terminal->
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch


Use following keys to navigate the map
w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop


Start exploring and drawing the map

Save Map:

Open a new terminal->
$ rosrun map_server map_saver -f ~/map


After Saving map, close all the nodes.


Part 2 Navigating In Map:

Run Roscore if Closed->
$ roscore

Launch the turtlebot again->
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

Launch the Navigation->
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml


Estimate Initial Pose:

Click the 2D Pose Estimate button in the RViz menu.

 

1.	Click on the map where the actual robot is located and drag the large green arrow toward the direction where the robot is facing.
2.	Repeat step 1 until the LDS sensor data is overlaid on the saved map.


Set Navigation Goal:

1.	Click the 2D Nav Goal button in the RViz menu.
 
2.	Click on the map to set the destination of the robot and drag the green arrow toward the direction where the robot will be facing.
		

	OR

Open the New terminal and the node file to specify xy coordinate and yaw
	$ rosrun turtlebot3_slam navigate_goal.py 


