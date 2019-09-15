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
def roda(lista):
	'''(list)->list'''
	lista.pop()
	res=[]
	n=len(lista)
	i=0
	while i<n:
		res.append((lista[i]+2*lista[(i+1)%n]+lista[(i+2)%n])/4)
		i+=1
	res.append(res[0])
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
print("insira o número de iterações:")
n=int(input())
cont=0
while cont<n:
	listax=quebra(listax)
	listay=quebra(listay)
	listax=roda(listax)
	listay=roda(listay)
	cont+=1
plt.plot(listax, listay)
plt.show()