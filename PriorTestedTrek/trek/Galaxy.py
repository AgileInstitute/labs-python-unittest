
class Galaxy(object):
    def __init__(self, webContext=None):
        # webContext is type WebGadget
        self.webContext = webContext

    def Parameter(self, parameterName):
        return self.webContext.Parameter(parameterName)

    def Variable(self, variableName):
        return self.webContext.Variable(variableName)

    def WriteLine(self, message):
        self.webContext.WriteLine(message)
