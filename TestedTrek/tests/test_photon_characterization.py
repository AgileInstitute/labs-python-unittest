
import unittest

from TestedTrek.Game.game import Game
from TestedTrek.Game.RandomWrapper import Random
from TestedTrek.Tests.MockWebGadget import MockWebGadget
from TestedTrek.Tests.MockKlingon import MockKlingon
from TestedTrek.Tests.MockRandom import MockRandom


class PhotonCharacterizationTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.context = MockWebGadget()
        self.context.set_value_for_testing("command", "photon")

    def test_notified_if_no_torpedoes_remain(self):
        self.game.torpedoes = 0
        self.context.set_value_for_testing("target", MockKlingon(2000, 200))

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "No more photon torpedoes! || ",
            self.context.get_all_output()
        )

    def test_torpedo_misses_due_to_random_factors(self):
        distanceWhereRandomFactorsHoldSway = 2500
        self.context.set_value_for_testing("target", MockKlingon(distanceWhereRandomFactorsHoldSway, 200))
        Game.generator = MockRandom()  # without this the test would often fail

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "Torpedo missed Klingon at 2500 sectors... || ",
            self.context.get_all_output()
        )
        self.assertEqual(7, self.game.torpedoes)

    def test_torpedo_misses_due_to_distance_and_clever_klingon_evasive_actions(self):
        distance_where_torpedoes_always_miss = 3500
        self.context.set_value_for_testing("target", MockKlingon(distance_where_torpedoes_always_miss, 200))

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "Torpedo missed Klingon at 3500 sectors... || ",
            self.context.get_all_output()
        )
        self.assertEqual(7, self.game.torpedoes)

    def test_torpedo_destroys_klingon(self):
        klingon = MockKlingon(500, 200)
        self.context.set_value_for_testing("target", klingon)
        Game.generator = MockRandom()

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "Photons hit Klingon at 500 sectors with 825 units || Klingon destroyed! || ",
            self.context.get_all_output()
        )
        self.assertEqual(7, self.game.torpedoes)
        self.assertTrue(klingon.delete_was_called())

    def test_torpedo_damages_klingon(self):
        self.context.set_value_for_testing("target", MockKlingon(500, 2000))
        Game.generator = MockRandom()

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "Photons hit Klingon at 500 sectors with 825 units || Klingon has 1175 remaining || ",
            self.context.get_all_output()
        )
        self.assertEqual(7, self.game.torpedoes)

    def tearDown(self):
        Game.generator = Random()

