# Author : George Poulos
# Version : 1.1
#
# Description :
#
# Pulls LatestNews Timestamp and summary from DailyHerald.com
# After pulling this information the program then crawls one layer deep to retrieve the full story
# of each latest Story on the homepage
#
# Using BeautifulSoup and requests libraries
#
#

from bs4 import BeautifulSoup
import requests

# grabbing html
url = 'http://www.dailyherald.com'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
soup = BeautifulSoup(response.content)

# initializing lists
timeStamp = list()
summary = list()
pageCrawls = list()

# initial table filter
tableEntries = soup.select('body div.sidebarOneInner ul li')

# retrieve and parse data
for rows in tableEntries:
    timestamp = rows.span
    key = timestamp.text.strip().rstrip(':')
    timeStamp.append(key)
    summ = rows.a
    key2 = summ.text.strip().rstrip(':')
    summary.append(key2)
    link = summ.attrs['href']
    url2 = url + link
    response2 = requests.get(url2, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
    soup2 = BeautifulSoup(response2.content)
    pList = list()
    tableEntries2 = soup2.select('body div.articleText p')
    # Crawl one level deep
    for p in tableEntries2:
        par = p.text.strip().rstrip(':')
        pList.append(par)
    pageCrawls.append(pList)

# Printing data
fmt = '{:<10}{:<80}'
for (a,b,c) in zip(timeStamp,summary,pageCrawls):
    print(fmt.format(a,b))
    for d in c:
        print(d)
    print("")