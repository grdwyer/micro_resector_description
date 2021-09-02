import os
import yaml
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro
from math import pi


def load_file(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)
    try:
        with open(absolute_file_path, 'r') as file:
            return file.read()
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return None


def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path, 'r') as file:
            return yaml.safe_load(file)
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return None


def generate_launch_description():
    # Component yaml files are grouped in separate namespaces
    package_path = get_package_share_directory('micro_resector_description')
    absolute_file_path = os.path.join(package_path, 'urdf/full_setup.urdf.xacro')
    doc = xacro.process_file(absolute_file_path).toprettyxml(indent='  ')

    robot_description = {'robot_description': doc}
    # RViz
    rviz_config_file = get_package_share_directory('micro_resector_description') + "/launch/urdf.rviz"

    rviz_node = Node(package='rviz2',
                     executable='rviz2',
                     name='rviz2',
                     output='log',
                     arguments=['-d', rviz_config_file],
                     parameters=[robot_description]
                     )

    joint_state_publisher_gui = Node(package='joint_state_publisher_gui',
                                     executable='joint_state_publisher_gui',
                                     name='joint_state_publisher_gui',
                                     parameters=[robot_description]
                                     )
    # Publish TF
    robot_state_publisher = Node(package='robot_state_publisher',
                                 executable='robot_state_publisher',
                                 name='robot_state_publisher',
                                 output='both',
                                 parameters=[robot_description]
                                 )

    return LaunchDescription([robot_state_publisher, rviz_node, joint_state_publisher_gui])
