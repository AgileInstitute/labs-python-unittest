
import unittest

from TestedTrek.Game.game import Game
from TestedTrek.Game.RandomWrapper import Random
from TestedTrek.Tests.MockGalaxy import MockGalaxy
from TestedTrek.Tests.MockKlingon import MockKlingon
from TestedTrek.Tests.MockRandom import MockRandom


class PhotonPinningTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.context = MockGalaxy()
        self.context.SetValueForTesting("command", "photon")

    def test_NotifiedIfNoTorpedoesRemain(self):
        self.game.torpedoes = 0
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
        self.game.FireWeapon(galaxy=self.context)
        self.assertEqual(
            "Torpedo missed Klingon at 2500 sectors... || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.torpedoes)

    def test_TorpedoMissesDueToDistanceAndCleverKlingonEvasiveActions(self):
        distanceWhereTorpedoesAlwaysMiss = 3500
        self.context.SetValueForTesting("target", MockKlingon(distanceWhereTorpedoesAlwaysMiss, 200))
        self.game.FireWeapon(galaxy=self.context)
        self.assertEqual(
            "Torpedo missed Klingon at 3500 sectors... || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.torpedoes)

    def test_TorpedoDestroysKlingon(self):
        klingon = MockKlingon(500, 200)
        self.context.SetValueForTesting("target", klingon)
        Game.generator = MockRandom()
        self.game.FireWeapon(self.context)
        self.assertEqual(
            "Photons hit Klingon at 500 sectors with 825 units || Klingon destroyed! || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.torpedoes)
        self.assertTrue(klingon.DeleteWasCalled())

    def test_TorpedoDamagesKlingon(self):
        self.context.SetValueForTesting("target", MockKlingon(500, 2000))
        Game.generator = MockRandom()
        self.game.FireWeapon(self.context)
        self.assertEqual(
            "Photons hit Klingon at 500 sectors with 825 units || Klingon has 1175 remaining || ",
            self.context.GetAllOutput()
        )
        self.assertEqual(7, self.game.torpedoes)

    def tearDown(self):
        Game.generator = Random()

