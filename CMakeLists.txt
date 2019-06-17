cmake_minimum_required(VERSION 2.8.3)
project(ROS)
find_package(catkin REQUIRED 
  roscpp 
  rospy 
  std_msgs 
  geometry_msgs
  message_generation
)
catkin_package(
  CATKIN_DEPENDS 
  message_runtime
  roscpp
  rospy
  std_msgs
  geometry_msgs
)

add_message_files(
  FILES
  arm_Orders.msg
  connection.msg
  corn.msg
  goal.msg
  IMU_Magnetism.msg
  IMU_Speed.msg
  position.msg
  pots.msg
  RPM.msg
  traction_Orders.msg
)
add_service_files(
  FILES
  enable.srv
)
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )
