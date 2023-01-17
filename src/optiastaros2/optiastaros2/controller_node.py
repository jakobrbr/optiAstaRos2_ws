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

    # check if the scaling between lin vel and ang vel is wrong (check units) - maybe set higher lin vel or multtply with something

    # add function to microros to light up blue and green leds on pcb

    # which queue size to use? use the same on everything?
    # pwm frequency and resolution fits with out clock cycle of xx mhz?

    # sæt framerate i motive op?

    # nyt batteri i den gule?


    # constrain angular velocity mere
    # mindre 

    # slet build mappen fra github workspace

class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller_node")
        
        # init sub for 8 robots:
        self.create_subscription(RigidBody, "/robot0/data", self.robot0_callback, 1)
        #self.create_subscription(RigidBody, "/robot1/data", self.robot1_callback, 1)
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

        # import svg file
        svg_file_path = input("Write path to route svg: (e.g. heart.svg)\n")
        with open(svg_file_path, "r") as f:
            # Read the contents of the file into a string variable
            svg_path = f.read()
        svg_str = minidom.parseString(svg_path)
        

        # generate path from svg file
        self.targetPosArr, stop_pos, stop_orient = (generateRobotPath.pointsFromDoc(svg_str,density=0.1, scale=1)) # set density and scale of path


        self.start_time = np.floor(time.time())
        self.lap_time = np.floor(time.time()) + 180

        self.get_logger().info("Controller node has been started")

    def map_value(self, val, in_min, in_max, out_min, out_max):
        #return (( (val - in_min) / (in_max - in_min) ) * (out_max - out_min) + out_min)
        return ((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    def robot0_callback(self, msg: RigidBody):
        n = 0 # this is the callback for robot n
        lookahead_distance = 24 # lookahead, in number of indeces
        velocity = 1.0 # constant linear velocity, should be float!

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

            # set publisher and publish the commands (we dont need to publish the name)
            publisher = self.set_publishers[n]
            cmd = RobotCmd()
            cmd.linear = velocity
            cmd.angular = angle
            self.get_logger().info("robot 0: ang vel" + str(cmd.angular))
            #self.get_logger().info("robot 0: ang" + str(unwrapped_heading[-1]))
            publisher.publish(cmd)
    
    def robot1_callback(self, msg: RigidBody):
        n = 1 # this is the callback for robot n
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
            self.get_logger().info("robot 1: ang vel" + str(cmd.angular)) # debug
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

"""
    # This is the temporary callback function that only works for one robot
    def pose_callback(self, msg: RigidBody):
        # this function is called whenever we get data from optitrack
        # Apply pure pursuit algorithm to get target angle and velocity values for each robot
        for j in range(0,len(self.targetPosArr)):
            if self.targetPosArr[j]:
                # update current position of robot 'j'

                self.currentPos[j] = (msg.pose.x, msg.pose.y) # this array of tuples (8x2) should contain the coordinates of all 8 robots 
                currentHeading = msg.rot.z # current rotation around the axis

                # calculate angle
                self.angle[j] = pure_pursuit(self.currentPos[j],self.targetPosArr[j], currentHeading, lookahead_distance = 5) # lookahead is in indeces
                #Purify ang array from NaN values
                if np.isnan(self.angle[j]) == 1:
                    self.angle[j] = 0
                    #print("angle : {}".format(angle[j]))
                    #print("current posistion : {}".format(turt[j].pos))
                    #print("target position : {}".format(targetPosArr[0][j+1]))
                #self.velocity[j] = velocity_controller(self.currentPos[j],self.targetPosArr[j],self.start_time,self.lap_time, 1) # for constant velocity set: velocyty = 1 


                self.velocity[j] = 1.0 # constant low linear velocity, maybe set to 1 again or 0.5


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
"""



def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()