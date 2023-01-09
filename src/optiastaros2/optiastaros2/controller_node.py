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
    # Kill node when we reach the end
    # create a launch directiory and file!
    # lav egen fortolkning af dansen ift robottens begræsninger, det er ikke ideelt at lave præcise menneskelige bevægelser for en robot
    # skriv et afsnit om vores valg der og find andre folks papers om dans/menneskelig bevægelse af robotter
    # med vores styring er det svært, men man kunne lave dansen ved at give kommandoer og koordinater
    # Vi tegner for at bedre visualisere osv
    # pure pursuit giver flydende bevægelser
    # den kører bedre med mange punkter

    # regulated pure pursuit (with velocity controller)
    # weighted pure pursuit (choose path with least angle change if at crossroad)
    
    # afstand mellem to linjer må ikke være mindre end afstanden mellem linjepunkterne

    # vi kan muligvis først teste om det virker med flere når vi er i optitrack
    # saml 8 pcb'er og vis at kommunikationen er hurtig nok, brug to robotter til at demonstrere synkronitet

    # test branch?: publish commands using the Twist message
    # send stop command to robot before we shut the nodes off, otherwise it will continue

    # limit publishing speed, so we dont update so often

class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller_node")

        """
        # init new sub for 8 robots, uncomment for 1 robot:
        self.sub_array = [] 
        for i in range(8): # create 8 subscribers, one for each robot data topic
            self.sub_array.append(self.create_subscription(RigidBody, "/robot{}/data".format(i), self.pose_callback, i)) # hvorfor er der et i til sidst??
        # end of 8 robot sub init
        """
        # old sub for 1 robot, uncomment for 8 robots:
        self.controller_node_ = self.create_subscription(RigidBody, "/robot0/data", self.pose_callback, 1)

        # new pub for 8 robots
        self.set_publishers = []
        for i in range(8): # create 8 publishers to topic "/cmd_vel"
            publisher = self.create_publisher(RobotCmd, "/robot{}/cmd_vel".format(i), 10)
            self.set_publishers.append(publisher)
        # end of init for 1 robot


        # initialize arrays
        self.msg_array = [None]*8 # kunne også være en array med 8 nuller
        self.currentPos = [None]*8 # should become array of tuples 
        self.last_angle = [0,0,0,0,0,0,0,0]
        self.angle = [0,0,0,0,0,0,0,0]
        self.velocity = [0,0,0,0,0,0,0,0]

        
        # import svg file
        svg_file_path = input("Write path to route svg: (e.g. heart.svg)\n")
        with open(svg_file_path, "r") as f:
            # Read the contents of the file into a string variable
            svg_path = f.read()
        svg_str = minidom.parseString(svg_path)

        # generate path from svg file
        self.targetPosArr, stop_pos, stop_orient = (generateRobotPath.pointsFromDoc(svg_str,density=0.1, scale=1))

        self.start_time = np.floor(time.time())
        self.lap_time = np.floor(time.time()) + 180

        self.get_logger().info("Controller node has been started")


    # This is the temporary callback function that only works for one robot, uncomment for more robots
    def pose_callback(self, msg: RigidBody):
        # this function is called whenever we get data from optitrack
        # Apply pure pursuit algorithm to get target angle and velocity values for each robot
        for j in range(0,len(self.targetPosArr)):
            if self.targetPosArr[j]:
                # update current position of robot 'j'

                self.currentPos[j] = (msg.pose.x, msg.pose.z) # this array of tuples (8x2) should contain the coordinates of all 8 robots 
                currentHeading = msg.rot.y # current roation around y axis

                # calculate angle
                self.angle[j] = pure_pursuit(self.currentPos[j],self.targetPosArr[j], currentHeading, max_angular_velocity=1, lookahead_distance = 4) # lookahead is in indeces
                #Purify ang array from NaN values
                if np.isnan(self.angle[j]) == 1:
                    self.angle[j] = 0
                    #print("angle : {}".format(angle[j]))
                    #print("current posistion : {}".format(turt[j].pos))
                    #print("target position : {}".format(targetPosArr[0][j+1]))

                #self.velocity[j] = velocity_controller(self.currentPos[j],self.targetPosArr[j],self.start_time,self.lap_time, 1) # for constant velocity set: velocyty = 1 
                self.velocity[j] = 1.0 # constant low velocity, maybe set to 1 again or 0.3
                #self.velocity[j] *= pure_pursuit_turn_speed(self.last_angle[j],self.angle[j]) # turn controller

                #print("velocity : {}".format(velocity[j]))

                for i, publisher in enumerate(self.set_publishers):
                    cmd = RobotCmd()
                    cmd.linear = self.velocity[j]
                    cmd.angular = self.angle[j]
                    #cmd.rigid_body_name = msg.rigid_body_name # we dont need to publish the name
                    publisher.publish(cmd)
                #print("vel and angle:" + str(cmd.linear) + " " + str(cmd.angular))
                # update last angle
                self.last_angle = self.angle

        # test print
        #print("natnet data (x,y): " + str(msg.pose.x) + str(msg.pose.y))
        self.get_logger().info("vel and angle:" + str(cmd.linear) + " " + str(cmd.angular))


"""
    # This is the callback function where we should sub and pub for 8 robots, rewrite this so it works!
    def pose_callback(self, msg: RigidBody):
        # this function is called whenever we get data from optitrack

        # Apply pure pursuit algorithm to get target angle and velocity values for each robot
        for j in range(0,len(self.targetPosArr)):
            if self.targetPosArr[j]:
                    # update current position of robot 'j'
                    # msg array is an array of two elements; x and y??
                    self.msg_array[j] = self.sub_array[j] # sådan her??
                    self.currentPos[j] = (self.msg_array[j],)

                    self.currentPos[j] = (msg.pose.x, msg.pose.y) # this array of tuples (8x2) should contain the coordinates of all 8 robots 

                    # calculate angle
                    self.angle[j] = pure_pursuit(self.currentPos[j],self.targetPosArr[j], lookahead_distance=5)
                    #Purify ang array from NaN values
                    if np.isnan(self.angle[j]) == 1:
                        self.angle[j] = 0
                    #print("angle : {}".format(angle[j]))
                    #print("current posistion : {}".format(turt[j].pos))
                    #print("target position : {}".format(targetPosArr[0][j+1]))

                    self.velocity[j] = proportional_velocity_controller(self.currentPos[j],self.targetPosArr[j],self.start_time,self.lap_time) # for constant velocity set: velocyty = 1 
                    self.velocity[j] *= pure_pursuit_turn_speed(self.last_angle[j],self.angle[j]) # turn controller

                    #print("velocity : {}".format(velocity[j]))

                    # set target values and publish to each robot
                        # we should use the i somehow when we publish, right??
                    for i, publisher in enumerate(self.set_publishers):
                        cmd = RobotCmd()
                        cmd.linear = self.velocity[j]
                        cmd.angular = self.angle[j]
                        #cmd.rigid_body_name = msg.rigid_body_name # we dont need to publish the name
                        publisher.publish(cmd)
                    
                    # try to use the same thing in the subscriber as we do here in the subscriber^^ something like "subscriber.subscrive(msg)" --------------

                    # update last angle
                    self.last_angle = self.angle
                    #currentPos[j] = turt[j].pos() # move robot, the optitrack system should do this part in the future
                    #last_angle[j] = angle[j] # Sets the new angle, the optitrack system should do this part in the futures
        # test print
        #self.get_logger().info("vel and angle:" + str(cmd.linear) + " " + str(cmd.angular))
"""


def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()