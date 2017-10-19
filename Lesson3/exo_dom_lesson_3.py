#!/usr/bin/env python3
# -*- coding: ascii -*- 

import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import pandas as pd
from statistics import mean
import csv

token = "b7c33928d85e646c9b47541dd4d21f7c7b88609f"
headers = {'Authorization' : 'token %s' % token}

def getSoupFromURL(url, method='get', data={}):
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

url = 'https://gist.github.com/paulmillr/2657075'


df = pd.DataFrame(columns = ('Rank', 'User', 'Star'))

def getRanking(url):
    rank_l = []
    name_l = []

    for i in range (1,256):
        rank = getSoupFromURL(url).find_all('tr')[i].select('th:nth-of-type(1)')[0].text
        name = getSoupFromURL(url).find_all('tr')[i].find('a').contents[0]
    
        rank_l.append(rank)
        name_l.append(name)
    df['Rank'] = rank_l
    df['User'] = name_l
    return df
    


def getStars(names):
    for name in names:
        nb_repo = int(getSoupFromURL('https://github.com/' + name).find_all(class_="Counter")[0].text)
        index = df['User'].values.tolist().index(name)
        df.iloc[index]['Star'] = 0
        for i in range(max(nb_repo//30,1)):
            url_repo = 'https://api.github.com/users/' + name + '/repos?page=' + str(i)
            r = requests.get(url_repo, headers = headers)
            data = json.loads(r.text)   
            df.iloc[index]['Star'] = df.iloc[index]['Star'] + sum(([data[i]['stargazers_count'] for i in range(min(30, nb_repo))]))
        n_l = int(nb_repo % 30)
        url_repo = 'https://api.github.com/users/' + name + '/repos?page=' + str(nb_repo//30 + 1)
        r = requests.get(url_repo, headers = headers)
        data = json.loads(r.text)
        df.iloc[index]['Star'] = df.iloc[index]['Star'] + sum([data[i]['stargazers_count'] for i in range(n_l)])
        df.iloc[index]['Star'] = "%.1f" % (df.iloc[index]['Star']/nb_repo)
    return df

ranking = getStars(getRanking(url)['User'])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



 