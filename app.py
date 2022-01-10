from bson import json_util
from flask import Flask, render_template, jsonify, request, json
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.onepage



## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movielist')
def movieList():
    return render_template('movie-list.html')




## API 역할을 하는 부분
@app.route('/current', methods=['GET'])
def currentListing():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/running/current.naver', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

    #영화 가져올 갯수
    count = 7

    # 현재movie 정보 넣을 list 초기화
    current_list = []

    for index, movie in enumerate(movies):

        img = movie.select_one('.thumb> a > img')['src']
        url = 'https://movie.naver.com/' + (movie.select_one('.thumb> a')['href'])
        title = movie.select_one('.tit > a').text
        kinds = movie.select_one('.info_txt1 > dd > span > a').text
        director = movie.select_one('.info_txt1 > dd:nth-child(4) > span > a').text


        # 딕셔너리에 담기
        dic = {'img': img,
               'url': url,
                'title': title,
                'kinds': kinds,
                'director': director}

        # 리스트에 dic추가
        current_list.append(dic)
        # print(current_list)

        if index + 1 == count:
            break

    return jsonify({"current": current_list})


@app.route('/menuMovie', methods=['GET'])
def munuListing():
    menu_receive = request.args.get('type')

    if menu_receive == 'preMovie':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get('https://movie.naver.com/movie/running/premovie.naver', headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

        # 영화 가져올 갯수
        count = 7

        # 현재movie 정보 넣을 list 초기화
        menu_list = []

        for index, movie in enumerate(movies):
            img = movie.select_one('.thumb> a > img')['src']
            url = 'https://movie.naver.com/' + (movie.select_one('.thumb> a')['href'])
            title = movie.select_one('.tit > a').text

            # 딕셔너리에 담기
            dic = {'img': img, 'url': url, 'title': title}

            # 리스트에 dic추가
            menu_list.append(dic)
            # print(menu_list)

            if index + 1 == count:
                break
        return jsonify({"menu_list": menu_list})
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get('https://movie.naver.com/movie/running/current.naver?view=list&tab=normal&order=point', headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

        # 영화 가져올 갯수
        count = 7

        # 현재movie 정보 넣을 list 초기화
        menu_list = []

        for index, movie in enumerate(movies):
            img = movie.select_one('.thumb> a > img')['src']
            url = 'https://movie.naver.com/' + (movie.select_one('.thumb> a')['href'])
            title = movie.select_one('.tit > a').text

            # 딕셔너리에 담기
            dic = {'img': img, 'url': url, 'title': title}

            # 리스트에 dic추가
            menu_list.append(dic)
            # print(menu_list)

            if index + 1 == count:
                break
        return jsonify({"menu_list": menu_list})


@app.route('/search', methods=['GET'])
def searchListing():
    query_receive = request.args.get('query_give')

    search_list = []

    url = 'https://movie.naver.com/movie/search/result.naver?query=' + query_receive
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.select('#old_content > ul.search_list_1 > li')

    for movie in movies:
        title = movie.select_one('dl > dt > a').text
        img = movie.select_one('p > a > img')['src']
        url = 'https://movie.naver.com' + (movie.select_one('dl > dt > a')['href'])
        # print(movie)

        # 딕셔너리에 담기
        dic = {'title': title, 'url': url, 'img':img}

        # 리스트에 dic추가
        search_list.append(dic)

    print(search_list)
    return jsonify({"search_list": search_list})


@app.route('/card', methods=['POST'])
def reviewSaving():
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']
    img_receive = request.form['img_give']

    print(title_receive, comment_receive, img_receive)

    doc = {'title': title_receive, 'comment': comment_receive, 'img':img_receive}
    db.review.insert_one(doc)

    return jsonify({'success': '저장되었습니다'})


@app.route('/review', methods=['GET'])
def reviewShow():
    reviewCard = list(db.review.find({},{'id':False}))
    print(reviewCard)

    return jsonify({'review': json_util.dumps(reviewCard)})


@app.route('/delete', methods=['POST'])
def reviewDel():
    title_receive = request.form['title_give']

    db.review.delete_one({'title': title_receive})
    print(title_receive)

    return jsonify({'msg':'삭제되었습니다', 'result': title_receive})



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)