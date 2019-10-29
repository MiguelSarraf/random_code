#referencia em https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
import serial
def read(directory, baudrate=1200, databits=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO):
	'''(str, int, bit_count, bit_parity, bit_count)->list'''
	port=serial.Serial(directory, baudrate, databits, parity, stopbits)
	port.flushInput()
	dados=[]
	leitura=None
	cont=0
	while cont<10:
		try:
			leitura=port.read(1)
			leitura=leitura.decode("utf-8")
			cont=0
		except:
			print("error during read")
			cont+=1
		dados.append(leitura)
		if dados[-1]==0x00000100:
			dados.pop()
			break
		cont+=1

	if cont==10: print("limite de erros atingido")
	port.close()
	return dados
def write(directory, data, baudrate=1200, databits=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO):
	'''(str, str, int, bit_count, bit_parity, bit_count)->list'''
	port=serial.Serial(directory, baudrate, databits, parity, stopbits)
	n=len(data)
	cont=0
	while cont<n:
		try:
			port.write(data[cont].encode())
		except:
			print("error during write")
		cont+=1
	port.close()