import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 9600)

buf = 0
print("Start")

while (buf != 2):
    buf = int(input("1: liga | 0: desliga "))
    if (buf == 1):
        ser.write("L")
        print("Enviado L")
        resposta = ser.readline()
        print(resposta)

    elif (buf == 0):
        ser.write("D")
        print("Enviado D")
        resposta = ser.readline()
        print(resposta)
    else:
        print("nao definido")
