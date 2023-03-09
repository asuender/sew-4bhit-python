from sensor import Sensor
from wetterstation import Wetterstation

sensor = Sensor()
wetterstation = Wetterstation(sensor)

for i in range(10):
    wetterstation.record_reading()
    print(f"Temperatur: {wetterstation.avg_temperature()} °C")
    print(f"Luftdruck: {wetterstation.avg_pressure()} hPa")
    print()