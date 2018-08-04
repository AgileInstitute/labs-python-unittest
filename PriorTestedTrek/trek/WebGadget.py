

class WebGadget(object):
    def __init__(self, commandParameter=None, commandArgument=None, targetVariable=None):
        self.commandParameter = commandParameter
        self.targetVariable = targetVariable
        self.commandArgument = commandArgument

    def Parameter(self, parameterName):
        if parameterName == 'command':
            return self.commandParameter
        else:
            return self.commandArgument

    def Variable(self, variableName):
        return self.targetVariable

    def WriteLine(self, message):
        print(message)
