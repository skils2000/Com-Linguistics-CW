import requests, pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
database = client.news_database
news = database.news
filteredNews = []
url = 'https://v1.ru/text/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
bigline = soup.find('div', class_='NFa25')
newsLine = bigline.find_all('p', class_='GFajr')
headlines = bigline.find_all('h2', class_='GFal')
newsTimes = bigline.find_all('time', class_='GPhx')
coms = bigline.find_all('a', class_='FVg7 FVk-')
watchs = bigline.find_all('div', class_='FVg7')

#tags = bigline.find_all('a', class_='cat')

for i in range(0, len(headlines)):
    headline = headlines[i].text #1 заголовок
    site = "https://v1.ru/" + headlines[i].find('a').get('href') #2 ссылка
    newsText = newsLine[i].find('span').text #3 текст новости
    newsTime = newsTimes[i].text #4   дата
    #com = coms[i].find('span').text #5
    watch = watchs[i].find('span').text #6 просмотры
    news_ = {
    "headline":headline,
    "text":newsText,
    "site":site,
    "time":newsTime,
    "watch":watch,
    }
    #news.insert_one(news_)
    if news.find_one({'headline': headline}, {'site': site}, {'time': newsTime}) is None:
        news.insert_one(news_)
    else:
        news.update_one({'headline': headline},{'site': site}, {'time': newsTime}, {'$set':{'watch': watch}})
