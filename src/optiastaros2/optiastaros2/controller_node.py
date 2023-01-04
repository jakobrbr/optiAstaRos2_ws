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
i = 0
last_angle = 0
targetPosArr = [0,0,0,0,0,0,0,0] # maybe we dont need to initialize with the zeros

# Notes:
# Try changing the queue size to something bigger if there are still issues.
# Change the msg files to contain coordinates of 8 robots by default, and publish to them according to rigid body number

class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller_node")
        self.controller_node_ = self.create_subscription(RigidBody, "/data", self.pose_callback, 1) # try setting to queue size 1, only care about newest
        self.cmd_publisher_node_ = self.create_publisher(RobotCmd, "/cmd_vel", 1) # input self.pose_callback??
        
        # controller parameters:
        svg_file_path = input("Write path to route svg.\n")
        with open(svg_file_path, "r") as f:
            # Read the contents of the file into a string variable
            svg_path = f.read()
        svg_str = minidom.parseString(svg_path)

        targetPosArr, stop_pos, stop_orient = (generateRobotPath.pointsFromDoc(svg_str,density=0.1, scale=1))

        # convert list of tuples to dataframe of floats
        #targetPosDF = pd.DataFrame(targetPosArr, columns=['x', 'y'])
        print(len(targetPosArr))
        print(len(targetPosArr[0]))
        col1 = targetPosArr[0]
        print(col1)
        print(col1[0])
        #print(targetPosDF)
        self.get_logger().info("Controller node has been started")


    # create seperate function for publishing and call it up ind self.cmd_publisher?
    # we got an error about something with the inputs in pose_callback 

    # try publishing debug messages of the targetposition array and the current position.

    def pose_callback(self, msg: RigidBody):
        # rewrite for more robots, do it for each rigidbody/name/robot number out of 8
        # probably also rewrite publisher node?
        #self.get_logger().info(str(msg.pose.x)) # test print x coord

        # robot names are 1-8, their paths are #-1 (get it from index in targetposarr)

        controller = PID_controller(1.5,0.2,0.01,0.1)
        global i 
        dt = 0.01
        # get current position data and save as tuple
        currentPos = (msg.pose.x, msg.pose.y)


        # get target angle and velocity values
        current_time = time.time() # time for simulation
        target_time = time.time() + 3 # same
        angle = pure_pursuit(currentPos,targetPosArr[0], lookahead_distance=2) # Apply pursuit algorithm
        if np.isnan(angle) == 1:
            angle = 0
        velocity = controller.update(currentPos, targetPosArr[i], current_time, target_time, dt) # for constant vel set velocity = 1
        velocity *= pure_pursuit_turn_speed(last_angle,angle)
        #print("position error %f" % np.linalg.norm(np.subtract(targetPosArr[i],currentPos)))
        
        # set target values and publish them
        cmd = RigidBody()
        cmd.linear = velocity # we temporarily use the rigidbody message instead of cmd_vel
        cmd.angular = angle
        cmd.rigid_body_name = msg.rigid_body_name
        self.cmd_publisher_node_.publish(cmd)
        
        # the messages should be changed so that the coordinates and velocities are linked and accessible through their names

        # test print
        #self.get_logger().info("vel and angle:" + str(velocity) + " " + str(angle))
        # update last angle and target index
        i += 1
        last_angle = angle


def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()