
from TestedTrek.Game.galaxy import Galaxy


class MockGalaxy(Galaxy):
    def __init__(self):
        Galaxy.__init__(self, webContext=None)
        self.stuff = {}
        self.my_string = ''

    def Parameter(self, parameterName):
        return self.stuff.get(parameterName, None)

    def Variable(self, variableName):
        return self.stuff.get(variableName, None)

    def WriteLine(self, message):
        fakeNewLine = " || "
        self.my_string += (str(message) + fakeNewLine)

    def SetValueForTesting(self, key, value):
        self.stuff[key] = value

    def GetAllOutput(self):
        res = self.my_string
        self.my_string = ''
        return res
