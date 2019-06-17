#!/usr/bin/env python
import rospy


def node_XBEE_pc():
    rospy.init_node('node_XBEE_pc', anonymous=True)


if __name__ == '__main__':
    try:

        node_XBEE_pc()
    except rospy.ROSInterruptException:
        pass