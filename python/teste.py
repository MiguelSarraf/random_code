import data
def teste():
	cont=0
	dados=[]
	while cont<10:
		leitura=data.read("COM15", ".", 300)
		dados.append((10-int(leitura[4]+leitura[5]+leitura[6])//10,int(leitura[0]+leitura[1]+leitura[2])))
		cont+=1
	return dados