
from TestedTrek.Game.RandomWrapper import Random


class MockRandom(Random):
    def next(self, maxValue):
        # always return 1/2 max:  It isn't random, and that's the point!
        return maxValue / 2
