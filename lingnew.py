import requests, pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient, ASCENDING, DESCENDING

f = open('input.txt', 'w')
client = MongoClient()
database = client.v34
v34 = database.v34
for x in v34.find( {} ).sort([('_id', ASCENDING)]):
    f.write(str(x['_id']) + '__' + x['headline'] + '. ' +  x['text'] + ';\n')
    
url = 'https://riac34.ru/news/131134'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
bigline = soup.find('div', class_='inner-new-content')
headlines = bigline.find_all('a', class_='caption')
newsTimes = bigline.find_all('span', class_='date')


for i in range(0, len(headlines)):
    headline = headlines[i].text #1 заголовок
    site = "https://riac34.ru/" + headlines[i].get('href') #2 ссылка
    responseT = requests.get(site)
    soupT = BeautifulSoup(responseT.text, 'lxml')
    biglineT = soupT.find('div', class_='full-text')
    newsLine = biglineT.text
    newsLine = newsLine.replace('\n', "") #3 текст новости
    newsTime = newsTimes[i].text #4   дата
    v34_ = {
    "headline":headline,
    "text":newsLine,
    "site":site,
    "time":newsTime,
    }
    
    if v34.find_one({'headline': headline}) is None:
        if v34.find_one({'site': site}) is None:
            if v34.find_one({'time': newsTime}) is None:
                v34.insertone(news)
    else:
        print('lol')