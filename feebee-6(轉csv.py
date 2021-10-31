import sqlite3
import pandas

searcH=input("請輸入要查詢的資料庫名稱: ")

dB=sqlite3.connect(searcH+".db") #資料庫的檔名命名為[商品名稱.db]

df=pandas.read_sql("SELECT * FROM goods",dB)

df.to_csv(searcH+".csv")

df.to_json(searcH+".json")