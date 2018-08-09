
import unittest

from TestedTrek.Game.game import Game
from TestedTrek.Game.RandomWrapper import Random

from TestedTrek.Tests.MockGalaxy import MockGalaxy
from TestedTrek.Tests.MockKlingon import MockKlingon
from TestedTrek.Tests.MockRandom import MockRandom


class PhaserPinningTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.context = MockGalaxy()
        self.energy_in_new_game = 10000
        self.context.SetValueForTesting("command", "phaser")

    def test_phasers_fired_with_insufficient_energy(self):

        self.context.SetValueForTesting("amount", str(self.energy_in_new_game + 1))

        self.game.FireWeapon(galaxy=self.context)

        self.assertEqual("Insufficient energy to fire phasers! || ",
                         self.context.GetAllOutput())

    def test_phasers_fired_when_klingon_out_of_range_and_energy_expended_anyway(self):
        maxPhaserRange = 4000
        outOfRange = maxPhaserRange + 1
        self.context.SetValueForTesting("amount", "1000")
        self.context.SetValueForTesting("target", MockKlingon(outOfRange))

        self.game.FireWeapon(galaxy=self.context)

        self.assertEqual(
            "Klingon out of range of phasers at " + str(outOfRange) + " sectors... || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(self.energy_in_new_game - 1000, self.game.EnergyRemaining())

    def test_phasers_fired_klingon_destroyed(self):
        klingon = MockKlingon(distance=2000, energy=200)
        self.context.SetValueForTesting("amount", "1000")
        self.context.SetValueForTesting("target", klingon)
        Game.generator = MockRandom()
        self.game.FireWeapon(galaxy=self.context)
        self.assertEqual(
            "Phasers hit Klingon at 2000 sectors with 400 units || Klingon destroyed! || ",
            self.context.GetAllOutput()
        )

        self.assertEqual(self.energy_in_new_game - 1000, self.game.EnergyRemaining())
        self.assertTrue(klingon.DeleteWasCalled())

    def test_phasers_damage_of_zero_still_hits_and_nondestructive_phaser_damage_displays_remaining(self):
        minimalFired = "0"
        minimalHit = "1"
        self.context.SetValueForTesting("amount", minimalFired)
        self.context.SetValueForTesting("target", MockKlingon(2000, 200))
        Game.generator = MockRandom()
        self.game.FireWeapon(galaxy=self.context)
        self.assertEqual(
            "Phasers hit Klingon at 2000 sectors with " +
            minimalHit + " units || Klingon has 199 remaining || ",
            self.context.GetAllOutput()
        )

    def tearDown(self):
        Game.generator = Random()
