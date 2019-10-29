import serial
#referencia em https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
def read(directory):
	'''(str)->list'''
	port=serial.Serial(directory, 1200, serial.SEVENBITS, serial.PARITY_EVEN, serial.STOPBITS_TWO)
	port.flushInput()
	dados=[]
	leitura=" "
	cont=0
	while cont<10:
		try:
			leitura=port.read(1)
			port.write(leitura)
			leitura=str(leitura)[2]
			#cont=0
		except ValueError:
			print("erro valor")
			#cont+=1
		except serial.SerialException:
			print("erro serial")
		dados.append(leitura)
		if dados[-1]=="p":
			dados.pop()
			break
		cont+=1
	if cont==10: print("limite de erros atingido")
	return dados