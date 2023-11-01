#!/usr/bin/python

#####################################################################
# Map.py							      #	                                                 #                                                                     #
#                                                                     #
# Este programa lee el STDIN, por cada linea elimina los espacios     #
# iniciales y traseros, luego elimina todos los simbolos y convierte  #
# las palabras a minusculas. Luego se queda con cada una de las       #
# palabras que componen la linea; y por cada palabra imprime una      #
# linea con la palabra seguida de un tab y un 1.                      #
#								      #
# Output: palabra\t1	       					      #
#	  ej: foo	1                                             #
# 	      foo	1					      #
####################################################################

import sys
import re

# input viene desde el STDIN (standard input)
for line in sys.stdin:
	# Elimina los espacios atras y adelante de la linea.
	line = line.strip()
	# Elimina los puntos, comas y demas simbolos no alfanumericos.
	line = re.sub(r'[^\w]', ' ', line)
	# Elimina todos los numeros para quedarme solo con las palabras.
	line = re.sub('\d+', ' ', line)
	# Convierte toda la linea a minusculas.
	line = line.lower()
	# Divide la linea en palabras.
	words = line.split()
	# Incrementa la cuenta.
	for word in words:
		# Escribe el resultado en STDOUT (standard output);
		# delimitado por un tab.
		# Este output va a ser el input para la funcion reduce.
		print '%s\t%s' % (word, 1)