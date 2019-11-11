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
import tkinter as tk
from tkinter import StringVar
import glob
import sys

#definicao das variaveis do grafico
fig=graph.figure()

#esta função le os dados seriais, confere sua validade e retorna os valores de angulo e distancia
def recebe(port):
	'''(str)->int, int'''
	#recepcao de dados
	dados=data.read(port, ".", 300)
	#conferencia de validade
	valid=["0","1","2","3","4","5","6","7","8","9"]
	if len(dados)!=7 or not(dados[0] in valid) or not(dados[1] in valid) or not(dados[2] in valid) or dados[3]!="," or not(dados[4] in valid) or not(dados[5] in valid) or not(dados[6] in valid):
		print("invalid data received")
		if len(dados)>=3 and dados[-1] in valid and dados[-2] in valid and dados[-3] in valid:
			angulo=-1
			distancia=int(leitura[4]+leitura[5]+leitura[6])//10
			return angulo, distancia
		return -2, 0
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
			if angulo==-1:
				angulo=angulos[-1]
			angulos.append(angulo)
			distancias.append(distancia)
			medida+=1
		#iteracao para corrigir redundancias
		while len(angulos)!=n_angulos:
			somaa=0
			somad=0
			cont=0
			n=0
			while cont<n_redund:
				if angulos[-1]==-2:
					angulos.pop()
					distancias.pop()
				else:
					somaa+=angulos.pop(0)
					somad+=distancias.pop(0)
					n+=1
				cont+=1
			somaa/=n
			somad/=n
		#converte os valores
		x, y=converte(angulos, distancias)
		#suaviza a curva
		x, y=smooth.smooth(x, y, n_itera)
		curvas.append([x, y])
		nivel +=1
	#plota o grafico
	superf=plota(curvas, color)
	superf.show()

#define uma lista com as portas ativas que podem ser utilizadas
if sys.platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    ports = glob.glob('/dev/tty[A-Za-z]*')
elif sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/tty.*')
else:
	print("unknown platform")
	exit()

#codigo principal que gera a interface grafica
win=tk.Tk()
win.title("ModelaDor 3D")
win.geometry("500x500")
modelcolor = StringVar(win)
porta=StringVar(win)
modelcolor.set("gray") # default value
labeli=tk.Label(win, text="Bem vindo ao ModelaDor 3D, insira os parâmetros necessários e clique 'Modelar'", height=3, wraplength=450)
labelport=tk.Label(win, text="Porta utilizada para comunicação:", height=3)
port=tk.OptionMenu(win, porta, *ports)
labellevel=tk.Label(win, text="Número de níveis que a serem amostrados:", height=3, wraplength=200)
level=tk.Spinbox(win, from_=1, to=18)
labelang=tk.Label(win, text="Número de ângulos sendo amostrados:", height=3)
ang=tk.Spinbox(win, from_=1, to=180)
labelredund=tk.Label(win, text="Número de medições por ângulo:", height=3)
redund=tk.Spinbox(win, from_=1, to=10)
labelitera=tk.Label(win, text="Número de iterações de suavização:", height=3)
itera=tk.Spinbox(win, from_=0, to=15)
labelcolor=tk.Label(win, text="Cor das linhas do modelo:", height=3)
color=tk.OptionMenu(win, modelcolor, "red", "green", "blue", "white", "black", "gray")
butc=tk.Button(win, text="Cancelar", width=20, command=win.destroy)
butm=tk.Button(win, text="Modelar", width=20, command=lambda:modela(str(porta), int(level.get()), int(ang.get()), int(redund.get()), int(itera.get()), modelcolor))
labeli.pack()
labeli.place(anchor="n",relx=.5)
butc.pack()
butc.place(anchor="sw",relx=.05, rely=.95)
butm.pack()
butm.place(anchor="se", relx=.95, rely=.95)
labelport.pack()
labelport.place(anchor="nw", relx=.05, rely=.095)
port.pack()
port.place(anchor="nw", relx=.6, rely=.13)
labellevel.pack()
labellevel.place(anchor="nw", relx=.05, rely=.2)
level.pack()
level.place(anchor="nw", relx=.6, rely=.24)
labelang.pack()
labelang.place(anchor="nw", relx=.05, rely=.315)
ang.pack()
ang.place(anchor="nw", relx=.6, rely=.35)
labelredund.pack()
labelredund.place(anchor="nw", relx=.05, rely=.425)
redund.pack()
redund.place(anchor="nw", relx=.6, rely=.46)
labelitera.pack()
labelitera.place(anchor="nw", relx=.05, rely=.535)
itera.pack()
itera.place(anchor="nw", relx=.6, rely=.57)
labelcolor.pack()
labelcolor.place(anchor="nw", relx=.05, rely=.655)
color.pack()
color.place(anchor="nw", relx=.6, rely=.68)
win.mainloop()