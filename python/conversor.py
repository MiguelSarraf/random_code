import math

#conversores de coordenadas

#conversor de coordenadas retangular para polar
	#coordenada de entrada: x e y
	#coordenadas de sáida polar: r e theta
def cordinates_rect(x, y):
	'''(float, float)->list'''
	res=[]
	r=math.sqrt(x**2+y**2)
	theta=math.atan(y/x)
	res.append((r, theta))
	return res

#conversor de coordenadas polar para retangular
	#coordenada de entrada: r e theta
	#coordenadas de sáida polar: x e y
def cordinates_polar(r, theta):
	'''(float, float)->list'''
	res=[]
	x=r*math.cos(theta)
	y=r*math.sin(theta)
	res.append((x, y))
	return res

#conversores de angulos

#conversor de angulo graus para radiano
	#entrada: thetag
	#saida: thetar
def angle_degree(thetag):
	'''(float)->float'''
	res=[]
	thetar=math.pi*thetag/180
	res.append(thetar)
	return res

#conversor de ngulo radiano para graus
	#entrada: thetar
	#saida:thetag
def angle_rad(thetar):
	'''(float)->float'''
	res=[]
	thetag=thetar*180/math.pi
	res.append(thetag)
	return res