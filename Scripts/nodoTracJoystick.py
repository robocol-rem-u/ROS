#!/usr/bin/env python
import rospy


def nodoTracJoystick():
    rospy.init_node('nodoTracJoystick',anonymous=True)
    





if __name__ == '__main__':
    try:
       
        nodoTracJoystick()
    except rospy.ROSInterruptException:
        pass