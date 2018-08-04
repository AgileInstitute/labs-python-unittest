
from TestedTrek.Game.galaxy import Galaxy
from TestedTrek.Game.RandomWrapper import Random
from TestedTrek.Game.weaponfactory import WeaponFactory
from tdd.notifications import AttackNotificationsFactory


class Game(object):

    generator = Random()  # DI it
    MaxDistance = 4000  # constant

    def __init__(self, randomgenerator=None):
        # this is terrible
        # move this to default values in weapons and leave out of create()?
        self._initial_ammo = {
            'phaser': 10000,
            'photon': 8
        }
        if randomgenerator is not None:
            Game.generator = randomgenerator

        self.weapons = { }

    def _get_remaining_ammo(self, weapon_name):
        weapon = self.weapons.get(weapon_name, None)
        if weapon:
            return weapon.energy
        else:
            return self._initial_ammo.get(weapon_name, None)

    # horribly not pythonic naming. would have to change tests also
    def EnergyRemaining(self):
        return self._get_remaining_ammo('phaser')

    # same construct for energy? eh. both suck
    @property
    def torpedoes(self):
        return self._get_remaining_ammo('photon')

    @torpedoes.setter
    def torpedoes(self, value):
        try:
            self.weapons['photon'].energy = value
        except:
            self._initial_ammo['photon'] = value

    def _fire_weapon(self, wgalaxy):
        command = wgalaxy.Parameter("command")
        attack_notification = AttackNotificationsFactory.create(
            weapon_name=command,
            callback=wgalaxy.WriteLine
        )

        # better input handling
        amt_str = wgalaxy.Parameter("amount")
        amt = int(amt_str) if amt_str else 1
        weapon = None
        try:
            weapon = WeaponFactory.create(
                weapon_name=command,
                energy=self._get_remaining_ammo(command),
                enemy=wgalaxy.Variable("target"),
                delta_energy=amt,
                random_generator=Game.generator,
                max_distance=Game.MaxDistance,
                attack_notifications=attack_notification
            )
            weapon_system = self.weapons.setdefault(
                command,
                weapon
            )
            weapon_system.Fire()
        except KeyError:
            attack_notification.callback("Invalid command " + command)

    def FireWeapon(self, galaxy=None, webContext=None):
        if galaxy:
            self._fire_weapon(galaxy)
        elif webContext:
            self._fire_weapon(Galaxy(webContext=webContext))

    @staticmethod
    def Rand(maximum):
        return Game.generator.next(maximum)
