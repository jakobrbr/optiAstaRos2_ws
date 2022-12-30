#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rigidbody_msgs.msg import RigidBody

class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller_node")
        self.controller_node_ = self.create_subscription(RigidBody, "/data", self.pose_callback, 200)

    def pose_callback(self, msg: RigidBody):
        self.get_logger().info(str(msg.pose.x))

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()