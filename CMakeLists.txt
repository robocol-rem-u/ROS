cmake_minimum_required(VERSION 2.8.3)
project(ROS)
find_package(catkin REQUIRED 
  roscpp 
  rospy 
  std_msgs 
  geometry_msgs
  message_generation
)

add_message_files(
  FILES
  arm_Orders.msg
  connection.msg
  current.msg
  goal.msg
  IMU_Magnetism.msg
  IMU_Speed.msg
  position.msg
  pots.msg
  RPM.msg
  traction_Orders.msg
)

#add_service_files(
#  FILES
#  enable.srv
#)

generate_messages(
    DEPENDENCIES
    std_msgs
)


catkin_package(
  CATKIN_DEPENDS 
  message_runtime
  roscpp
  rospy
  std_msgs
  geometry_msgs
)


# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )


