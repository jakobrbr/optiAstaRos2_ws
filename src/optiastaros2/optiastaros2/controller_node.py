#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rigidbody_msgs.msg import RigidBody, RobotCmd

import numpy as np
import pandas as pd
import sys
from xml.dom import minidom
from purePursuit import pure_pursuit, pure_pursuit_turn_speed, PID_controller
import generateRobotPath
import time

# Notes/to do:
    # Try changing the queue sizes to something bigger (10) if there are still issues. (We tried setting to queue size 1 => only care about newest)
    # Change the msg files to contain coordinates of 8 robots by default, and publish to them according to rigid body number
    
    # Change indexing of targetposarr; we should index points, not robots!
        # do not index outside the length of the target array, only index when we set a new goal!
    # In purepursuit.py line 46; change axis?
    # Do we wait for the robot to reach the point before we give new goal?
    
    # rewrite for more robots, do it for each rigidbody/name/robot number out of 8
        # Probably also rewrite the publisher function to accomodate and sort more rigid bodies.
        # robot names are 1-8, their paths are "number minus 1" (get it from index in targetposarr)
    # 

class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller_node")
        self.controller_node_ = self.create_subscription(RigidBody, "/data", self.pose_callback, 1)
        self.cmd_publisher_node_ = self.create_publisher(RobotCmd, "/cmd_vel", 1)
        
        # controller parameters:
        svg_file_path = input("Write path to route svg: (e.g. heart.svg)\n")
        with open(svg_file_path, "r") as f:
            # Read the contents of the file into a string variable
            svg_path = f.read()
        svg_str = minidom.parseString(svg_path)

        self.targetPosArr, stop_pos, stop_orient = (generateRobotPath.pointsFromDoc(svg_str,density=0.1, scale=1))
        self.i = 0
        self.last_angle = 0

        # debug messages:
        # convert list of tuples to dataframe of floats
        #targetPosDF = pd.DataFrame(targetPosArr, columns=['x', 'y'])
        print(len(self.targetPosArr)) # length is 9
        print(len(self.targetPosArr[0])) # length is 32
        #col1 = self.targetPosArr[0]
        #print(col1)
        #print(col1[0])
        #print(targetPosDF)

        self.get_logger().info("Controller node has been started")


    def pose_callback(self, msg: RigidBody):
        controller = PID_controller(1.5,0.2,0.01,0.1)
        dt = 0.01
        # get current position data and save as tuple
        currentPos = (msg.pose.x, msg.pose.y)

        # get target angle and velocity values
        current_time = time.time() # time for simulation
        target_time = time.time() + 3 # same
        angle = pure_pursuit(currentPos,self.targetPosArr[0], lookahead_distance=2) # Apply pursuit algorithm
        if np.isnan(angle) == 1:
            angle = 0
        velocity = controller.update(currentPos, self.targetPosArr[self.i], current_time, target_time, dt) # for constant vel set velocity = 1
        velocity *= pure_pursuit_turn_speed(self.last_angle,angle)
        #print("position error %f" % np.linalg.norm(np.subtract(targetPosArr[i],currentPos)))
        
        # set target values and publish them
        cmd = RobotCmd()
        cmd.linear = velocity
        cmd.angular = angle
        cmd.rigid_body_name = msg.rigid_body_name
        self.cmd_publisher_node_.publish(cmd)
        
        # the messages should be changed so that the coordinates and velocities are linked and accessible through the robot names

        # test print
        self.get_logger().info("vel and angle:" + str(cmd.linear) + " " + str(cmd.angular))

        # update last angle and target index:
        self.i += 1
        self.last_angle = angle


def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()