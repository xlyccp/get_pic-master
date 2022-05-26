from selenium.webdriver.common.by import By
from time import sleep

import pyautogui
from selenium.webdriver.support import expected_conditions as EC
class BasePage(object):

    def __init__(self,driver,url=None):
        self.driver=driver
        self.url=url
        if self.url!=None:
            self.driver.get(self.url)

    def by_name(self,id):
        locator=(By.NAME,id)
        ele=self.driver.find_element(*locator)
        return ele

    def by_id(self,id):
        locator=(By.ID,id)
        ele=self.driver.find_element(*locator)
        return ele

    def by_xpath(self,xpath):
        locator=(By.XPATH,xpath)
        ele=self.driver.find_element(*locator)
        return ele

    def by_link(self,link):
        locator=(By.PARTIAL_LINK_TEXT,link)
        ele=self.driver.find_element(*locator)
        return ele
    def cl_link(self,link):
        sleep(1)
        locator = (By.PARTIAL_LINK_TEXT, link)
        ele = self.driver.find_element(*locator).click()
        return ele

    def isElementExist(self,exit):
        flag = True
        try:
            self.by_xpath(exit)
            return flag
        except:
            flag = False
            return flag

    def headles_top(self):  # 切换最新句柄
        self.im_wait()
        headles = self.driver.window_handles
        print(headles)
        self.driver.switch_to.window(headles[-1])


    def im_wait(self,i=3):
        self.driver.implicitly_wait(i)

    def cl_xpath(self,xpath):
        self.im_wait()
        self.driver.find_element(By.XPATH,xpath).click()

    def se_xpath(self,xpath,text):
        self.im_wait()
        self.driver.find_element(By.XPATH,xpath).clear()
        self.driver.find_element(By.XPATH,xpath).send_keys(text)

    def close(self):
        sleep(1)
        self.im_wait()
        self.driver.close()
