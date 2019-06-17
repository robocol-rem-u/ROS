#!/usr/bin/env python
import rospy


def nodoFPGA():
    rospy.init_node('nodoFPGA',anonymous=True)






if __name__ == '__main__':
    try:

        nodoFPGA()
    except rospy.ROSInterruptException:
        pass
