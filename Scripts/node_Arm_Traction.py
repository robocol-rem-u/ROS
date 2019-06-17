#!/usr/bin/env python
import rospy


def node_Arm_Traction():
    rospy.init_node('node_Arm_Traction',anonymous=True)






if __name__ == '__main__':
    try:

        node_Arm_Traction()
    except rospy.ROSInterruptException:
        pass
