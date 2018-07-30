
from trek.Klingon import Klingon


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

    def DeleteWasCalled(self):
        return self.deleteCalled
