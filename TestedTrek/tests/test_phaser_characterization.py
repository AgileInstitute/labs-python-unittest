
import unittest

from trek.Game import Game
from trek.Random import Random

from tests.mocks.MockGalaxy import MockGalaxy
from tests.mocks.MockKlingon import MockKlingon
from tests.mocks.MockRandom import MockRandom


class PhaserPinningTests(unittest.TestCase):

    def setUp(self):

        self.game = Game()
        self.context = MockGalaxy()
        self.energy_in_new_game = 10000

        self.context.SetValueForTesting("command", "phaser")

    def test_PhasersFiredWithInsufficientEnergy(self):
        self.context.SetValueForTesting("amount", str(self.energy_in_new_game + 1))
        self.game.FireWeapon(galaxy=self.context)
        self.assertEqual("Insufficient energy to fire phasers! || ",
                         self.context.GetAllOutput())

    def test_PhasersFiredWhenKlingonOutOfRange_AndEnergyExpendedAnyway(self):
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

    def test_PhasersFiredKlingonDestroyed(self):
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

    def test_PhasersDamageOfZeroStillHits_AndNondestructivePhaserDamageDisplaysRemaining(self):
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

    def RemoveTheMockRandomGeneratorForOtherTests_IReallyWantToRefactorThatStaticVariableSoon(self):
        Game.generator = Random()

    def tearDown(self):
        self.RemoveTheMockRandomGeneratorForOtherTests_IReallyWantToRefactorThatStaticVariableSoon()
