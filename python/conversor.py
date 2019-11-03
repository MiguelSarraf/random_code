import math

#conversores de coordenadas

#conversor de coordenadas retangular para polar, eliptica
	#coordenada de entrada: x, y e a
	#coordenadas de sáida polar: r e theta
	#coordenadas de saóda eliptica: mu e nu
def cordinates_rect(x, y, a=1):
	'''(float, float)->list'''
	res=[]
	#polar
	r=math.sqrt(x**2+y**2)
	theta=math.atan(y/x)
	res.append((r, theta))
	#eliptica
	k=math.sqrt((x-a)**2+y**2)+math.sqrt((x+a)**2+y**2)
	mu=math.acosh(k/(2*a))
	nu=math.acos(x/(a*math.cosh(mu)))
	res.append((mu, nu))
	return res

#conversor de coordenadas polar para retangular, eliptica
	#coordenada de entrada: r, theta e a
	#coordenadas de sáida retangular: x e y
	#coordenadas de saída eliptica: mu e nu
def cordinates_polar(r, theta, a=1):
	'''(float, float)->list'''
	res=[]
	#cartesiana
	x=r*math.cos(theta)
	y=r*math.sin(theta)
	res.append((x, y))
	#eliptica
	k=math.sqrt((x-a)**2+y**2)+math.sqrt((x+a)**2+y**2)
	mu=math.acosh(k/(2*a))
	nu=math.acos(x/(a*math.cosh(mu)))
	res.append((mu, nu))
	return res

#conversor de coordenadas eliptica para retangular, polar
	#coordenada de entrada: mu, nu e a
	#coordenadas de sáida retangular: x e y
	#coordenadas de saída polar: r e theta
def cordinates_elip(mu, nu, a=1):
	'''(float, float)-> list'''
	res=[]
	#cartesiana
	x=a*math.cosh(mu)*math.cos(nu)
	y=a*math.sinh(mu)*math.sin(nu)
	res.append((x, y))
	#polar
	r=math.sqrt(x**2+y**2)
	theta=math.atan(y/x)
	res.append((r, theta))
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