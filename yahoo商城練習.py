import requests
from bs4 import BeautifulSoup

want=input('想找什麼? : ')
url='https://tw.buy.yahoo.com/search/product?p='+want
much=input('找幾筆? : ')
yahoo=True
pg=1
mm=1

while yahoo:
    rq=requests.get(url).text
    bp=BeautifulSoup(rq,'html5lib')
    
    soup=bp.find('div','ResultList_resultList_IpWJt')

    for i in soup.find_all('li') :
        try:
            tit=i.find('span','BaseGridItem__title___2HWui').text.strip()
            pris=i.find('em','BaseGridItem__price___31jkj').text.strip()
            link=i.find('a')['href'].strip()
            
            print(mm,tit)
            print(link)
            print(pris)
            print('-'*30)
            mm+=1
            if mm==int(much):
                yahoo=False
                break
        
        
        except:
            continue
    pg+=1
    url='https://tw.buy.yahoo.com/search/product?p='+want+'&pg='+str(pg)
    
       
       