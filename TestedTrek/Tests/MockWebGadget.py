
from TestedTrek.Untouchables.webgadget import WebGadget


class MockWebGadget(WebGadget):
    def __init__(self):
        self.stuff = {}
        self.my_string = ''

    def Parameter(self, parameterName):
        return self.stuff.get(parameterName, None)

    def Variable(self, variableName):
        return self.stuff.get(variableName, None)

    def WriteLine(self, message):
        fakeNewLine = " || "
        self.my_string += (str(message) + fakeNewLine)

    def set_value_for_testing(self, key, value):
        self.stuff[key] = value

    def get_all_output(self):
        return self.my_string
