# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:25:19 2021

@author: USER
"""

from selenium import webdriver
import time

url='https://data.epa.gov.tw/dataset/aqx_p_434'
win=webdriver.Chrome('chromedriver.exe')
win.implicitly_wait(10)
win.get(url)
win.maximize_window()

aqi=win.find_element_by_xpath('//*[@id="dataset-resources"]/div/table/tbody/tr[1]/td[1]/a').click()

js=win.find_element_by_link_text('JSON').click()
time.sleep(2)
cs=win.find_element_by_link_text('CSV').click()
time.sleep(2)
cs=win.find_element_by_link_text('XML').click()
time.sleep(2)