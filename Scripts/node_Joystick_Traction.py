#!/usr/bin/env python
import rospy


def nodoTraccionJoystick():
    rospy.init_node('nodoTraccionJoystick',anonymous=True)
    





if __name__ == '__main__':
    try:
       
        nodoTraccionJoystick()
    except rospy.ROSInterruptException:
        pass
