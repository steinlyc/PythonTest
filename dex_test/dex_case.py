from selenium import webdriver
import unittest
import time


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        url = "https://exchange.fo/"
        self.browser = webdriver.Chrome()
        self.browser.get(url)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

    def test_click(self):
        self.browser.find_element_by_xpath(
            "/html/body/div/div/div[1]/div/div[1]/div[1]/div[2]/ul/li[2]/span"
        ).click()
        time.sleep(5)
        value = self.browser.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[4]"
        ).text
        self.assertEqual(format(18.8800, '.4f'), value)


if __name__ == "__main__":
    unittest.main()
