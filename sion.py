#!/usr/bin/python3.6

import os
import random
import getpass
from base64 import b64decode, b64encode
from selenium import webdriver

url = ""
param = ""

chromedriver = "chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url)

def submitForm():
    target = url + param
    pesan = ["Test AutoSubmit :)", "Random generated text :)"]
    driver.get(url)
    driver.find_element_by_css_selector("input[type='radio'][value='1']").click()
    for i in driver.find_elements_by_tag_name('option'):
        if i.text == 'SMA':
            i.click()
        elif i.text == '<= RP. 1 JUTA':
            i.click()
            break

    for radio_btn in range(108):
        driver.find_elements_by_xpath("//*[starts-with(@value, '4')]")[radio_btn].click()

    driver.find_element_by_xpath("//textarea[@class='form-control']").send_keys(random.choice(pesan))
    driver.find_element_by_xpath("//input[@type='submit']").click()

def login(nim, passcode):
    username = driver.find_element_by_id("usern")
    password = driver.find_element_by_id("passw")

    username.send_keys(nim)
    password.send_keys(passcode)

    driver.find_element_by_css_selector(".submit").click()
    submitForm()

if __name__ == "__main__":
    nim = input("NIM : ")
    passcode = b64encode(getpass.getpass().encode('ascii'))
    login(nim, b64decode(passcode).decode('ascii'))
