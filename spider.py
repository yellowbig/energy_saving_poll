from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AutoVoter(object):
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--incognito')
        option.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.24 Safari/537.36")
        self.browser = webdriver.Chrome(chrome_options=option)
        self.wait = WebDriverWait(self.browser, 10)
        # it's 马麟
        self.vote_button_xpath = '//*[@id="EconomyUser"]/div[4]/div[2]/div[2]/a[1]'

    def vote(self):
        try:
            self.browser.get('http://i.feixin.10086.cn/activity/jnxcz/candidate/vote')

            vote_button = self.browser.find_element_by_xpath(self.vote_button_xpath)
            vote_button.click()
            time.sleep(1)

            input_box = self.browser.find_element_by_xpath('//*[@id="elect"]/div[6]/div/div[2]/div/input')
            input_box.send_keys('15022161502')
            time.sleep(1)

            radio = self.browser.find_element_by_xpath('//*[@id="elect"]/div[6]/div/div[3]/div[2]/div[1]/span[1]/input')
            radio.click()
            time.sleep(1)

            select_list = self.browser.find_element_by_xpath('//*[@id="provinceName"]')
            select_list.find_element_by_xpath("//option[@id='2']").click()
            time.sleep(3)

            submit_button = self.browser.find_element_by_xpath('//*[@id="elect"]/div[6]/input')
            submit_button.click()

        except TimeoutException:
            return self.vote()


if __name__ == '__main__':
    av = AutoVoter()
    av.vote()
