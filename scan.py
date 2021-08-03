# -*- coding: utf-8 -*
import serial
import time
import os

ser = serial.Serial("/dev/ttyUSB0", 115200)
code=""
while True :
	a=ser.read(1)
	time.sleep(0.001)
	if a not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789" :
		fichier = open("data_barcode.txt", "w")
		fichier.write(code)
	else :
		code = code+a
		# for titre in soup.find_all('title'):
		# print(code)
		# code=""

os.system("python3 scraping.py")
