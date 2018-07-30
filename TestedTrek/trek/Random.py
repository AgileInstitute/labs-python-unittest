
import random


class Random(object):
    def Next(self, maxValue):
        return maxValue*random.random()

    def NextDouble(self):
        return random.random()
