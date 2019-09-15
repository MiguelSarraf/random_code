import matplotlib.pyplot as plt
import math
print("lados:")
n=int(input())
#determina o sen e cos do angulo externo do poligono a ser montado
sin=math.sin(2*math.pi/n)
cos=math.cos(2*math.pi/n)
#define o primeiro vértice e o primeiro vetor diretor de lado
x=[0]
y=[0]
v=[1,0]
cont=1
while cont<n:
	#para cada lado adiciona-se o próximo vértice e define-se o próximo vetor diretor
	x.append(x[-1]+v[0])
	y.append(y[-1]+v[1])
	#para se determinar o próximo vetor diretor, deve-se rotacionar o anterior pelo angulo externo v(k+1)=v(k)[[cos, sen],[-sen, cos]]
	dx=v[0]*cos-v[1]*sin
	dy=v[0]*sin+v[1]*cos
	v=[dx, dy]
	cont+=1
x.append(0)
y.append(0)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y)
plt.show()
print(x[::-1])
print(y[::-1])