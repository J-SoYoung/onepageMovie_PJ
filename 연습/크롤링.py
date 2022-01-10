import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.movieprac
# client = MongoClient('mongodb://test:test@localhost', 27017)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/running/current.naver', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')


for movie in movies:
    # 현재movie 정보 넣을 list 초기화
    # current_list = []
    # print(movie.text)

    img = movie.select_one('.thumb> a > img')['src']
    url = 'https://movie.naver.com/'+(movie.select_one('.thumb> a')['href'])
    title = movie.select_one('.tit > a').text
    kinds = movie.select_one('.info_txt1 > dd > span > a').text
    director = movie.select_one('.info_txt1 > dd:nth-child(4) > span > a').text
#     actor = movie.select_one('.info_txt1 > dd:nth-child(6) > span > a').text
#     age = movie.select_one('.tit > span').text[0:3]
#     age = movie.select_one('.tit > span').get_text()

    print(url)
#     # 딕셔너리에 담기
#     dic = {'img': img, 'title': title, 'kinds': kinds, 'director': director}
#
#     # 리스트에 dic추가
#     movie_list.append(dic)
#

