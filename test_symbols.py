from http import HTTPStatus
import unittest
import requests
import time

class TestApiMethods(unittest.TestCase):

    def get_symbols(self):
        r = requests.get('https://api.bitfinex.com/v1/symbols')
        self.assertEqual(r.status_code, HTTPStatus.OK, "Status code is: %s" % r.status_code)
        self.assertEqual(r.headers['Content-Type'], "application/json; charset=utf-8")
        self.assertIsNotNone(r.json())
        self.assertNotEqual(len(r.json()), 0)
        return r.json()

    def test_01symbolsvalues(self):
        explist = ['btcusd', 'ltcusd', 'ltcbtc', 'ethusd', 'ethbtc', 'etcbtc', 'etcusd', 'rrtusd', 'rrtbtc', 'zecusd',
                   'zecbtc',
                   'xmrusd', 'xmrbtc', 'dshusd', 'dshbtc', 'btceur', 'btcjpy', 'xrpusd', 'xrpbtc', 'iotusd', 'iotbtc',
                   'ioteth',
                   'eosusd', 'eosbtc', 'eoseth', 'sanusd', 'sanbtc', 'saneth', 'omgusd', 'omgbtc', 'omgeth', 'bchusd',
                   'bchbtc',
                   'bcheth', 'neousd', 'neobtc', 'neoeth', 'etpusd', 'etpbtc', 'etpeth', 'qtmusd', 'qtmbtc', 'qtmeth',
                   'avtusd',
                   'avtbtc', 'avteth', 'edousd', 'edobtc', 'edoeth', 'btgusd', 'btgbtc', 'datusd', 'datbtc', 'dateth',
                   'qshusd',
                   'qshbtc', 'qsheth', 'yywusd', 'yywbtc', 'yyweth', 'gntusd', 'gntbtc', 'gnteth', 'sntusd', 'sntbtc',
                   'snteth',
                   'ioteur', 'batusd', 'batbtc', 'bateth', 'mnausd', 'mnabtc', 'mnaeth', 'funusd', 'funbtc', 'funeth',
                   'zrxusd',
                   'zrxbtc', 'zrxeth', 'tnbusd', 'tnbbtc', 'tnbeth', 'spkusd', 'spkbtc', 'spketh', 'trxusd', 'trxbtc',
                   'trxeth',
                   'rcnusd', 'rcnbtc', 'rcneth', 'rlcusd', 'rlcbtc', 'rlceth', 'aidusd', 'aidbtc', 'aideth', 'sngusd',
                   'sngbtc',
                   'sngeth', 'repusd', 'repbtc', 'repeth', 'elfusd', 'elfbtc', 'elfeth', 'btcgbp', 'etheur', 'ethjpy',
                   'ethgbp',
                   'neoeur', 'neojpy', 'neogbp', 'eoseur', 'eosjpy', 'eosgbp', 'iotjpy', 'iotgbp', 'iosusd', 'iosbtc',
                   'ioseth',
                   'aiousd', 'aiobtc', 'aioeth', 'requsd', 'reqbtc', 'reqeth', 'rdnusd', 'rdnbtc', 'rdneth', 'lrcusd',
                   'lrcbtc',
                   'lrceth', 'waxusd', 'waxbtc', 'waxeth', 'daiusd', 'daibtc', 'daieth', 'cfiusd', 'cfibtc', 'cfieth',
                   'agiusd',
                   'agibtc', 'agieth', 'bftusd', 'bftbtc', 'bfteth', 'mtnusd', 'mtnbtc', 'mtneth', 'odeusd', 'odebtc',
                   'odeeth']
        actlist = self.get_symbols()

        self.assertEqual(len(actlist), len(explist), "Values count doesn't match")

        for i in actlist:
            self.assertTrue(i in explist, "%s value is not in the list" % i)

    def test_02ratelimit(self):
        # https://docs.bitfinex.com/v1/reference#rest-public-lends Ratelimit: 5req/min
        count = 0
        while count < 6:
            r = requests.get('https://api.bitfinex.com/v1/symbols')
            count += 1
        self.assertEqual(r.status_code, HTTPStatus.TOO_MANY_REQUESTS)
        time.sleep(70)
        r = requests.get('https://api.bitfinex.com/v1/symbols')
        self.assertEqual(r.status_code, HTTPStatus.OK)


if __name__ == '__main__':
    unittest.main()

