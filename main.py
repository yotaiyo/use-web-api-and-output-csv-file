# coding:utf-8
import json
import urllib.request
import datetime
import csv

f = open('input.json', 'r',encoding='utf_8')
d = json.load(f)
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='

output = []
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
da_tomorrow = tomorrow + datetime.timedelta(days=1)
output.append(['city_name','city_id',str(today),str(tomorrow),str(da_tomorrow)])

for i in d:
    city_name = i['city_name']
    city_id = i['id']
    city_url = url + city_id

    readObj = urllib.request.urlopen(city_url)
    response = readObj.read()
    res = json.loads(response)

    max_today = ''
    max_tomorrow = ''
    max_da_tomorrow = ''
    for j in res['forecasts']:
        if j['dateLabel'] == '今日' and j['temperature']['max'] != None:
            max_today = j['temperature']['max']['celsius']
        if j['dateLabel'] == '明日' and j['temperature']['max'] != None:
            max_tomorrow = j['temperature']['max']['celsius']
        if j['dateLabel'] == '明後日' and j['temperature']['max'] != None:
            max_da_tomorrow = j['temperature']['max']['celsius']
    output.append([city_name,city_id,max_today,max_tomorrow,max_da_tomorrow])

with open('output.csv','w',newline='',encoding='utf_8') as f:
    writer = csv.writer(f)
    for i in output:
        writer.writerow(i)
