from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from random import seed
from random import randint
from urllib.request import urlopen
import re
import webbrowser


class InstagramBotRegister1:
    def __init__(self):
        self.driver = webdriver.chrome('./chromedriver2.exe')
        register1("https://freephonenum.com/us/receive-sms/5417083275")
        time.sleep(2)

    def register1(self, link):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            chrome_options=options, executable_path=r'./chromedriver.exe')
        driver.get(link)
        time.sleep(8)

        try:
            code = driver.find_element_by_css_selector(
                '#msgtbl > div:nth-child(4) > div.col-xs-12.col-md-8').text
            #code.strip()
            code = [str(s) for s in code.split() if s.isdigit()]  
            print(code)
            number = str(code[0]) + str(code[1])
            print(number)
            time.sleep(1)
            driver.close()
            return number
        except Exception as e:
            print('Exception-AAAAA', format(e))
