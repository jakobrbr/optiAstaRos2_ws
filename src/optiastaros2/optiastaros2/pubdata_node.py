#!/usr/bin/env python3
import rclpy
import timeit
import math
from rclpy.node import Node
from rigidbody_msgs.msg import RigidBody
#from geometry_msgs.msg import Pose2D
from NatNetClient import NatNetClient

class PublishDataNode(Node):

    def __init__(self):
        super().__init__("pubdata_node")
        # create 8 publishers, publishing to different topics
        self.set_publishers = []
        self.id_dict = dict() # dictionary for positions of rigid bodies
        for i in range(8):
            publisher = self.create_publisher(RigidBody, "robot{}/data".format(i), 1)
            self.set_publishers.append(publisher)
            self.get_logger().info("Created publisher #{}".format(i))

        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot1/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot3/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot4/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot5/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot6/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot7/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot8/data", 200)
        streamingClient = NatNetClient(ver=(3, 0, 0, 0), quiet=True)
        streamingClient.rigidBodyListener = self.receiveRigidBodyFrame
        streamingClient.run()
        self.timer_ = self.create_timer(0.01, self.send_data) #0.001 or 0.01
        self.get_logger().info("NatNet data publisher node has been started")

    def receiveRigidBodyFrame(self, id, position, rotation):
        #id_dict[str(id)] = [position,rotation] # update the position and orientation of rigid body
        self.id_dict = {(str(id)):[position,rotation]} # update the position and orientation of robot
        # Optitrack client
        #pos,rot = self.id_dict[str(id)]
        #print("id: %s" % str(id))
        #print("pos: {0}".format(pos))
        #print("rot: {0}".format(rot))

    def send_data(self):
        for i, publisher in enumerate(self.set_publishers):
            msg = RigidBody()
            if str(i) in self.id_dict.keys():
                # the ground plane in asta is either (x,y) or (x,z) depending on motive settings,
                # and we are given axis rotation in quaternion

                pos,rot = self.id_dict[str(i)]

                # set positions to publish (multiply w. 100 to get in cm):
                msg.pose.x = pos[0]*100
                msg.pose.y = pos[1]*100
                msg.pose.z = pos[2]*100
                #msg.rigid_body_name = i

                # convert from quaternions to radians and set z and y rotation (depending on motive settings):
                msg.rot.y = math.atan2(2*(rot[3]*rot[1]+rot[0]*rot[2]), 1-2*(rot[1]*rot[1]+rot[0]*rot[0]))
                msg.rot.z = math.atan2(2*(rot[3]*rot[2]+rot[0]*rot[1]), 1-2*(rot[2]*rot[2]+rot[0]*rot[0]))


                # debug for robot0:
                if str(i) == "0":
                    print("Robot0 (x,z,roty,rotz): " + str(msg.pose.x) + " " + str(msg.pose.z) + " " + str(msg.rot.y) + " " + str(msg.rot.z))
                    #print("quat: " + str(rot[0]) + str(rot[1]) + str(rot[2]) + str(rot[3]))
                elif str(i) == "1":
                    print("Robot1 (x,z,rot): " + str(msg.pose.x) + " " + str(msg.pose.z) + " " + str(msg.rot.y))
                publisher.publish(msg)


        #msg = RigidBody()
        #for i in id_dict.keys():
            #pos,rot = id_dict[i]
            #msg.pose.x = pos[0]
            #msg.pose.y = pos[1]
            #msg.pose.z = pos[2]
            #msg.rot.x = rot[0]
            #msg.rot.y = rot[1]
            #msg.rot.z = rot[2]
            #msg.rigid_body_name = i
        #self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PublishDataNode()
    rclpy.spin(node)
    # destroy timer?
    rclpy.shutdown()


if __name__ == '__main__':
    main()