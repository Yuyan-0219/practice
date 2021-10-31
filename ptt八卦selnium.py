# -*- coding: utf-8 -*-
'''
Created on Sat Oct 30 14:57:54 2021

@author: USER
'''


from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
import time

def _newPage():
    global bb,pp,cc
    url='https://www.ptt.cc/bbs/Gossiping/index.html'

    web=webdriver.Chrome('chromedriver.exe')
    
    web.implicitly_wait(10)
    web.get(url)
    web.maximize_window()
    eighteen=web.find_element_by_class_name('btn-big')
    eighteen.click()
    
    while True:
        soup=BeautifulSoup(web.page_source,'html5lib')
        
        soups=soup.find(id='main-container')
        
        for mysoup in soups.find_all('div','r-ent'):
            if d4==mysoup.find('div','date').text:
                try:
                    if mysoup.find('div','nrec').text.strip()=='爆':
                        print(pp+1,mysoup.find('div','title').a.text.strip())
                        print('https://www.ptt.cc'+mysoup.find('div','title').a['href'].strip())
                        print(mysoup.find('div','author').text.strip())
                        print(mysoup.find('div','date').text.strip())
                        print(mysoup.find('div','nrec').text.strip())
                        print('-'*30)
                        bb=bb+1
                    pp=pp+1
                except:
                    continue
            else:
                cc=cc-1
        
        if cc<=0:
            break
        top=web.find_element_by_partial_link_text('上頁')
        top.click()
        time.sleep(3)


d1=datetime.datetime.today()
d2=str(d1).split(' ')[0]
d3=d2.split('-')
d4=d3[1]+'/'+d3[2]
if len(d4)==4:
    d4=' '+d4


cc=50
pp=0
bb=0

_newPage()

print('今天: ',d1)
print('共有文章: ',pp,'篇')
print('爆爆: ',bb,'篇')