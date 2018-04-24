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
            apiprice = round(float(btcdic['price_usd']), 2)

            driver.get("https://www.bitfinex.com/")
            actprice = None
            try:
                actpriceelem = driver.find_element_by_xpath("//table[@id='fav-ticker-list-table']//td[text()='BTCUSD']/following-sibling::td")
                actpricetext = actpriceelem.text.replace(",", "")
                actprice = round(float(actpricetext), 2)
            except NoSuchElementException as e:
                print("Exception was caught: %s" % e)

            print(apiprice, actprice)

            self.assertEqual(apiprice, actprice, "Actual price doesn't match expected price")
        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main()

