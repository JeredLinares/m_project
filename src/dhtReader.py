# Read data from DHT22
# JD Linares
# 14 Mar 2021

# Requires: 
#	adafruit/circuitpython
#	adafruit-circuitpython-dht https://github.com/adafruit/Adafruit_CircuitPython_DHT
#	python3-libgpiod
# TODO Understand CircuitPython


import time
import adafruit_dht
import board
import os

def toFahrenheit( celsius):
	fahrenheit = celsius*9.0/5.0 + 32
	return str(fahrenheit)

dhtDevice = adafruit_dht.DHT22(board.D2)

temperature = dhtDevice.temperature
humidity = dhtDevice.humidity

print()
print("Prime")
print("Temperature: "+str(temperature))
print("Humidity: "+str(humidity))
print("Converted Temp: "+toFahrenheit(temperature))
print()



while(1):
	time.sleep(60)
	try:
		file = open("THData.csv",'a')
		print(str(time.time()))
		print(toFahrenheit(dhtDevice.temperature))
		print(dhtDevice.humidity)
		print()
		file.write(str(time.time())+","+toFahrenheit(dhtDevice.temperature)+","+str(dhtDevice.humidity)+"\n")
		file.close()
	except:
		print("error")
		file.close()
	finally: 
		file.close()


