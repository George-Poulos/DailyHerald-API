# Author : George Poulos
# Version : 1.0
#
# Description :
#
# Pulls LatestNews Timestamp and summary from DailyHerald.com
# Using BeautifulSoup and requests libraries
#
#

from bs4 import BeautifulSoup
import requests

url = 'http://www.dailyherald.com/'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
soup = BeautifulSoup(response.content)

timeStamp = list()
summary = list()

tableEntries = soup.select('body div.sidebarOneInner ul li')

for rows in tableEntries:
    timestamp = rows.span
    key = timestamp.text.strip().rstrip(':')
    timeStamp.append(key)
    summ = rows.a
    key2 = summ.text.strip().rstrip(':')
    summary.append(key2)

fmt = '{:<10}{:<80}{}'
for (a,b) in zip(timeStamp,summary):
    print(a)
    print (b)
    print("\n")