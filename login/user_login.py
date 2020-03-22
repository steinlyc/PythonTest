import unittest
from time import sleep
from selenium import webdriver
from test_page import YiYiPage
import config


class TestYiYi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_01(self):
        page = YiYiPage(self.driver)
        page.open()
        sleep(2)
        page.dev_input("http://210.74.12.96:8081/")
        page.dev_button()
        sleep(2)
        self.assertEqual(page.by_xpath(config.check_dev).text, "测试项目")

    def test_02(self):
        page = YiYiPage(self.driver)
        page.user_login()
        sleep(1)
        self.assertEqual(
            page.by_xpath(config.check_login).text, "会员编号 : 462370")

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
