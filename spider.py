from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import time


class AutoVoter(object):
    def __init__(self):
        # self.browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

        # it's 马麟
        self._vote_button = '//*[@id="EconomyUser"]/div[4]/div[2]/div[2]/a[1]'
        # '//*[@id="elect"]/div[6]/div/div[2]/div/input'
        self._input_box = '#elect > div.alert > div > div.mobileInfo > div > input'
        self._radio_box = '//*[@id="elect"]/div[6]/div/div[3]/div[2]/div[1]/span[1]/input'
        self._option_box = "//option[@id='2']"
        self._submit_button = '//*[@id="elect"]/div[6]/input'

    def vote(self):
        print('正在投票')
        try:
            self.browser.get('http://i.feixin.10086.cn/activity/jnxcz/candidate/vote')

            time.sleep(1)

            vote_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self._vote_button))
            )
            vote_button.click()

            time.sleep(1)

            input_box = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self._input_box))
            )
            input_box.send_keys('13702040007')

            time.sleep(1)

            radio = self.browser.find_element_by_xpath(self._radio_box)
            radio.click()

            time.sleep(1)

            option = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self._option_box))
            )
            option.click()

            time.sleep(1)

            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self._submit_button))
            )
            submit_button.click()

            time.sleep(3)

            revote_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self._vote_button))
            )
            revote_button.click()
            print('已投票')

        except TimeoutException:
            return self.vote()


if __name__ == '__main__':
    av = AutoVoter()
    av.vote()
