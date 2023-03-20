from sensor import Sensor

class Wetterstation:
    """
    Repräsentiert eine Wetterstation. Jede Station braucht einen Sensor,
    von welchem Daten bezogen werden können.
    
    Des Weiteren werden zwei Methoden angeboten, um die
    Durchschnittstemperatur bzw. -druck auszurechnen.
    """

    def __init__(self, sensor: Sensor):
        """
        Initialisiert eine Wetterstation.

        Parameter:
        sensor: Sensor
        """

        self._sensor = sensor
        self._readings = []

    def record_reading(self):
        """Holt sich eine Aufzeichnung vom Sensor"""

        reading = self._sensor.get_reading()
        if len(self._readings) >= 10:
            self._readings.pop(0)
        self._readings.append(reading)

    def avg_temperature(self):
        """Berechnet die Durchschnittstemperatur aller Aufzeichnungen"""

        if len(self._readings) == 0:
            raise ValueError("Es sind keine Daten vorhanden!")
        
        sum = 0
        for reading in self._readings:
            sum += reading.temperature
        return sum / len(self._readings)

    def avg_pressure(self):
        """Berechnet den Durschnittsdruck aller Aufzeichnungen"""

        if len(self._readings) == 0:
            raise ValueError("Es sind keine Daten vorhanden!")
        
        sum = 0
        for reading in self._readings:
            sum += reading.pressure
        return sum / len(self._readings)