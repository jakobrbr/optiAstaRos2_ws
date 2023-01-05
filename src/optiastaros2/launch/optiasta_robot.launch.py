from launch import LaunchDescription
from launch_ros.actions import Node

#from launch.actions import DeclareLaunchArgument
#from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='optiastaros2', executable='pubdata_node', namespace='robot1', output='screen'),
        Node(
            package='optiastaros2', executable='controller_node', namespace='robot1', output='screen'),
    ])