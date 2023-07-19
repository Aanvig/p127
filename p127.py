from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)
star_data =[]
temp=[]
soup = BeautifulSoup(browser.page_source, "html.parser")
star_table = soup.find('table')

rows = star_table.find_all('tr')
for tr in rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp.append(row)

Names = []
Distance = []
Mass = []
Radius =[]

for i in range(1,len(temp)):
    Names.append(temp[i][1])
    Distance.append(temp[i][3])
    Mass.append(temp[i][5])
    Radius.append(temp[i][6])

df = pd.DataFrame(list(zip(Names,Distance,Mass,Radius)),columns=['Names','Distance','Mass','Radius'])
print(df)
df.to_csv('stars.csv')