import requests
from bs4 import BeautifulSoup


def getSoupFromURL(url, method='get', data={}):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

soup = getSoupFromURL('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2013')

data = soup.find(class_='montantpetit G').parent.select('td:nth-of-type(1)')
#row_title = soup.find_all(class_='libellepetit G')

print(data)
#print(row_title)

'''
def getDataFromSoup(url):   
    
    title = getSoupFromURL(url).select('th:nth-of-type(5)')
    title2 = getSoupFromURL(url).select('th:nth-of-type(6)')
    
    print(title[0].text,title2[0].text)
    '''