#!/usr/bin/env python
import rospy


def nodoInterface():
    rospy.init_node('nodoInterface',anonymous=True)






if __name__ == '__main__':
    try:

        nodoInterface()
    except rospy.ROSInterruptException:
        pass
