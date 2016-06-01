#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='emilio',passwd='crom', db='DBdeEmilio')

# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# Creamos variables
for i in range(2):
	while True:
		nombre = raw_input('Introduce el nombre: ')
		profesion = raw_input('Introduce la profesion: ')
		muerte = raw_input('Introduce la muerte: ')
		
		if nombre == "" or profesion == "" or muerte == "":
			print "No puede dejar campos vacíos. Inténtelo de nuevo."
		else:
			q = "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+ str(i+1) +",\"" + nombre + "\", \"" + profesion + "\",\"" + muerte +"\");"
			micursor.execute(q)
			Conexion.commit()
			break

query = "SELECT * FROM Victimas"
micursor.execute(query)
registros = micursor.fetchall()

for registro in registros:
	print registro["Nombre"] + " es del tipo " + registro["Profesion"]
