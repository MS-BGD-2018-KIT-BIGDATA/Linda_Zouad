import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import pandas as pd
from statistics import mean
import csv

def getSoupFromURL(url, method='get', data={}):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def getRanking(url):
    city_l = []

    for i in range (1,10):
        city = getSoupFromURL(url).find_all('tr')[i].select('td:nth-of-type(2)')[0].text   
        city_l.append(city)
    city_l = [s.replace('\n', '') for s in city_l]
    city_l = [s.replace(' ', '') for s in city_l]
    return city_l

url = 'https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/' 

city = '|'.join(getRanking(url))
df = pd.DataFrame(index=getRanking(url),columns = getRanking(url))
url_map = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + city + '&destinations=' + city + 'mode=driving&language=fr-FR&key'
r = requests.get(url_map)
data = json.loads(r.text)

def getDistance(url):
        for i in range(9):
            for j in range(9):
                d = data['rows'][i]['elements'][j]['distance']['text']
                df.iloc[i][j] = d
        return df

result = getDistance(getRanking(url))

result.to_csv('exo_cc_lesson3.csv')