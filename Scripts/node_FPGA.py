#!/usr/bin/env python
import rospy


def node_FPGA():
    rospy.init_node('node_FPGA',anonymous=True)






if __name__ == '__main__':
    try:

        node_FPGA()
    except rospy.ROSInterruptException:
        pass
