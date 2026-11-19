# ESDRELON, Keith Asher S.
# 9-PINATUBO / FA3 CS2Q2

from abc import ABC, abstractmethod

class Sensor(ABC): # Abstract Base Class
    @abstractmethod
    def get_reading(self):
        pass


# Child classes with get_reading() methods
class PHSensor(Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")

class TempSensor(Sensor):
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")
        
        
# insantiating and executing

print("--- Lab Inventory System ---\n")

ph_sensor = PHSensor()
ph_sensor.get_reading()

temp_sensor = TempSensor()
temp_sensor.get_reading()

print("--------------------------------")