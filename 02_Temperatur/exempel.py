from Blinker import Blinker
from machine import Pin
from NTC import NTC
import dht

# Gör så att LED börjar blinka (Pico W), använd 25 på Pico utan WiFi
b = Blinker("LED", freq=1)
b.start()

sensor = dht.DHT11(Pin(16)) # DHT11:an finns på pin 16
sensor.measure()
temp = sensor.temperature()
humidity = sensor.humidity()

print("DHT11: {} grader C, {}%".format(temp, humidity))

ntc = NTC(26, Rref = 9860) # NTC finns på pin 26 (ad0)
tempC = ntc.readT()
print("NTC: {} grader C".format(round(tempC)))
