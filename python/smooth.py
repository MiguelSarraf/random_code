import matplotlib.pyplot as plt
#este método recebe uma lista de inteiros e cria pontos médios nas suas arestas
def quebra(lista):
	'''(list)->list'''
	res=[]
	n=len(lista)
	i=0
	while i<n-1:
		res.append(lista[i])
		res.append((lista[i]+lista[i+1])/2)
		i+=1
	res.append(lista[-1])
	return res
#este método recebe uma lista de float e altera cada ponto k para a media ponderada entre k, k+1 e k+2, com pesos 1,2,1
def roda(lista, eh_fechado):
	'''(list, bool)->list'''
	res=[]
	if eh_fechado==True:
		lista.pop()
	else:
		res.append((lista[-1]+2*lista[0]+lista[1])/4)
	n=len(lista)
	i=0
	while i<n:
		res.append((lista[i]+2*lista[(i+1)%n]+lista[(i+2)%n])/4)
		i+=1
	if eh_fechado==True:
		res.append(res[0])
	else:
		res.pop()
	return res
#este método corrige os pontos para que os valores de entrada estejam na configuração final do desenho
def corrige(listax, listay):
	'''(list, list)->list, list'''
	resx=[]
	resy=[]
	mediox=0
	medioy=0
	cont=0
	while cont<len(listax)-1:
		mediox+=listax[cont]
		medioy+=listay[cont]
		cont+=1
	mediox/=(len(listax)-1)
	medioy/=(len(listax)-1)
	cont=0
	while cont<len(listax):
		resx.append(mediox+(5.03266031019*(len(listax)-1)**(-.851770887821))*(listax[cont]-mediox))
		resy.append(medioy+(5.03266031019*(len(listax)-1)**(-.851770887821))*(listay[cont]-medioy))
		cont+=1
	return resx, resy

#método main que operacionaliza os cálculos
plt.xlabel('x')
plt.ylabel('y')
print("valores iniciais em x:")
listax=input().split(", ")
cont=0
while cont<len(listax):
	listax[cont]=float(listax[cont])
	cont+=1
print("valores iniciais em y:")
listay=input().split(", ")
cont=0
while cont<len(listay):
	listay[cont]=float(listay[cont])
	cont+=1
plt.plot(listax, listay)
listax, listay=corrige(listax, listay)
if listax[0]==listax[-1] and listay[0]==listay[-1]:
	eh_fechado=True
else:
	eh_fechado=False
print("insira o número de iterações:")
n=int(input())
cont=0
while cont<n:
	listax=quebra(listax)
	listay=quebra(listay)
	listax=roda(listax, eh_fechado)
	listay=roda(listay, eh_fechado)
	cont+=1
plt.plot(listax, listay)
plt.show()