from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from http import HTTPStatus
import unittest
import requests

class TestCurrentPrice(unittest.TestCase):

    def test_btcusdprice(self):
        driver = webdriver.Firefox(executable_path='./geckodriver')
        driver.implicitly_wait(30)
        try:
            r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
            self.assertEqual(r.status_code, HTTPStatus.OK)
            rparsed = r.json()
            btcdic = None
            for c in rparsed:
                if 'symbol' in c and c['symbol'] == 'BTC':
                    btcdic = c
                    break
            if btcdic is None:
                raise Exception("BTC is not found in response")
            apiprice = round(float(btcdic['price_usd']), 1)

            driver.get("https://www.bitfinex.com/")
            try:
                actpriceelem = driver.find_element_by_xpath("//table[@id='fav-ticker-list-table']//td[text()='BTCUSD']/following-sibling::td")
                actpricetext = actpriceelem.text.replace(",", "")
                actprice = round(float(actpricetext), 1)
            except NoSuchElementException as e:
                print("Exception was caught: %s" % e)
                raise e

            self.assertEqual(apiprice, actprice, "Actual price doesn't match expected price")
        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main()

