import unittest

from mock import MagicMock

from lunexservices import LunExServices


class StockQuote:
    def __init__(self, symbol, number_shares, exchange_service):
        self.symbol = symbol
        self.number_shares = number_shares
        self.exchange_service = exchange_service

    def total(self):
        return int(self.number_shares
                   * self.exchange_service.current_price(self.symbol)
                   * 1.02) + 10;


class StockQuoteTest(unittest.TestCase):

    def ignored_test_quote_total_includes_fees(self):
        service = LunExServices();
        quote = StockQuote("HE3", 100, service);
        total = quote.total()
        self.assertEqual(1234, total)

    def test_quote_total_includes_fees(self):
        service = LunExServices();
        service.current_price = MagicMock(return_value=12)
        quote = StockQuote("HE3", 100, service);

        total = quote.total()

        self.assertEqual(1234, total)
