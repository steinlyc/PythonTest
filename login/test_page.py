from base import PageBase
from selenium.webdriver.common.action_chains import ActionChains
import config
from time import sleep


class YiYiPage(PageBase):
    url = config.test_url

    def dev_input(self, search_key):
        test_address = config.test_input_js
        self.by_xpath(config.test_input).click()
        self.js(test_address)
        self.by_xpath(config.test_input).send_keys(search_key)

    def dev_button(self):
        self.by_xpath(config.test_button).click()

    def user_login(self):
        self.by_xpath(config.user_info).click()
        sleep(1)
        user_num = config.user_num_js
        user_num_clear = config.user_num_clear
        self.js(user_num_clear)
        self.js(user_num)
        self.by_xpath(config.user_num).send_keys(config.user_name)
        self.by_xpath(config.user_pwd).send_keys(config.user_password)
        self.by_xpath(config.login_button).click()