import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import sqlite3
import re
import random
import sys
from IPPool import IPPool

conn = sqlite3.connect(r'mingluji.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mingluji (id integer NOT NULL PRIMARY KEY AUTOINCREMENT,email varchar(60),name varchar(60),category carchar(60),istrue integer);""")
ua = UserAgent()
baseUrl = 'https://cantonfair110.mingluji.com/node/'
IPPool = IPPool()

def getinfo(ua,baseUrl,cursor):
    global nav
    istrue = 1
    url = baseUrl+str(nav)
    headers={
        'User-Agent':ua.random
        }
    html = IPPool.getHtml(url,headers)
    html = etree.HTML(html.content)
    meta = html.xpath('//a//span/text()')
    for i in meta:
        if re.search(r'\@',i) !=None:
            email = i
    meta2 = html.xpath('//span[@class="field-item"]/text()')
    category = meta2[-2]
    name = meta2[-1]
    print(email)
    cursor.execute("""INSERT INTO mingluji (email,name,category,istrue) VALUES (?,?,?,?)""",(str(email),str(name), str(category),str(istrue)))

if __name__ == "__main__":
    
    nav = sys.argv[1]
    while(int(nav)<55000):
        try:
            getinfo(ua,baseUrl,cursor)
        except:
            print('error')
        conn.commit()
        time.sleep(random.randint(1,2))
        nav=int(nav)+1
