#!/usr/bin/env python
import rospy


def node_Interface():
    rospy.init_node('nodoInterface',anonymous=True)






if __name__ == '__main__':
    try:

        node_Interface()
    except rospy.ROSInterruptException:
        pass
