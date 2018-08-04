
from TestedTrek.Game.RandomWrapper import Random


class Weapon(object):

    def __init__(self, energy, enemy, delta_energy=1, random_generator=Random(),
                 attack_notifications=None, **kwargs):
        self.energy = energy                            # energy or torpedo
        self.enemy = enemy                              # Klingon
        self.delta_energy = delta_energy                # amount or 1 torpedo
        self.random_generator = random_generator
        self.attack_notifications = attack_notifications

    def _callback_if_not_none(self, attr, *args, **kwargs):
        if self.attack_notifications:
            getattr(self.attack_notifications, attr)(*args, **kwargs)

    def Fire(self):
        if self.energy >= self.delta_energy:
            distance = self.enemy.Distance()
            if self.DistanceOutOfRange(distance):
                self._callback_if_not_none('out_of_range', self.enemy, distance)
            else:
                damage = self.CalculateDamage(distance=distance)
                self._callback_if_not_none('hit_damage', self.enemy, distance, damage)

                if damage < self.enemy.GetEnergy():
                    self.enemy.SetEnergy(self.enemy.GetEnergy() - damage)
                    self._callback_if_not_none('enemy_energy', self.enemy)
                else:
                    self.enemy.Delete()
                    self._callback_if_not_none('enemy_defeated', self.enemy)

            self.energy -= self.delta_energy
        else:
            self._callback_if_not_none('no_more_ammo')

    def DistanceOutOfRange(self, distance):
        """
        Must be implemented by all weapon types.
        :returns: bool
        """
        raise NotImplementedError()

    def CalculateDamage(self, distance=None):
        """
        Must be implemented by all weapon types.
        :returns: double
        """
        raise NotImplementedError()

