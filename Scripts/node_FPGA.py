#!/usr/bin/env python
import rospy
from Ros.msg import traction_Orders
from Ros.msg import connection
from Ros.msg import arm_Orders
from Ros.msg import RPM
from Ros.msg import corn
from Ros.msg import pots


def traction_Orders_Callback(param):
    pass

def connection_Callback(param):
    pass
def arm_Orders_Callback(param):
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
    # publica en RPM, CORN y POTS
    pub_RPM = rospy.Publisher('topic_RPM', RPM, queue_size=10)
    pub_Corn = rospy.Publisher('topic_Corn', corn, queue_size=10)
    pub_Pots= rospy.Publisher('topic_Pots',pots,queue_size=10)





if __name__ == '__main__':
    try:

        node_FPGA()
    except rospy.ROSInterruptException:
        pass
