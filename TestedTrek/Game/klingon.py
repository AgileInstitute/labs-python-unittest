
from TestedTrek.Game.RandomWrapper import Random


class Klingon(object):

    def __init__(self):
        self.distance = 100 + Random().next(4000)
        self.energy = 1000 + Random().next(2000)

    def Distance(self):
        return self.distance

    def GetEnergy(self):
        return self.energy

    def SetEnergy(self, value):
        self.energy = value

    def Delete(self):
        raise NotImplementedError()
