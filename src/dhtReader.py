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

def toFahrenheit( celsius):
	fahrenheit = celsius*9.0/5.0 + 32
	return fahrenheit

dhtDevice = adafruit_dht.DHT22(board.D2)

temperature = dhtDevice.temperature
humidity = dhtDevice.humidity

print()
print(humidity)
print(temperature)
print()
print(toFahrenheit(temperature))



