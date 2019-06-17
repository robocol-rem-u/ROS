#!/usr/bin/env python
import rospy


def nodoTraccionBrazo():
    rospy.init_node('nodoTraccionBrazo',anonymous=True)






if __name__ == '__main__':
    try:

        nodoTraccionBrazo()
    except rospy.ROSInterruptException:
        pass
