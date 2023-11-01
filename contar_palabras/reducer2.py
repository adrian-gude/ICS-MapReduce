#!/usr/bin/env python

#######################################################################
# Reduce.py							                                  #
#								                                      #
# Este programa lee el STDIN que recibe de Map.py y va sumarizando    #
# por cada clave (palabra) para escribir su frecuencia de aparicion   #
# El output de este programa son las palabras que recibe de Map.py    #
# sin repetirse seguidas de un tab y el valor de su frecuencia.       #
#																	  #
# Output: palabra\tfrecuencia		                                  #
#	  ej: foo	4                                                     #
# 	      raul	2					                                  #
#######################################################################

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input viene desde el STDIN
for line in sys.stdin:
	# Elimina los espacios atras y adelante de la linea.
	line = line.strip()

	# divide el input recibido desde map.py
	word, count = line.split('\t', 1)

	# Convierte count (de momento un string) a int
	try:
		count = int(count)
	except ValueError:
		# count no es un numero
		# ignorar/descartar esta linea.
		continue

	# Esto funciona porque hadoop ordena map output
	# por key (o sea, word) antes de pasarlo al reducer
	if current_word == word:
		current_count += count
	else:
		if current_word:
			# Escribe el resultado en el STDOUT
			print '%s\t%s' % (current_word, current_count)
		current_count = count
		current_word = word

# no olvidar el output de la ultima palabra!
if current_word == word:
	print '%s\t%s' % (current_word, current_count)