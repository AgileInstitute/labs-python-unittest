
#
# THIS FILE IS UNTOUCHABLE
#
# Please do not alter this file. Pretend you didn't see it. ;-)
#


import random
import time


class LunExServiceUnavailableException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, "Sorry, sunspot activity today...please try again later", *args, **kwargs)


class SecurityExchangeTransmissionInterface(object):
    def current_price(self, symbol):
        raise NotImplementedError()


class LunExServices(SecurityExchangeTransmissionInterface):

    def current_price(self, symbol):
        self.pauseFiveSeconds()
        self.seedRandomGenerator()
        if self.randomIntegerBetweenZeroAnd(100) > 80:
            raise LunExServiceUnavailableException()

        return 42 + self.randomIntegerBetweenZeroAnd(17)

    def pauseFiveSeconds(self):
        time.sleep(5)

    def seedRandomGenerator(self):
        random.seed(int(time.time() * 256))

    def randomIntegerBetweenZeroAnd(self, maximum):
        return int(random.random() * maximum)
