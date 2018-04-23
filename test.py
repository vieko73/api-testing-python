from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import requests

class TestApiMethods(unittest.TestCase):

    def test_getBTCUSDcurrentprice(self):
        driver = webdriver.Firefox(executable_path='./geckodriver')
        try:
            r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
            rparsed = r.json()
            btcdic = None
            for i in rparsed:
                if 'symbol' in i and i['symbol'] == 'BTC':
                    btcdic = i
                    break
            if btcdic is None:
                raise Exception("BTC is not found in response")
            priceusd = btcdic['price_usd']

            driver.get("https://www.bitfinex.com/")
            expprice = priceusd
            actprice = None
            try:
                actprice = driver.find_element_by_xpath("//table[@id='fav-ticker-list-table']//td[text()='BTCUSD']/following-sibling::td[text()='%s']" % expprice)
            except NoSuchElementException as e:
                print("Exception was caught: %s" % e)

            self.assertIsNotNone(actprice, "BTCUSD element was not found!")
        finally:
            driver.quit()

# parse xpath string and then compare

if __name__ == '__main__':
    unittest.main()

