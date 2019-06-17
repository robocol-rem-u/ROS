#!/usr/bin/env python
#Se importan las librerias necesarias junto con los mensajes a utilizar
import rospy

def nodoIMU()
	# Se inicia el nodo de odometria
	rospy.init_node ('nodoIMU', anonymous=True)
	


# Metodo principal, crea el nodo de ROS, se suscribe a topico de informacion obstaculos e imprime su informacion
# mientras que el nodo se este ejecutando
if __name__ == '__main__':
    try:
    	nodoIMU()
        rate = rospy.Rate (10)
        while not rospy.is_shutdown ():
            rate.sleep ()
    except rospy.ROSInterruptException:
        pass