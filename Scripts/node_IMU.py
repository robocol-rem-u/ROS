#!/usr/bin/env python
#Se importan las librerias necesarias junto con los mensajes a utilizar
import rospy
from ROS.msg import IMU_Speed
from ROS.msg import IMU_Magnetism



def node_IMU():
	# Se inicia el nodo de odometria
    rospy.init_node ('node_IMU', anonymous=True)
    # Se publica al topico sobre la velocidad segun IMU
    pub_IMU_Speed = rospy.Publisher ('topic_IMU_Speed', IMU_Speed, queue_size=10)
    # Se publica al topico sobre la velocidad segun IMU
    pub_IMU_Magnetism = rospy.Publisher ('topic_IMU_Magnetism', IMU_Magnetism, queue_size=10)
    rate = rospy.Rate (10)
    while not rospy.is_shutdown ():
        rate.sleep ()

# Metodo principal, crea el nodo de ROS, se suscribe a topico de informacion obstaculos e imprime su informacion
# mientras que el nodo se este ejecutando
if __name__ == '__main__':
    try:
    	node_IMU()
    except rospy.ROSInterruptException:
        pass
