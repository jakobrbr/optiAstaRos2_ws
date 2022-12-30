#!/usr/bin/env python3
import rclpy
import timeit
from rclpy.node import Node
from rigidbody_msgs import RigidBody
#from geometry_msgs.msg import Pose2D
from NatNetClient import NatNetClient
id_dict = dict() # dictionary for positions of rigid bodies

def receiveRigidBodyFrame(id, position, rotation):
    id_dict[str(id)] = [position,rotation] # update the position and orientation of rigid body

class PublishDataNode(Node):

    def __init__(self):
        super().__init__("pubdata_node")
        self.cmd_vel_pub_ = self.create_publisher(RigidBody, "/data", 10)
        self.timer_ = self.create_timer(0.005, self.send_data)
        self.get_logger().info("NatNet data publisher node has been started")

    def send_data(self):
        streamingClient = NatNetClient(ver=(3, 0, 0, 0), quiet=True)
        streamingClient.rigidBodyListener = receiveRigidBodyFrame
        streamingClient.run()
        msg = RigidBody()
        for i in id_dict.keys():
            pos,rot = id_dict[i]
            msg.pose.x = pos[0]
            msg.pose.y = pos[1]
            msg.pose.z = pos[2]
            msg.rot.x = rot[0]
            msg.rot.y = rot[1]
            msg.rot.z = rot[2]
            msg.rigid_body_name = i
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PublishDataNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()