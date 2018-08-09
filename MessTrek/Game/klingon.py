
from MessTrek.Game.game import Game


class Klingon(object):

    def __init__(self):
        self.distance = 100 + Game.Rnd(4000)
        self.energy = 1000 + Game.Rnd(2000)

    def Distance(self):
        return self.distance

    def GetEnergy(self):
        return self.energy

    def SetEnergy(self, value):
        self.energy = value

    def Delete(self):
        raise NotImplementedError()
