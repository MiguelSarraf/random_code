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
	'''(list)->list'''
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