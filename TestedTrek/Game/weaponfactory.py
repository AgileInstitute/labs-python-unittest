from TestedTrek.Game.phaser import Phaser
from TestedTrek.Game.photon import Photon


class WeaponFactory(object):
    """This is mediocre but gets the point across"""
    @staticmethod
    def create(weapon_name, **kwargs):
        return {
            'phaser': Phaser(**kwargs),
            'photon': Photon(**kwargs)
        }[weapon_name.lower()]