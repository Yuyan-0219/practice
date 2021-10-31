
from selenium import webdriver
url='https://www.ptt.cc/bbs/Gossiping/index.html'

web=webdriver.Chrome('chromedriver.exe')
    
web.implicitly_wait(10)
web.get(url)
web.maximize_window()
eighteen=web.find_element_by_class_name('btn-big')
eighteen.click()
CC=5
while True:
    
    top=web.find_element_by_xpath('//*[@id="action-bar-container"]/div/div[2]/a[2]')
    top.click()
    CC-=1
    if CC<=0:
        break