
from TestedTrek.Game.weapon import Weapon


class Phaser(Weapon):

    def __init__(self, energy, enemy, delta_energy, max_distance=0, **kwargs):
        Weapon.__init__(self, energy, enemy, delta_energy, **kwargs)
        self.max_distance = max_distance

    def DistanceOutOfRange(self, distance, *args, **kwargs):
        return distance > self.max_distance

    def CalculateDamage(self, distance=None, *args, **kwargs):
        de = self.delta_energy
        damage = de - (((de / 20) * distance / 200) + self.random_generator.next(200))  # override getDamage
        if damage < 1:
            return 1
        return damage
