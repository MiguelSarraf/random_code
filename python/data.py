import serial
def read():
	''''''
	port=serial.Serial('COM5')#completar o diretorio da porta
	port.flushInput()
	dados=[]
	while True:
		try:
			leitura=port.readLine()
			leitura=leitura[0:len(leitura)-2].decode("utf-8")
		except:
			print("algum erro")
			break
		dados.append(leitura)
		if leitura[-1]=="p":
			dados.pop()
			break
	return dados