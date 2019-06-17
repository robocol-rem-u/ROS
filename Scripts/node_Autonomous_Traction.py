#!/usr/bin/env python
import rospy


def node_Autonomous_Traction():
    rospy.init_node('node_Autonomous_Traction',anonymous=True)
    



if __name__ == '__main__':
    try:

        node_Autonomous_Traction()
    except rospy.ROSInterruptException:
        pass