
#
#
# THIS FILE IS UNTOUCHABLE
#
#


import time
import random


class LunExServiceUnavailableException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, "Sorry, sunspot activity today...please try again later", *args, **kwargs)


class SecurityExchangeTransmissionInterface(object):
    def current_price(self, symbol):
        raise NotImplementedError()


class LunExServices(SecurityExchangeTransmissionInterface):

    def current_price(self, symbol):
        self.pause()
        if self.invisible_hand(100) > 80:
            raise LunExServiceUnavailableException()

        randomPrice = 42 + (self.invisible_hand(12))
        return randomPrice

    def pause(self):
        time.sleep(5000)

    def invisible_hand(self, maxValue):
        return maxValue*random.random()

