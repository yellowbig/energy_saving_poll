from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
from staff_mobile import *
import time
import pymongo
import argparse


class AutoVoter(object):
    def __init__(self):
        # mongodb数据库
        self.client = pymongo.MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]

        # self.browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

        # it's 张妍's xpath
        self._tab = '//*[@id="elect"]/div[3]/ul/li[2]/p'
        self._vote_button = '//*[@id="EconomyUser"]/div[3]/div[2]/div[2]/a[1]'
        self._input_box = '#elect > div.alert > div > div.mobileInfo > div > input'
        self._radio_box = '//*[@id="elect"]/div[6]/div/div[3]/div[2]/div[1]/span[1]/input'
        self._option_box = "//option[@id='2']"
        self._submit_button = '//*[@id="elect"]/div[6]/input'
        self._vote_success = '/html/body/div[4]/p'
        self._confirm_button = '/html/body/div[4]/div[7]/div/button'

    def vote_main(self, mobile_number):
        print('正在投票')

        try:
            self.browser.get('http://i.feixin.10086.cn/activity/jnxcz/candidate/vote')

            time.sleep(1)

            self._do_vote(mobile_number)

            try:
                self.close_floating()
            except NoSuchElementException:
                print('投票后又返回了资料填写页面，重新填写中...')
                self._do_vote(mobile_number, first_use=False)
                self.close_floating()

            print('已投票')

            self.browser.quit()

            time.sleep(1)

        except TimeoutException:
            self._do_vote(mobile_number)

    def _do_vote(self, mobile_number, first_use=True):
        tab = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self._tab))
        )
        tab.click()

        time.sleep(1)

        if first_use:
            vote_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self._vote_button))
            )
            vote_button.click()
            time.sleep(1)

        input_box = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self._input_box))
        )
        if first_use:
            input_box.send_keys(str(mobile_number))

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

        vote_again = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self._vote_button))
        )
        vote_again.click()

        time.sleep(1)

    def close_floating(self):
        self.browser.find_element_by_xpath(self._vote_success)
        self.browser.find_element_by_xpath(self._confirm_button).click()

    @staticmethod
    def get_batch_staff():
        """
        获得一批员工号码
        """
        return MOBILE_NUMBERS


def parse_args():
    parser = argparse.ArgumentParser(description='节能减排投票机')
    parser.add_argument('-n', '--num', help='输入手机号码')
    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    av = AutoVoter()
    if not args.num:
        print('你妹，去搞个号码再来投票')
    else:
        av.vote_main(args.num)
