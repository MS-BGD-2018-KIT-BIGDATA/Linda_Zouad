
#!/usr/bin/env python3
# -*- coding: ascii -*-   
    
import requests
from bs4 import BeautifulSoup
import pandas as pd


def getSoupFromURL(url, method='get', data={}):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup



url = 'https://www.cdiscount.com/informatique/ordinateurs-pc-portables/pc-portables/lf-228394_6-acer.html#_his_'

def getDataFromSoup(url):
    computerRef = []
    initialPrice = []
    discountedPrice = []
    
    for i in range(0,2):
        priceInit = getSoupFromURL(url).find_all(class_='price')
        initialPrice.append(priceInit[i].text)
        
        priceDisc = getSoupFromURL(url).find_all(class_='prdtPrSt')
        discountedPrice.append(priceDisc[i].text)
        
        model = getSoupFromURL(url).find_all(class_='prdtBTit')
        computerRef.append(model[i].text)

        df = pd.DataFrame({'model': computerRef,
                       'initial_price': initialPrice,
                       'discounted_price': discountedPrice,
                       })
        return df
    
print(getDataFromSoup(url).info)


