from random import randint
from reading import Reading

class Sensor:
    def get_reading(self) -> Reading:
        return Reading(randint(-20, 50), randint(100, 200))