from bs4 import BeautifulSoup
import requests
import sqlite3
head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

item=input('找啥? :')
ppp=input('幾筆? :')
db=sqlite3.connect(item+'.db')
db.execute('CREATE TABLE goods (id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT, price INTEGER, shop TEXT, link TEXT)')
db.commit()

p=1
c=1
check=True

while check:
    url='https://feebee.com.tw/s/'+item+'?page='+str(p)        
    rq=requests.get(url,headers=head).text
    bp=BeautifulSoup(rq,'html5lib')    
    soup=bp.find('ol')
    
    for i in soup.find_all('li'):
        try:
            data=db.execute('SELECT * FROM goods WHERE product=?',(i.find('h3').text.strip(),))
            if data.fetchone()==None:
                list1=[]
                list1.append(i.find('h3').text.strip())
                list1.append(i.find('a')['data-price'])
                list1.append(i.find('span','shop').span.text)            
                list1.append(i.find('a')['href'])
                db.execute('INSERT INTO goods (product,price,shop,link) VALUES(?,?,?,?)',list1)
                db.commit()
                
                if c>=int(ppp):
                    check=False
                    break
                c+=1
            else:
                print('資料重複ㄌ')
        except:
            continue
    p+=1    
    
db.close()    