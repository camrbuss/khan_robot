cmake_minimum_required(VERSION 3.5)
project(khan_control)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(hardware_interface REQUIRED)
find_package(controller_manager REQUIRED)
find_package(transmission_interface REQUIRED)
find_package(control_toolbox REQUIRED)
find_package(urdf REQUIRED)

# This package needs significant modification to interface with
# ros2_control and its arch changes

# Using std mutex instead of Boost

# add_library(khan_hwintf src/KHANHWInterface.cpp)
# target_include_directories(khan_hwintf PUBLIC
#   $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#   $<INSTALL_INTERFACE:include>)
# ament_target_dependencies(khan_hwintf
#   rclcpp
#   sensor_msgs
#   hardware_interface
#   controller_manager
#   transmission_interface
#   control_toolbox)

# add_executable(khan_control src/KHANPythonControl.cpp)
# target_include_directories(khan_control PUBLIC
#   $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#   $<INSTALL_INTERFACE:include>)
# ament_target_dependencies(khan_control rclcpp controller_manager)
# target_link_libraries(khan_control khan_hwintf)

# install(TARGETS khan_hwintf khan_control
#   ARCHIVE DESTINATION lib
#   LIBRARY DESTINATION lib
#   RUNTIME DESTINATION bin
# )

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
