#-*- coding: utf-8 -*-
import random
import time
import sys
print " "
print "\t\t\t\t....................................................................."
print "\t\t\t\t............................BIENVENDIDO A............................"
print "\t\t\t\t........................¡Adivina un Número!!!........................"
print "\t\t\t\t....................................................................."
print " "
print " "
print "El objetivo del juego es el siguiente:"
print " "
print "--- El sistema generará automaticamente números al azar, del cual, tendras que ingresar un número entero entre los rangos 0 y 10 para adivinar el que el sistema genera---"
print " "
print "Bueno. Pues a ¡Jugar se ha dicho!"
print " "
print "¿Estás listo?"
print " "
listo = True
while listo==True:
	print "Ingresa 'y' si lo estás y 'n' si no lo estás y salir"
	preg = raw_input("Escribe 'y' o 'n':   ")
	print " "
	contador = 0
	num_aleatorio = random.randint(0,10)
	if preg.lower()=="y":
		print "Ok. Cuentas con 5 intentos. ¡No los Desperdicies!"
		print " "
		while contador < 5:
			try:
				contador = contador + 1
				numero = raw_input("Elige un número del 1 al 10: ")
				numero = int(numero)
				print " "
				print "Procesando... Que tengas suerte!"
				print " "
				time.sleep(2) 
				if numero < num_aleatorio:
					print ("→→→ Tu número es mas bajo que el generado por el sistema. Ya que el sistema obtuvo " + str(num_aleatorio))
					print "Intentalo de nuevo"
					print " "
				if numero > num_aleatorio:
					print ("→→→ Tu número es mas alto que el generado por el sistema. Ya que el sistema obtuvo " + str(num_aleatorio))
					print " "
			except ValueError,NameError:
				print "***Error Solo se pueden Ingresar Números***"
				print " "

		if numero == num_aleatorio:
				print ("¡WoWEres un genio....!")
				print " "
				print ( " lo lograste con %d intentos" % (contador))
				break

		if numero != num_aleatorio:
			print ("Has perdido. xS será en otra ocasión.")
			print "Saliedo....."
			break
			sys.exit(4)
	elif preg.lower()=="n":
		listo == False
	else:
		print "No es una respuesta correcta. ¡Intentalo de Nuevo!"