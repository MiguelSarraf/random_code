import serial
#referencia em https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
def read(directory):
	'''(str)->list'''
	port=serial.Serial(directory)
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