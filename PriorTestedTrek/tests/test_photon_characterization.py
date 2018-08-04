
import unittest

from trek.Game import Game
from trek.Random import Random
from mocks.MockGalaxy import MockGalaxy
from mocks.MockKlingon import MockKlingon
from mocks.MockRandom import MockRandom


class PhotonPinningTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.context = MockGalaxy()
        self.context.SetValueForTesting("command", "photon")

    def test_NotifiedIfNoTorpedoesRemain(self):
        self.game.Torpedoes = 0
        self.context.SetValueForTesting("target", MockKlingon(2000, 200))
        self.game.FireWeapon(galaxy=self.context)
        self.assertEqual(
            "No more photon torpedoes! || ",
            self.context.GetAllOutput()
        )

    def test_TorpedoMissesDueToRandomFactors(self):
        distanceWhereRandomFactorsHoldSway = 2500
        self.context.SetValueForTesting("target", MockKlingon(distanceWhereRandomFactorsHoldSway, 200))
        Game.generator = MockRandom()  # without this the test would often fail
        self.game.FireWeapon(self.context)
        self.assertEqual(
            "Torpedo missed Klingon at 2500 sectors... || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.Torpedoes)

    def test_TorpedoMissesDueToDistanceAndCleverKlingonEvasiveActions(self):
        distanceWhereTorpedoesAlwaysMiss = 3500
        self.context.SetValueForTesting("target", MockKlingon(distanceWhereTorpedoesAlwaysMiss, 200))
        self.game.FireWeapon(galaxy=self.context)
        self.assertEqual(
            "Torpedo missed Klingon at 3500 sectors... || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.Torpedoes)

    def test_TorpedoDestroysKlingon(self):
        klingon = MockKlingon(500, 200)
        self.context.SetValueForTesting("target", klingon)
        Game.generator = MockRandom()
        self.game.FireWeapon(self.context)
        self.assertEqual(
            "Photons hit Klingon at 500 sectors with 825 units || Klingon destroyed! || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.Torpedoes)
        self.assertTrue(klingon.DeleteWasCalled())

    def test_TorpedoDamagesKlingon(self):
        self.context.SetValueForTesting("target", MockKlingon(500, 2000))
        Game.generator = MockRandom()
        self.game.FireWeapon(self.context)
        self.assertEqual(
            "Photons hit Klingon at 500 sectors with 825 units || Klingon has 1175 remaining || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.Torpedoes)

    def RemoveTheMockRandomGeneratorForOtherTests_IReallyWantToRefactorThatStaticVariableSoon(self):
        Game.generator = Random()

    def tearDown(self):
        self.RemoveTheMockRandomGeneratorForOtherTests_IReallyWantToRefactorThatStaticVariableSoon()

