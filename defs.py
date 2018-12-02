import requests
import json
import datetime
import random



def get_random_video_ru():
    day = random.randrange(3000)
    sec = random.randrange(86399)
    datenow = datetime.datetime.now()
    publishedAfter1 = datenow - datetime.timedelta(days=(day +1), seconds = sec)
    publishedAfter = publishedAfter1.strftime("%Y-%m-%dT%H:%M:%SZ")
    publishedBefore1 = datenow - datetime.timedelta(days=day, seconds = sec)
    publishedBefore = publishedBefore1.strftime("%Y-%m-%dT%H:%M:%SZ")

    qQ = 'абвгдеёжзийклмнопрстуфхцчшщъыэюя'
    q = qQ[random.randrange(0, (len(qQ)-1))]
    params = {"q": q,
            "order": 'date',
            "part": 'snippet',
            "type": 'video',
            "videoDuration": 'short',
            "publishedBefore": publishedBefore,
            "publishedAfter": publishedAfter,
            "relevanceLanguage": 'ru',
            "maxResults": 1,
            "key": 'AIzaSyDMQuRHpIjfG_eMhJEVNo2TEcntJfw5_Ms'}

    url = 'https://www.googleapis.com/youtube/v3/search'
    r = requests.get(url, params=params)
    json_data = json.loads(r.text)
    try:
        temp = json_data["items"][0]["id"]["videoId"]
        video_link = str(temp)
        return video_link
    except :
        print('except')
        get_random_video_ru()




def get_random_video():
    day = random.randrange(3000)
    sec = random.randrange(86399)
    datenow = datetime.datetime.now()
    publishedAfter1 = datenow - datetime.timedelta(days=(day +1), seconds = sec)
    publishedAfter = publishedAfter1.strftime("%Y-%m-%dT%H:%M:%SZ")
    publishedBefore1 = datenow - datetime.timedelta(days=day, seconds = sec)
    publishedBefore = publishedBefore1.strftime("%Y-%m-%dT%H:%M:%SZ")
    key = 'AIzaSyDMQuRHpIjfG_eMhJEVNo2TEcntJfw5_Ms'
    params = {"q": '',
            "order": 'date',
            "part": 'snippet',
            "type": 'video',
            "videoDuration": 'short',
            "publishedBefore": publishedBefore,
            "publishedAfter": publishedAfter,
            "maxResults": 1,
            "key": 'AIzaSyDMQuRHpIjfG_eMhJEVNo2TEcntJfw5_Ms'}

    url = 'https://www.googleapis.com/youtube/v3/search'
    r = requests.get(url, params=params)
    json_data = json.loads(r.text)
    try:
        temp = json_data["items"][0]["id"]["videoId"]
        video_link = str(temp)
        return video_link
    except :
        get_random_video()




def most_popular_video_a_year_ago(n):
    datenow = datetime.datetime.now()
    date_some_years_ago = datenow.replace(year=datenow.year-n, hour=0, minute=0)
    publishedAfter = date_some_years_ago.strftime("%Y-%m-%dT%H:%M:%SZ")
    publishedBefore1 = date_some_years_ago + datetime.timedelta(days=1)
    publishedBefore = publishedBefore1.strftime("%Y-%m-%dT%H:%M:%SZ")
    stopdate = datetime.datetime(1970, 1, 1)
    if date_some_years_ago < stopdate:
        return 'date error'
    key = 'AIzaSyDMQuRHpIjfG_eMhJEVNo2TEcntJfw5_Ms'
    params = {"q": '',
            "order": 'viewCount',
            "part": 'snippet',
            "type": 'video',
            "videoDuration": 'short',
            "publishedBefore": publishedBefore,
            "publishedAfter": publishedAfter,
            "maxResults": 1,
            "key": 'AIzaSyDMQuRHpIjfG_eMhJEVNo2TEcntJfw5_Ms'}

    url = 'https://www.googleapis.com/youtube/v3/search'
    r = requests.get(url, params=params)
    json_data = json.loads(r.text)
    try:
        temp = json_data["items"][0]["id"]["videoId"]
        video_link = "https://www.youtube.com/watch?v="+str(temp)
        return video_link
    except :
        return 'canot read request correct'
