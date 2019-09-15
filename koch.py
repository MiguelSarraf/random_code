import matplotlib.pyplot as plt
def itera_koch(listax, listay):
	'''(list, list)->list, list'''
	n=len(listax)
	resx=[]
	resy=[]
	cont=0
	while(cont<n-1):
		#determina tamanho dos novos segmentos
		a=(((listax[cont]-listax[cont+1])**2+(listay[cont]-listay[cont+1])**2)**(1/2))/3
		#adiciona os vértices originais à lista
		resx.append(listax[cont])
		resy.append(listay[cont])
		#adiciona a primeiro novo vértice contido na linha original
		resx.append(listax[cont]+(listax[cont+1]-listax[cont])/3)
		resy.append(listay[cont]+(listay[cont+1]-listay[cont])/3)
		#calcula as varições em x e y na aresta original
		dx=listax[cont+1]-listax[cont]
		dy=listay[cont+1]-listay[cont]
		#define a direção perpendicular à original com módulo = a altura do triangulo a ser criado
		dx=dx+dy
		dy=dx-dy
		dx=dx-dy
		dx=(-1)*dx
		dx=dx/(3*a)
		dy=dy/(3*a)
		dx=a*dx*3**(1/2)/2
		dy=a*dy*3**(1/2)/2
		#cria o novo vértice fora da aresta original
		resx.append((listax[cont]+listax[cont+1])/2+dx)
		resy.append((listay[cont]+listay[cont+1])/2+dy)
		#cria o segundo vértice contido na aresta original
		resx.append(listax[cont+1]-(listax[cont+1]-listax[cont])/3)
		resy.append(listay[cont+1]-(listay[cont+1]-listay[cont])/3)
		cont+=1
		#adiciona o último vértice à lista
	resx.append(listax[cont])
	resy.append(listay[cont])
	return resx, resy


plt.xlabel('x')
plt.ylabel('y')
print("valores iniciais em x:")
kochx=input().split(", ")
cont=0
while cont<len(kochx):
	kochx[cont]=float(kochx[cont])
	cont+=1
print("valores iniciais em y:")
kochy=input().split(", ")
cont=0
while cont<len(kochy):
	kochy[cont]=float(kochy[cont])
	cont+=1
print("ordem:")
n=int(input())
cont=0
while(cont<n):
	kochx, kochy=itera_koch(kochx, kochy)
	cont+=1
plt.plot(kochx, kochy)
plt.show()
print(kochx)
print(kochy)