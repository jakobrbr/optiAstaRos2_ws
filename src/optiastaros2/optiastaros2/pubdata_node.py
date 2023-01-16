#!/usr/bin/env python3
import rclpy
import timeit
import math
from rclpy.node import Node
from rigidbody_msgs.msg import RigidBody
#from geometry_msgs.msg import Pose2D
from NatNetClient import NatNetClient


# the controller crashes if it doesnt recieve any values, so we cant publish at the exact 180z
# we need to be sure we get messages - maybe check with latency calc how fast we can publish here

class PublishDataNode(Node):

    def __init__(self):
        super().__init__("pubdata_node")
        # create 8 publishers, publishing to different topics
        self.set_publishers = []
        for i in range(8):
            publisher = self.create_publisher(RigidBody, "robot{}/data".format(i), 1)
            self.set_publishers.append(publisher)
            self.get_logger().info("Created publisher #{}".format(i))
        
        self.id_dict = dict() # dictionary for positions of rigid bodies

        streamingClient = NatNetClient(ver=(3, 0, 0, 0), quiet=True)
        streamingClient.rigidBodyListener = self.receiveRigidBodyFrame
        streamingClient.run()

        timer_period = 0.01 # motive is 180 fps -> 0.0056 s
        self.timer_ = self.create_timer(timer_period, self.send_data)
        self.get_logger().info("NatNet data publisher node has been started")

    def receiveRigidBodyFrame(self, id, position, rotation):
        self.id_dict[str(id)] = [position,rotation] # update the position and orientation of all robots

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

                publisher.publish(msg)

            if str(i) == "0":
                    print("Robot0 (x,z,roty,rotz): " + str(msg.pose.x) + " " + str(msg.pose.z) + " " + str(msg.rot.y) + " " + str(msg.rot.z))
                    #print("quat: " + str(rot[0]) + str(rot[1]) + str(rot[2]) + str(rot[3]))
            elif str(i) == "1":
                    print("Robot1 (x,z,roty,rotz): " + str(msg.pose.x) + " " + str(msg.pose.z) + " " + str(msg.rot.y) + " " + str(msg.rot.z))


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