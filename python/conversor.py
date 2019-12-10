import math

#conversores de coordenadas planas

#conversor de coordenadas retangular para polar, eliptica, parabolica
	#entrada: x, y e a
	#saída polar: r e theta
	#saída eliptica: mu e nu
	#saída parabólica: sigma e tau
def cordinates_rect(x, y, a=1):
	'''(float, float, float)->list'''
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
	#parabolica
	sigma=math.sqrt(math.sqrt(x**2+y**2)-y)
	tau=math.sqrt(math.sqrt(x**2+y**2)+y)
	res.append((sigma, tau))
	return res

#conversor de coordenadas polar para retangular, eliptica, parabólica
	#entrada: r, theta e a
	#saída retangular: x e y
	#saída eliptica: mu e nu
	#saída parabólica: sigma e tau
def cordinates_polar(r, theta, a=1):
	'''(float, float, float)->list'''
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
	#parabolica
	sigma=math.sqrt(math.sqrt(x**2+y**2)-y)
	tau=math.sqrt(math.sqrt(x**2+y**2)+y)
	res.append((sigma, tau))
	return res

#conversor de coordenadas eliptica para retangular, polar, parabólica
	#entrada: mu, nu e a
	#saída retangular: x e y
	#saída polar: r e theta
	#saída parabólica: sigma e tau
def cordinates_elip(mu, nu, a=1):
	'''(float, float, float)-> list'''
	res=[]
	#cartesiana
	x=a*math.cosh(mu)*math.cos(nu)
	y=a*math.sinh(mu)*math.sin(nu)
	res.append((x, y))
	#polar
	r=math.sqrt(x**2+y**2)
	theta=math.atan(y/x)
	res.append((r, theta))
	#parabolica
	sigma=math.sqrt(math.sqrt(x**2+y**2)-y)
	tau=math.sqrt(math.sqrt(x**2+y**2)+y)
	res.append((sigma, tau))
	return res

#conversor de coordenadas parabólica para retangular, polar, elíptica
	#entrada: sigma, tau e a
	#saída retangular: x e y
	#saída polar: r e theta
	#saída elíptica: mu e nu
def cordinates_parab(sigma, tau, a=1):
	'''(float, float, float)->list'''
	res=[]
	#cartesiana
	x=sigma*tau
	y=(tau**2-sigma**2)/2
	res.append((x, y))
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

#conversores de angulos

#conversor de angulo graus para radiano, grado
	#entrada: thetag
	#saida: thetar, thetagon
def angle_degree(thetag):
	'''(float)->list'''
	res=[]
	thetar=math.pi*thetag/180
	res.append(thetar)
	thetagon=thetag*10/9
	res.append(thetagon)
	return res

#conversor de angulo radiano para graus, grado
	#entrada: thetar
	#saida:thetag, thetagon
def angle_rad(thetar):
	'''(float)->list'''
	res=[]
	thetag=thetar*180/math.pi
	res.append(thetag)
	thetagon=thetag*10/9
	res.append(thetagon)
	return res

#conversor de angulo grado para graus, radiano
	#entrada: thetagon
	#saida:thetag, thetar
def angle_grad(thetagon):
	'''(float)->list'''
	res=[]
	thetag=thetagon*9/10
	res.append(thetag)
	thetar=math.pi*thetag/180
	res.append(thetar)
	return res

#conversores de temperatura

#conversor de temperatura celcius para farenheit, kelvin
	#entrada: Tc
	#saída: Tf, Tk
def temp_celcius(Tc):
	'''(float)->list'''
	res=[]
	Tf=Tc*9/5+32
	res.append(Tf)
	Tk=Tc+273
	res.append(Tk)
	return res

#conversor de temperatura farenheit para celcius, kelvin
	#entrada: Tf
	#saída: Tc, Tk
def temp_faren(Tf):
	'''(float)->list'''
	res=[]
	Tc=(Tf-32)*5/9
	res.append(Tc)
	Tk=Tc+273
	res.append(Tk)
	return res

#conversor de temperatura kelvin para celcius, farenheit
	#entrada: Tk
	#saída: Tc, Tf
def temp_kelvin(Tk):
	'''(float)->list'''
	res=[]
	Tc=Tk-273
	res.append(Tc)
	Tf=Tc*9/5+32
	res.append(Tf)
	return res