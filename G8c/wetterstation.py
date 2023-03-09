from sensor import Sensor

class Wetterstation:
    def __init__(self, sensor: Sensor):
        self._sensor = sensor
        self._readings = []

    def record_reading(self):
        reading = self._sensor.get_reading()
        if len(self._readings):
            self._readings.pop(0)
        self._readings.append(reading)

    def avg_temperature(self):
        if len(self._readings) == 0:
            raise ValueError("Es sind keine Daten vorhanden!")
        
        sum = 0
        for reading in self._readings:
            sum += reading.temperature
        return sum / len(self._readings)

    def avg_pressure(self):
        if len(self._readings) == 0:
            raise ValueError("Es sind keine Daten vorhanden!")
        
        sum = 0
        for reading in self._readings:
            sum += reading.pressure
        return sum / len(self._readings)