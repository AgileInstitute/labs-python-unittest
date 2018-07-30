
from tdd.Galaxy import Galaxy
from tdd.Random import Random


class Game(object):

    generator = Random()

    def __init__(self):
        self.e = 10000
        self.t = 8

    def EnergyRemaining(self):
        return self.e

    @property
    def Torpedoes(self):
        return self.t

    @Torpedoes.setter
    def Torpedoes(self, value):
        self.t = value

    def _fire_weapon(self, wg):
        if (wg.Parameter("command") == "phaser"):
            amount = int(wg.Parameter("amount"))
            enemy = wg.Variable("target")

            if (self.e >= amount):
                distance = enemy.Distance()
                if (distance > 4000):
                    wg.WriteLine("Klingon out of range of phasers at " + str(distance) + " sectors...")
                else:
                    damage = amount - (((amount / 20) * distance / 200) + Game.Rnd(200))
                    if (damage < 1):
                        damage = 1
                    wg.WriteLine("Phasers hit Klingon at " + str(distance) + " sectors with " + str(damage) + " units")
                    if (damage < enemy.GetEnergy()):
                        enemy.SetEnergy(enemy.GetEnergy() - damage)
                        wg.WriteLine("Klingon has " + str(enemy.GetEnergy()) + " remaining")
                    else:
                        wg.WriteLine("Klingon destroyed!")
                        enemy.Delete()

                self.e -= amount
            else:
                wg.WriteLine("Insufficient energy to fire phasers!")


        elif (wg.Parameter("command") == "photon"):
            enemy = wg.Variable("target")
            if (self.t > 0):
                distance = enemy.Distance()
                if ((Game.Rnd(4) + ((distance / 500) + 1) > 7)):
                    wg.WriteLine("Torpedo missed Klingon at " + str(distance) + " sectors...")
                else:
                    damage = 800 + Game.Rnd(50)
                    wg.WriteLine("Photons hit Klingon at " + str(distance) + " sectors with " + str(damage) + " units")

                    if (damage < enemy.GetEnergy()):
                        enemy.SetEnergy(enemy.GetEnergy() - damage)
                        wg.WriteLine("Klingon has " + str(enemy.GetEnergy()) + " remaining")
                    else:
                        wg.WriteLine("Klingon destroyed!")
                        enemy.Delete()

                self.t -= 1

            else:
                wg.WriteLine("No more photon torpedoes!")

    def FireWeapon(self, galaxy=None, webContext=None):
        if galaxy:
            self._fire_weapon(galaxy)
        elif webContext:
            self._fire_weapon(Galaxy(webContext=webContext))

    @staticmethod
    def Rnd(maximum):
        return Game.generator.Next(maximum)
