import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.movieprac
# client = MongoClient('mongodb://test:test@localhost', 27017)

search_list = []
query_receive = '해리포터'

url = 'https://movie.naver.com/movie/search/result.naver?query=' + query_receive
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('#old_content > ul.search_list_1 > li')

for movie in movies :
    # old_content > ul:nth-child(4) > li:nth-child(1) > dl > dt > a > strong
    title = movie.select_one('dl > dt > a').text
    img = movie.select_one('p > a > img')['src']
    url = 'https://movie.naver.com'+(movie.select_one('dl > dt > a')['href'])


    # print(title,img)
    dic = {'title': title, 'url':url}

    # dic = {'title': title, 'img': img, 'url': url}

    # 리스트에 dic추가
    search_list.append(dic)

# 리스트 하나씩 출력하는건.... for문 나와서 list출력// 맞나..;;
print(search_list)