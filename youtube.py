import requests
import json
import datetime
import random


day = random.randrange(3000)
sec = random.randrange(86399)
datenow = datetime.datetime.now()
publishedAfter1 = datenow - datetime.timedelta(days=(day +1), seconds = sec)
publishedAfter = publishedAfter1.strftime("%Y-%m-%dT%H:%M:%SZ")
publishedBefore1 = datenow - datetime.timedelta(days=day, seconds = sec)
publishedBefore = publishedBefore1.strftime("%Y-%m-%dT%H:%M:%SZ")

qQ = 'абвгдеёжзийклмнопрстуфэюя'
q = qQ[random.randrange(0, (len(qQ)-1))]
order = 'date'
part = 'snippet'
type = 'video'
videoDuration = 'short'
maxResults = 1
relevanceLanguage = 'ru'
key = 'AIzaSyDMQuRHpIjfG_eMhJEVNo2TEcntJfw5_Ms'
params = {"q": q,
        "order": order,
        "part": part,
        "type": type,
        "videoDuration": videoDuration,
        "publishedBefore": publishedBefore,
        "publishedAfter": publishedAfter,
        "relevanceLanguage": relevanceLanguage,
        "maxResults": maxResults,
        "key": key}

url = 'https://www.googleapis.com/youtube/v3/search'
r = requests.get(url, params=params)
json_data = json.loads(r.text)

print (publishedAfter)
NCTID = json_data["items"][random.randrange(maxResults)]["id"]["videoId"]
print("https://www.youtube.com/watch?v="+str(NCTID))
