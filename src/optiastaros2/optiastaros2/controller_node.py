#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rigidbody_msgs.msg import RigidBody, RobotCmd

import numpy as np
import pandas as pd
import sys
from xml.dom import minidom
import time
from purePursuit import pure_pursuit, velocity_controller, pure_pursuit_turn_speed
import generateRobotPath


class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller_node")
        
        # init sub for 8 robots:
        self.create_subscription(RigidBody, "/robot0/data", self.robot0_callback, 1)
        self.create_subscription(RigidBody, "/robot1/data", self.robot1_callback, 1)
        #self.create_subscription(RigidBody, "/robot2/data", self.robot2_callback, 1)
        #self.create_subscription(RigidBody, "/robot3/data", self.robot3_callback, 1)
        #self.create_subscription(RigidBody, "/robot4/data", self.robot4_callback, 1)
        #self.create_subscription(RigidBody, "/robot5/data", self.robot5_callback, 1)
        #self.create_subscription(RigidBody, "/robot6/data", self.robot6_callback, 1)
        #self.create_subscription(RigidBody, "/robot7/data", self.robot7_callback, 1)

        # init pub for 8 robots:
        self.set_publishers = []
        for i in range(8): # create 8 publishers to topic "/cmd_vel"
            publisher = self.create_publisher(RobotCmd, "/robot{}/cmd_vel".format(i), 1)
            self.set_publishers.append(publisher)

        # init angle buffer array with size 10, create one for each robot used
        self.angBuffer0 = np.zeros(10)
        self.angBuffer1 = np.zeros(10)

        # init robot last angle, create one for each robot
        self.last_angle0 = 0
        self.last_angle1 = 0

        # import svg file
        svg_file_path = input("Write path to route svg: (e.g. heart.svg)\n")
        with open(svg_file_path, "r") as f:
            # Read the contents of the file into a string variable
            svg_path = f.read()
        svg_str = minidom.parseString(svg_path)
        

        # generate path from svg file
        self.targetPosArr, stop_pos, stop_orient = (generateRobotPath.pointsFromDoc(svg_str,density=0.1, scale=1)) # set density and scale of path

        # set time and goal completion time, could be 35 for Sine
        goal = 35 # seconds

        self.start_time = np.floor(time.time())
        self.lap_time = np.floor(time.time()) + goal

        self.get_logger().info("Controller node has been started")

    def map_value(self, val, in_min, in_max, out_min, out_max):
        #return (( (val - in_min) / (in_max - in_min) ) * (out_max - out_min) + out_min)
        return ((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    def robot0_callback(self, msg: RigidBody):
        n = 0 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        kp = 0.1
        #velocity = 0.5 # constant linear velocity (should be float!)

        if self.targetPosArr[n]: # maybe not needed to check
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y) # array of tuples (8x2) should contain the coordinates of all 8 robots 
            currentHeading = msg.rot.z # current rotation around the axis

            # unwrap heading angle
            self.angBuffer0 = np.append(self.angBuffer0[1:], currentHeading)
            unwrapped_heading = np.unwrap(self.angBuffer0)
            self.angBuffer0 = unwrapped_heading

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], unwrapped_heading[-1], lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0
            
            # for constant velocity comment this out and write a number: velocity = 0.5 # the number has to be float
            #currentPos = np.array(currentPos).reshape(1,2)
            velocity = velocity_controller(currentPos,self.targetPosArr[n],self.start_time,self.lap_time,kp)
            velocity *= pure_pursuit_turn_speed(self.last_angle0,angle) # turn controller

            # set publisher and publish the commands (we dont need to publish the name)
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 0: ang vel" + str(cmd.angular))
            #self.get_logger().info("robot 0: ang" + str(unwrapped_heading[-1]))
            self.last_angle0 = angle
            publisher.publish(cmd)
    
    def robot1_callback(self, msg: RigidBody):
        n = 1 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        kp = 0.1
        #velocity = 0.5 # linear velocity

        if self.targetPosArr[n]:
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y)
            currentHeading = msg.rot.z # current rotation around the axis

            # unwrap heading angle
            self.angBuffer1 = np.append(self.angBuffer1[1:], currentHeading)
            unwrapped_heading = np.unwrap(self.angBuffer1)
            self.angBuffer1 = unwrapped_heading

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], currentHeading, lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0
            
            # for constant velocity comment this out and write a number: velocity = 0.5 # the number has to be float
            velocity = velocity_controller(currentPos,self.targetPosArr[n],self.start_time,self.lap_time)
            velocity *= pure_pursuit_turn_speed(self.last_angle0,angle) # turn controller

            # set publisher and publish the commands
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 1: ang vel" + str(cmd.angular)) # debug
            self.last_angle0 = angle
            publisher.publish(cmd)
    
    def robot2_callback(self, msg: RigidBody):
        n = 2 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        velocity = 0.5 # linear velocity

        if self.targetPosArr[n]:
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y)
            currentHeading = msg.rot.z # current rotation around the axis

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], currentHeading, lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0

            # set publisher and publish the commands
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 2: ang vel" + str(cmd.angular)) # debug
            publisher.publish(cmd)
    
    def robot3_callback(self, msg: RigidBody):
        n = 3 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        velocity = 0.5 # linear velocity

        if self.targetPosArr[n]:
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y)
            currentHeading = msg.rot.z # current rotation around the axis

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], currentHeading, lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0

            # set publisher and publish the commands
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 3: ang vel" + str(cmd.angular)) # debug
            publisher.publish(cmd)
    
    def robot4_callback(self, msg: RigidBody):
        n = 4 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        velocity = 0.5 # linear velocity

        if self.targetPosArr[n]:
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y)
            currentHeading = msg.rot.z # current rotation around the axis

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], currentHeading, lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0

            # set publisher and publish the commands
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 4: ang vel" + str(cmd.angular)) # debug
            publisher.publish(cmd)
    
    def robot5_callback(self, msg: RigidBody):
        n = 5 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        velocity = 0.5 # linear velocity

        if self.targetPosArr[n]:
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y)
            currentHeading = msg.rot.z # current rotation around the axis

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], currentHeading, lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0

            # set publisher and publish the commands
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 5: ang vel" + str(cmd.angular)) # debug
            publisher.publish(cmd)
    
    def robot6_callback(self, msg: RigidBody):
        n = 6 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        velocity = 0.5 # linear velocity

        if self.targetPosArr[n]:
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y)
            currentHeading = msg.rot.z # current rotation around the axis

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], currentHeading, lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0

            # set publisher and publish the commands
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 6: ang vel" + str(cmd.angular)) # debug
            publisher.publish(cmd)
    
    def robot7_callback(self, msg: RigidBody):
        n = 7 # this is the callback for robot n
        lookahead_distance = 1 # lookahead, in number of indeces
        velocity = 0.5 # linear velocity

        if self.targetPosArr[n]:
            # update current position of robot 'n'
            currentPos = (msg.pose.x, msg.pose.y)
            currentHeading = msg.rot.z # current rotation around the axis

            # calculate angle
            angle = pure_pursuit(currentPos, self.targetPosArr[n], currentHeading, lookahead_distance)

            #Purify ang array from NaN values
            if np.isnan(angle) == 1:
                angle = 0

            # set publisher and publish the commands
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 7: ang vel" + str(cmd.angular)) # debug
            publisher.publish(cmd)




def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()