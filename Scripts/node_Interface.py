#!/usr/bin/env python
import rospy
from ROS.msg import traction_Orders, IMU_Speed, IMU_Magnetism, pots, corn, RPM, arm_Orders, goal, connection

def node_Interface():
    rospy.init_node('node_Interface',anonymous=True)
    rospy.Subscriber('topic_Traction_Orders', traction_Orders, traction_Orders_Callback)
    rospy.Subscriber('topic_IMU_Speed', IMU_Speed, IMU_Speed_Callback)
    rospy.Subscriber('topic_IMU_Magnetism', IMU_Magnetism, IMU_Magnetism_Callback)
    rospy.Subscriber('topic_Pots', pots, pots_Callback)
    rospy.Subscriber('topic_Corn', corn, corn_Callback)
    rospy.Subscriber('topic_RPM', RPM, RPM_Callback)
    rospy.Subscriber('topic_Arm_Orders', arm_Orders, arm_Orders_Callback)
    pub_Goal = rospy.Publisher('topic_Goal', goal, queue_size=10)
    pub_Arm_Orders = rospy.Publisher('topic_Arm_Orders', arm_Orders, queue_size=10)
    pub_Connection = rospy.Publisher('topic_Connection', connection, queue_size=10)
    pub_Traction_Orders = rospy.Publisher('topic_Traction_Orders', traction_Orders, queue_size=10)


def traction_Orders_Callback(param):
    pass

def IMU_Speed_Callback(param):
    pass

def IMU_Magnetism_Callback(param):
    pass

def pots_Callback(param):
    pass

def corn_Callback(param):
    pass

def RPM_Callback(param):
    pass

def arm_Orders_Callback(param):
    pass


if __name__ == '__main__':
    try:

        node_Interface()
    except rospy.ROSInterruptException:
        pass
