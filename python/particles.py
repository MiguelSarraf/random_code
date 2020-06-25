import matplotlib.pyplot as plt
from numpy import *
import pylab as graph
from mpl_toolkits.mplot3d import Axes3D

fig=graph.figure()
ax=graph.axes(projection='3d')

perda=1

class coord:
	def __init__(self, x, y):
		self.x=x
		self.y=y

	def __add__(self, outro):
		return coord(self.x+outro.x, self.y+outro.y)

	def __sub__(self, outro):
		return coord(self.x-outro.x, self.y-outro.y)

	def __mul__(self, k):
		return coord(k*self.x, k*self.y)

	def __div__(self, k):
		return coord(self.x/k, self.y/k)

	def __str__(self):
		return str(self.x)+", "+str(self.y)

	def mod(self):
		return ((self.x)**2+(self.y)**2)**.5

	def dist2(self, outro):
		return (self.x-outro.x)**2+(self.y-outro.y)**2

	def dist(self, outro):
		return dist2(self, outro)**.5

class part:
	def __init__(self, carga, massa, pos, vel, acel, forca=coord(0,0), semove=True):
		self.carga=carga
		self.posicao=pos
		self.massa=massa
		self.velocidade=vel
		self.aceleracao=acel
		self.forca=forca
		self.semove=semove

	def move(self, delta):
		self.velocidade+=self.aceleracao*delta
		self.velocidade*=perda
		self.posicao+=self.velocidade*delta

	def atualizaf(self, forca):
		self.forca=forca*(max(min(forca.mod(), 100), -100)/forca.mod())
		self.aceleracao=self.forca*(1/self.massa)

	def makeforca(self, outro):
		return ((self.posicao-outro.posicao)*(1/(self.posicao-outro.posicao).mod()))*(self.carga*outro.carga)*(1/self.posicao.dist2(outro.posicao))

parts=[]
x=[]
y=[]
t=[0]
colors={True:"blue", False:"red"}

while True:
	c=input()
	if c=="n":
		carga=float(input("carga: "))
		massa=float(input("massa: "))
		pos=coord(float(input("posicao inicial x: ")), float(input("posicao inicial y: ")))
		vel=coord(float(input("velocidade inicial x: ")), float(input("velocidade inicial y: ")))
		acel=coord(float(input("aceleracao inicial x: ")), float(input("aceleracao inicial y: ")))
		sem=float(input("se move: "))
		parts.append(part(carga, massa, pos, vel, acel, semove=sem))
		x.append([pos.x])
		y.append([pos.y])
	elif c=="s":
		disc=float(input("discretização: "))
		ntotal=float(input("total de pts: "))
		cont=0
		while cont<ntotal:
			for p1 in parts:
				fres=coord(0,0)
				for p2 in parts:
					if p1!=p2:
						fres+=p1.makeforca(p2)
				p1.atualizaf(fres)
			for p in parts:
				if p.semove: 
					p.move(disc)
				x[parts.index(p)].append(p.posicao.x)
				y[parts.index(p)].append(p.posicao.y)
			t.append(t[-1]+disc)
			cont+=1
			print(str(parts[1].posicao)+"   "+str(parts[1].velocidade)+"   "+str(parts[1].aceleracao)+"   "+str(parts[1].forca))
		for cont in range(len(parts)):
			ax.plot3D(ravel(x[cont]), ravel(y[cont]), ravel(t), colors[parts[cont].carga>0])
		graph.show()
		exit()