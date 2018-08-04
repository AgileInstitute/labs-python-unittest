
from TestedTrek.Game.weapon import Weapon


class Photon(Weapon):
    def __init__(self, energy, enemy, **kwargs):
        Weapon.__init__(self, energy, enemy, **kwargs)

    def DistanceOutOfRange(self, distance, *args, **kwargs):
        return self.random_generator.next(4) + ((distance / 500) + 1) > 7

    def CalculateDamage(self, *args, **kwargs):
        return 800 + self.random_generator.next(50)
