import os
import launch
import launch_ros.actions
from launch_ros.substitutions import FindPackageShare
import xacro

def generate_launch_description():
    pkg_share = FindPackageShare('khan_description').find('khan_description')

    urdf_file = os.path.join(pkg_share, 'urdf', 'description.xacro')
    urdf_processed = xacro.process_file(urdf_file)

    rsp = launch_ros.actions.Node(package='robot_state_publisher',
                                  executable='robot_state_publisher',
                                  output='both',
                                  parameters=[
                                      {"robot_description": urdf_processed.toxml()},
                                      {"publish_frequency": 50.0}
                                  ])
    return launch.LaunchDescription([rsp])