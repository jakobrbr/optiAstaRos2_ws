import rclpy
from rclpy.node import Node
from std_msgs.msg import String
# This node is used to test the latency when sending a message wirelessly 
# from Raspberry Pi to ESP32 using ROS2-microROS

class LatencyTester(Node):

    def __init__(self):
        super().__init__('latency_tester')
        self.publisher_ = self.create_publisher(String, 'latency_topic', 10)
        timer_period = 0.1  # s
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.sent_time = None

    def timer_callback(self):
        msg = String()
        msg.data = "ping"
        self.sent_time = self.get_clock().now().nanoseconds
        self.publisher_.publish(msg)

    def latency_callback(self, msg):
        receive_time = self.get_clock().now().nanoseconds
        latency = receive_time - self.sent_time
        self.get_logger().info("Latency: {} ns".format(latency))

def main(args=None):
    rclpy.init(args=args)

    latency_tester = LatencyTester()

    rclpy.spin(latency_tester)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    latency_tester.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
