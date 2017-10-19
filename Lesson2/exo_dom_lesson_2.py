#!/usr/bin/env python3
# -*- coding: ascii -*-   
    
import requests
from bs4 import BeautifulSoup


def getSoupFromURL(url, method='get', data={}):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup



def getDataFromSoup(url):   
    
    title = getSoupFromURL(url).select('th:nth-of-type(5)')
    title2 = getSoupFromURL(url).select('th:nth-of-type(6)')
    
    print(title[0].text,title2[0].text)

    data = getSoupFromURL(url).find_all(class_='montantpetit G')
    row_title = getSoupFromURL(url).find_all(class_='libellepetit G')


  
    print(data[1].text,data[2].text,row_title[0].text)
    print(data[4].text,data[5].text,row_title[1].text)
    print(data[10].text,data[11].text,row_title[3].text)
    print(data[13].text,data[14].text,row_title[4].text)
    
def getDataForYear(year):
    url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=' + year  
    print('\nDonnees ' + year)
    return getDataFromSoup(url)

for year in range (int('2010'),int('2016')):
    getDataForYear(str(year))


    