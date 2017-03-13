#función que convierte un numero en un string de tamaño igual al numero de interaciones
def StringNum(num):
	try:
		res=""
		for i in range(num):
			res+="n"
		return res

	except TypeError:
		num=int(num)
		res=""
		for i in range(num):
			res+="n"
		return res