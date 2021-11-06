import requests
import random as rd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common import exceptions

driver = webdriver.Firefox(executable_path="./geckodriver",
        options=Options())
class Facebook_renew:

    def __init__(self, driver):

        self.driver = driver
        pass

    url = "www.facebook.com"

    def renew(self):

        self.driver.get(self.url)
        mail = self.driver.find_element_by_name("email")
        mail.send_keys("Migueljts1987@gmail.com")
        passd = self.driver.find_element_by_name("pass")
        passd.send_keys(str("22930335k"))
        time.sleep(rd.randint(2.0, 4.0))
        self.driver.find_element_by_name("login").click()
        time.sleep(rd.randint(10.0, 12.0))

        try:

            market = self.driver.find_elements_by_xpath(
                    "//a[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn cbu4d94t datstx6m taijpn5t k4urcfbm']")
            print(len(market))

            if len(market) > 5:

                market[2].click()
                time.sleep(rd.randint(2.0, 5.0))

            else:

                market = self.driver.find_elements_by_xpath(
                        '//li[@class = ""]'
                        )
                market[2].click()
                time.sleep(rd.randint(2.0, 5.0))
                
        except exceptions.NoSuchAttributeException:
            print("no se encontro el atributo")
            pass

        my_account = self.driver.find_elements_by_xpath(
                '//div[@class="ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 tgvbjcpo hpfvmrgz qt6c0cv9 rz4wbd8a a8nywdso jb3vyjys du4w35lb bp9cbjyn btwxx1t3 l9j0dhe7"]'
                )
        print(len(my_account))
        
        my_account[3].click()
        pass

    def AvailableUnavailable(self):

        renew()
        button_A_NA = self.driver.find_elements_by_xpath(
                '//span[class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5"]'
                )
        if button_A_NA.text() == "Marcar como disponible":button_A_NA.click()        
        pass
    pass

if __name__ == "__main__":

    Facebook_renew.renew()
    pass


       





