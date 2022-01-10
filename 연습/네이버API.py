import requests
from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup

client_id = "ZUPIuFn5lLD_szUdXcao"
client_secret = "dcsdSoNnRY"


# Open API 검색 요청 개체 설정
header = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
keyword = '해리포터'

url = f"https://openapi.naver.com/v1/search/movie.json?query={keyword}&display=5&pubDate=2021"
response = requests.get(url, headers=header)
print(response.text)


for data in response:
    title = data['title']
    img = data['image']
    link = data['link']
    # actor = data['actor']
    # director = data['director']
    # pubDate = data['pubDate']
    #
    print (link)
    # doc = {
    #     'title': title,
    #     'img': img,
    #     'actor': actor,
    #     'director': director,
    #     'pubDate': pubDate
    # }
    # db.prac.insert_one(doc)
    # print(title, img, actor, director, pubDate)

# get
# results = list(db.lovelist.find({}, {'_id': False}))
# for result in results:
    # print(result['title'])
    # for문을 돌려 나온 값 result의 ['listTitle']을 출력한다