
import random


class Random(object):

    def next(self, maxValue):
        return maxValue * random.random()

    def next_double(self):
        return random.random()
