'''
Problema: modelar um objeto à partir de um sensor de distância e servo motor com transmissão serial
Passos:
	1)Receber dados via serial
	2)converter para coordenadas cartesianas
	3)suavizar a forma
'''

import data
import conversor
import smooth
from numpy import *
import pylab as graph
import mpl_toolkits.mplot3d.axes3d as axes

#definicao das variaveis do grafico
fig=graph.figure()
ax=axes.Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
fig.add_axes(ax)

#esta função le os dados seriais, confere sua validade e retorna os valores de angulo e distancia
def recebe(port):
	'''(str)->int, int'''
	#recepcao de dados
	dados=data.read(port, ".", 300)
	#conferencia de validade
	if len(dados)!=7 or type(dados[0])!=int or type(dados[1])!=int or type(dados[2])!=int or dados[3]!="," or type(dados[4])!=int or type(dados[5])!=int or type(dados[6])!=int:
		print("invalid data received")
		return
	#criacao dos valores de angulo e distancia
	angulo=int(leitura[0]+leitura[1]+leitura[2])
	distancia=int(leitura[4]+leitura[5]+leitura[6])//10
	#conversao do angulo para radianos
	angulo=conversor.angle_degree(angulo)[0]
	#retorno
	return angulo, distancia

#esta funcao recebe listas com valores de angulos e distancia e os converte para coordenadas cartesianas
def converte(angulos, distancias):
	'''(list, list)->list, list'''
	#conferencia da validade de angulos e distancias
	if len(angulos)!=len(distancias):
		print("lists badly formulated")
		return
	#conversao dos valores
	x=[]
	y=[]
	n=len(angulos)
	cont=0
	while cont<n:
		cart=conversor.cordinates_polar(distancias[cont], angulos[cont])
		x.append(cart[0][0])
		y.append(cart[0][1])
		cont+=1
	#retorno
	return x, y

#esta funcao recebe uma lista com as curvas de nível de uma superfície em ordem crescente e plota num espaço de Hilbert de 3a ordem 
#[[[x para z=0],[y para z=0]],[[x para z=1],[y para z=1]],...,[[x para z=n],[y para z=n]]]
def plota(cords, color):
	'''(list)->pylab'''
	#cria iteração para cada curva de nível
	n=len(cords)
	cont=0
	while cont<n:
		#conferencia da validade dos dados
		x=cords[cont][0]
		y=cords[cont][1]
		if len(x)!=len(y):
			print("lists badly formulated for z="+cont)
			return
		#plota a curva de nível cont
		z=[cont]*len(x)
		ax.plot3D(ravel(x), ravel(y), ravel(z), color)
		cont+=1
	return graph

#esta funcao faz todo o processo do modelador
def modela(port, n_niveis=1, n_angulos=18, n_redund=3, n_itera=5, color="gray"):
	#iteracao para leitura dos niveis
	n_medidas=n_angulos*n_redund
	nivel=0
	curvas=[]
	while nivel<n_niveis:
		medida=0
		angulos=[]
		distancias=[]
		#iteracao para leituras pontuais
		while medida<n_medidas:
			angulo, distancia=recebe(port)
			angulos.append(angulo)
			distancias.append(distancia)
			medida+=1
		#iteracao para corrigir redundancias
		while len(angulos)!=n_angulos:
			somaa=0
			somad=0
			cont=0
			while cont<n_redund:
				somaa+=angulos.pop(0)
				somad+=distancias.pop(0)
				cont+=1
			somaa.append(somaa/n_redund)
			somad.append(somad/n_redund)
		#converte os valores
		x, y=converte(angulos, distancias)
		#suaviza a curva
		x, y=smooth.smooth(x, y, n_itera)
		curvas.append([x, y])
		nivel +=1
	#plota o grafico
	superf=plota(curvas, color)
	superf.show()