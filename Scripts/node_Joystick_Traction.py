#!/usr/bin/env python
import rospy


def node_Joystick_Traction():
    rospy.init_node('node_Joystick_Traction',anonymous=True)
    





if __name__ == '__main__':
    try:
       
        node_Joystick_Traction()
    except rospy.ROSInterruptException:
        pass
