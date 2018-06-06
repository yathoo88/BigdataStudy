from bs4 import BeautifulSoup
import os
import requests
import math


file_name = 'output/daum_movie_review.txt'
folder = file_name.split('/')[0]

# 폴더가 존재하지 않으면 새로 생성해준다.
if not os.path.exists(folder):
    os.makedirs(folder)

file = open(file_name, 'w')

base_url = 'http://movie.daum.net/moviedb/grade?movieId=%s&type=netizen&page=%d'


#  영화제목 가져오기
def _parse_title(page):
    try:
        return page.find('h2', class_='tit_rel').text
    except:
        return 'err : _parse_title'


# review 목록 가져오기
def _parse_review_list(page):
    try:
        return page.find_all('div', class_='review_info')
    except:
        return 'err : _parse_review_list'


# reivew 전체 갯수와 페이지별 보여주는 review의 개수를 가져와서 총 리뷰 페이지를 계산
def _get_page_cnt(page, review_list):
    review_tot = page.select('a[class=link_menu] span[class=txt_menu]')[0].text.replace('(', '').replace(')', '')
    review_page_tot = 1 if (int(review_tot) <= len(review_list)) else math.ceil(int(review_tot) / len(review_list))
    return review_page_tot


# page_no를 넘겨서 각 page를 load한다.
def _get_page(movie_id, page_no):
    try:
        movie_url = base_url % (movie_id, page_no)
        movie_html = requests.get(movie_url).text
        movie_page = BeautifulSoup(movie_html, 'html.parser')
        return movie_page
    except:
        return 'err : _request_get_page'


# 각 리뷰 정보를 파싱한다
def _parse_review(review):
    try:
        return {'author': review.select('a em[class=link_profile]')[0].text,
                'score': review.select('div[class=raking_grade] em')[0].text,
                'review': review.select('p[class=desc_review]')[0].text.strip(),
                'date': review.select('div[class=append_review] span[class=info_append]')[0].text.strip(),
                'movie_id': movie_id,
                'movie_title': movie_title
                }
    except:
        return 'err : _parse_review'


# 한 영화의 전체 review 조회
def _get_reviews(movie_id, page_tot_cnt):
    try:
        reviews = []
        for i in range(1, page_tot_cnt + 1):
            page = _get_page(movie_id, i)
            review_list = _parse_review_list(page)

            for review in review_list:
                a_review = _parse_review(review)
                reviews.append(a_review)
        return reviews
    except:
        return 'err : _get_reviews'

result = []
for a in range(1882, 1884) :
    movie_id = a
    page_no = 1
    page = _get_page(movie_id, page_no)
    review_list = _parse_review_list(page)
    page_tot_cnt = _get_page_cnt(page, review_list)
    movie_title = _parse_title(page)
    # _get_reviews(movie_id, page_tot_cnt)
    #result.append(a_movie_review)
    file.write(str(_get_reviews(movie_id, page_tot_cnt)) + '\n')




print(len(result))
print(result)