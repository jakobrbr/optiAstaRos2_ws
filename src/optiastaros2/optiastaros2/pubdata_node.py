#!/usr/bin/env python3
import rclpy
import timeit
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
            publisher = self.create_publisher(RigidBody, "robot{}/data".format(i), 10)
            self.set_publishers.append(publisher)
            self.get_logger().info("Created publisher #{}".format(i))

        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot1/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot3/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot4/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot5/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot6/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot7/data", 200)
        #self.cmd_vel_pub_ = self.create_publisher(RigidBody, "robot8/data", 200)

        self.timer_ = self.create_timer(0.005, self.send_data)
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
        streamingClient = NatNetClient(ver=(3, 0, 0, 0), quiet=True)
        streamingClient.rigidBodyListener = self.receiveRigidBodyFrame
        streamingClient.run()

        for i, publisher in enumerate(self.set_publishers):
            msg = RigidBody()
            if str(i) in self.id_dict.keys():
                pos,rot = self.id_dict[str(i)]
                # set message values, multiply with 100 to get in cm
                # remember that the ground plane in asta is (x,z)!
                msg.pose.x = pos[0]*100
                msg.pose.y = pos[1]*100
                msg.pose.z = pos[2]*100
                #msg.rot.x = rot[0]
                #msg.rot.y = rot[1]
                #msg.rot.z = rot[2]
                #msg.rigid_body_name = i

                # debug for robot0:
                if str(i) == "0":
                    print("Robot0: " + str(msg.pose.x) + " " + str(msg.pose.y) + " " + str(msg.pose.z))
                if str(i) == "1":
                    print("Robot1: " + str(msg.pose.x) + " " + str(msg.pose.y) + " " + str(msg.pose.z))
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