from selenium import webdriver
import os
import time


class InstagramBotLogin:

    def __init__(self, username, password, user):
        """
        date:
            username ---> nome instagram dell'utente
            password ---> password dell'utente              GO DOWN TO SET THE DATA 
            user     ---> utente da seguire
        attribute:
            driver:selenium.webdriver.chrome ---> permette di eseguire chrome

        """

        self.username = username
        self.password = password
        self.user = user

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()
        time.sleep(2)
        self.base_url = "https://www.instagram.com"
        self.nav_user(user)
        time.sleep(2)
        self.follow_user()
        time.sleep(2)
        self.driver.close()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(2)
        self.driver.find_element_by_class_name('L3NKy').click()
        time.sleep(2)

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))

    def follow_user(self):  # FOLLOW AND UNFOLLOW AN USER
        try:
            self.driver.find_element_by_class_name(
                'L3NKy   ').click()
        except Exception as e:
            print('errore' + format(e))
        try:
            self.driver.find_element_by_class_name(
                '_5f5mN   ').click()
        except Exception as e:
            print('errore' + format(e))
        time.sleep(2)
        try:
            self.driver.find_element_by_class_name(
                '-Cab_').click()
        except Exception as e:
            print('errore' + format(e))


if __name__ == '__main__':
    file = open("user.txt", "r")
    righe = file.readlines()
    print(righe)
    for riga in righe:
        print(riga)
        ig_bot = InstagramBotLogin(riga, 'INSERT-PASSWORD', 'USERNAME-TO-FOLLOW')
