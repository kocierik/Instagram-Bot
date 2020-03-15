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
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver.exe')
        driver.get(link)
        time.sleep(8)
        
        try:
            code = driver.find_element_by_css_selector(
                'body > section > div > div.row > div.col-lg-9 > table > tbody > tr:nth-child(1) > td:nth-child(3)').text
            code = int(re.search(r'\d+', code).group(0))
            print(code)
            time.sleep(1)
            driver.close()
            return code
        except Exception as e:
            print('Exception-AAAAA', format(e))
