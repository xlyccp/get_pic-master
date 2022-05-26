from selenium.webdriver.common.by import By
from selenium import webdriver
from base.base import *
from time import sleep

class Get_Pic(BasePage):
    def get(self,url):
        self.headles_top()
        js = 'window.open("' + url + '");'
        self.driver.execute_script(js)
        sleep(2)

        self.headles_top()  # 开始执行下载
        a = self.by_xpath('//*[@id="showcase-sidebar"]/div/div[1]/h3').text
        print(a.find('2'))
        x=a.find('x')
        aa = a[0:x-1]
        bb = a[x+2:]
        self.by_link('Crop & Scale Download').click()
        self.im_wait()
        self.se_xpath('//*[@id="form-respicker-custom-width"]', aa)
        self.se_xpath('//*[@id="form-respicker-custom-height"]', bb)
        self.cl_xpath('//*[@id="respicker-form"]/button')
        self.cl_xpath('//*[@id="overlay"]/section/div/a[2]')
        sleep(2)
        self.close()


