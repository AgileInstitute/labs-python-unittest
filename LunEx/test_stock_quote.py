import unittest

from mock import MagicMock

from lunexservices import LunExServiceUnavailableException
from lunexservices import LunExServices


class StockQuote:
    def __init__(self, symbol, number_shares, exchange_service):
        self.symbol = symbol
        self.number_shares = number_shares
        self.exchange_service = exchange_service

    def total(self):
        try:

            return int(self.number_shares
                       * self.exchange_service.current_price(self.symbol)
                       * 1.02) + 10
        except LunExServiceUnavailableException as e:
            raise EarthboundError(e)


class EarthboundError(Exception):
    pass


class StockQuoteTest(unittest.TestCase):

    def ignored_test_quote_total_includes_fees(self):
        service = LunExServices();
        quote = StockQuote("HE3", 100, service)
        total = quote.total()
        self.assertEqual(1234, total)

    def test_quote_total_includes_fees(self):
        service = LunExServices()
        mock_function = MagicMock(return_value=12)
        service.current_price = mock_function
        quote = StockQuote("HE3", 100, service)

        total = quote.total()

        self.assertEqual(1234, total)
        quote.total() # calling again to assure immutability
        mock_function.assert_called_once()

    def test_earthbound_exception_raised_on_sunspots(self):
        service = LunExServices()
        service.current_price = MagicMock(side_effect= \
                      LunExServiceUnavailableException("sunspots"))
        quote = StockQuote("HE3", 100, service)

        self.assertRaises(EarthboundError, quote.total)
