#!/usr/bin/env python
import rospy
from ROS.msg import traction_Orders
from ROS.msg import connection
from ROS.msg import arm_Orders
from ROS.msg import RPM
from ROS.msg import current
from ROS.msg import pots
from ROS.msg import sensibility

def traction_Orders_Callback(param):
    pass

def connection_Callback(param):
    pass
def arm_Orders_Callback(param):
    pass
def sensibility_Callback(param):
    pass

def node_FPGA():
    #creacion del nodo
    rospy.init_node('node_FPGA',anonymous=True)

    #se subscribe al topico traction orders
    rospy.Subscriber ('topic_Traction_Orders', traction_Orders, traction_Orders_Callback)
    #se subscribe al topico connection
    rospy.Subscriber ('topic_Connection', connection, connection_Callback)
    # se subscribe al topico Arm Orders
    rospy.Subscriber ('topic_Arm_Orders', arm_Orders, arm_Orders_Callback)
    #se subscribe a sensibility
    rospy.Subscriber ('topic_Sensibility', sensibility, sensibility_Callback)   
    # publica en RPM, Current y POTS
    pub_RPM = rospy.Publisher('topic_RPM', RPM, queue_size=10)
    pub_Current = rospy.Publisher('topic_Current', current, queue_size=10)
    pub_Pots= rospy.Publisher('topic_Pots',pots,queue_size=10)
    rate = rospy.Rate (10)
    while not rospy.is_shutdown ():
        rate.sleep ()





if __name__ == '__main__':
    try:

        node_FPGA()

    except rospy.ROSInterruptException:
        pass
