#!/usr/bin/env python
import rospy
from ROS.msg import traction_Orders


def node_Joystick_Traction():
    rospy.init_node('node_Joystick_Traction',anonymous=True)
    

    #publica en el topico traction orders
    pub_Traction_Orders = rospy.Publisher('topic_Traction_Orders', traction_Orders, queue_size=10)


if __name__ == '__main__':
    try:
       
        node_Joystick_Traction()
    except rospy.ROSInterruptException:
        pass
