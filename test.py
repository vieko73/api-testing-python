from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest
# import requests

class TestApiMethods(unittest.TestCase):

    def test_getBTCUSDcurrentprice(self):
        driver = webdriver.Firefox(executable_path='./geckodriver')
        driver.get("https://www.bitfinex.com/")
        expname = "BTCUS1D"
        # print (type(actname))
        try:
            actname = driver.find_element_by_xpath("//table[@id='fav-ticker-list-table']//td[text()='%s']" % expname)
        except NoSuchElementException:
            print("Exception was caught")

        self.assertTrue(actname, "BTCUSD element was not found!")
        driver.quit()

if __name__ == '__main__':
    unittest.main()

