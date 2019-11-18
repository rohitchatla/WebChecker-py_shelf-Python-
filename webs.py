# import csv
# # import urllib.request
# # import bs4 as bs
# #
# # res=urllib.request.urlopen('https://www.sastra.edu/running-news.html')
# # #type(res)
# # #res.text
# # soup=bs.BeautifulSoup(res, 'lxml')
# # #title=soup.select('.list-title > a')
# # #print(title)
# # table=soup.find('table')
# # print(table)
# # # table_row=table.find_all('tr')
# # # # for tr in table_row:
# # # #     td=tr.find_all('td')
# # # #     row=[i.text for i in td]
# # # # print(row)
# #
# # csvf=open('scrapped.csv','wt', newline='')
# # writer=csv.writer(csvf)
# # try:
# #     #csv.append(table.get_text())
# #     writer.writerow(table)
# # finally:
# #     csvf.close()



import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time


# def fu():
url=urlopen("https://www.sastra.edu/running-news.html")
bsob=BeautifulSoup(url, "lxml")
table=bsob.findAll("table", {"class":"table table-striped table-bordered table-hover"})[0]
rows=table.findAll("tr")
csvf=open("scrapped2.csv", 'wt', newline='')
writer=csv.writer(csvf)
try:
 for row in rows:
    csvrow=[]
    for items in row.findAll(['td', 'th']):
            csvrow.append(items.get_text())
            writer.writerow(csvrow)


 print("old")



finally:
 csvf.close()
 while True:
  time.sleep(60)
  print("new")
  os.system('search.py')
  os.system('webs.py')
# fu()
