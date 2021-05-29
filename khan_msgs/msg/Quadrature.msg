# Message representing Quadrature Encoder data, for testing/exploring
# quadrature encoding. Normally this wouldn't be sent over ROS topics in
# a real system, but this is useful as a learning example of both ROS
# pub/sub and quadrature encoding.
# Author: Jason Ziglar <jpz@vt.edu>
std_msgs/Header header
bool state_a
bool state_b