
from TestedTrek.Game.klingon import Klingon


class MockKlingon(Klingon):
    def __init__(self, distance, energy=None):
        Klingon.__init__(self)
        self.overrideDistance = distance
        self.deleteCalled = False
        self.SetEnergy(energy)

    def Distance(self):
        return self.overrideDistance

    def Delete(self):
        self.deleteCalled = True

    def delete_was_called(self):
        return self.deleteCalled
