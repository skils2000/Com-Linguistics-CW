from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient()
database = client.v34
v34 = database.v34
tomita = database.tomita

f = open('output.txt', 'r')
prevLine = "1"
for line in f:
    if line.find('Polit') >= 0:
        tomita_ = {
        "textTomita": prevLine
        }
        tomita.insert_one(tomita_)
    else:
        print('not Tomita')
    prevLine = line
