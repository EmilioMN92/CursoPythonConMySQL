#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='emilio',passwd='crom', db='DBdeEmilio')

# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# Creamos variables
for i in range(10):
	nombre = input('Introduce el nombre: ')
	profesion = input('Introduce la profesion: ')
	muerte = input('Introduce la muerte: ')
	q = "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1,\"" + nombre + "\", \"" + profesion + "\",\"" + muerte +"\");"
	print q
	#micursor.execute(q)

