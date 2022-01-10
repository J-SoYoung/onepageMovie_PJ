import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.movieprac
# client = MongoClient('mongodb://test:test@localhost', 27017)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.fuleaf.com/plants', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

plant = soup.select_one('#plants_list > ul > div:nth-child(1) > a > div.plant__title-flex > h3')

print(plant)


