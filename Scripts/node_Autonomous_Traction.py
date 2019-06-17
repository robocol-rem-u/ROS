#!/usr/bin/env python
import rospy


def nodoAutonomoTraccion():
    rospy.init_node('nodoAutonomoTraccion',anonymous=True)
    





if __name__ == '__main__':
    try:
       
        nodoAutonomoTraccion()
    except rospy.ROSInterruptException:
        pass