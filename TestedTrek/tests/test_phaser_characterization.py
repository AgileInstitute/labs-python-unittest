
import unittest

from TestedTrek.Game.game import Game
from TestedTrek.Game.RandomWrapper import Random

from TestedTrek.Tests.MockWebGadget import MockWebGadget
from TestedTrek.Tests.MockKlingon import MockKlingon
from TestedTrek.Tests.MockRandom import MockRandom


class PhaserCharacterizationTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.context = MockWebGadget()
        self.energy_in_new_game = 10000
        self.context.set_value_for_testing("command", "phaser")

    def test_phasers_fired_with_insufficient_energy(self):

        self.context.set_value_for_testing("amount", str(self.energy_in_new_game + 1))

        self.game.fire_weapon(self.context)

        self.assertEqual("Insufficient energy to fire phasers! || ",
                         self.context.get_all_output())

    def test_phasers_fired_when_klingon_out_of_range_and_energy_expended_anyway(self):
        max_phaser_range = 4000
        out_of_range = max_phaser_range + 1
        self.context.set_value_for_testing("amount", "1000")
        self.context.set_value_for_testing("target", MockKlingon(out_of_range))

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "Klingon out of range of phasers at " + str(out_of_range) + " sectors... || ",
            self.context.get_all_output()
        )
        self.assertEqual(self.energy_in_new_game - 1000, self.game.EnergyRemaining())

    def test_phasers_fired_klingon_destroyed(self):
        klingon = MockKlingon(distance=2000, energy=200)
        self.context.set_value_for_testing("amount", "1000")
        self.context.set_value_for_testing("target", klingon)
        Game.generator = MockRandom()

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "Phasers hit Klingon at 2000 sectors with 400 units || Klingon destroyed! || ",
            self.context.get_all_output()
        )
        self.assertEqual(self.energy_in_new_game - 1000, self.game.EnergyRemaining())
        self.assertTrue(klingon.delete_was_called())

    def test_phaser_damage_displays_remaining_and_minimum_damage_of_one(self):
        # defect #038429: eventually there will be a different minimum fired
        minimal_fired = "0"

        minimal_hit = "1"
        self.context.set_value_for_testing("amount", minimal_fired)
        self.context.set_value_for_testing("target", MockKlingon(2000, 200))
        Game.generator = MockRandom()

        self.game.fire_weapon(self.context)

        self.assertEqual(
            "Phasers hit Klingon at 2000 sectors with " +
            minimal_hit + " units || Klingon has 199 remaining || ",
            self.context.get_all_output()
        )

    def tearDown(self):
        Game.generator = Random()
