from bs4 import BeautifulSoup
import requests
import math
import os

file_name = 'output/naver_movie_review(generator).txt'
folder = file_name.split('/')[0]

# 폴더가 존재하지 않으면 새로 생성해준다.
if not os.path.exists(folder):
    os.makedirs(folder)

file = open(file_name, 'w')



base_url = 'https://movie.naver.com/movie/point/af/list.nhn?target=after&page=%d'
page_no = 1


# page_no를 넘겨서 각 page를 load한다.
def _get_page(page_no):
    try:
        movie_url = base_url % page_no
        movie_html = requests.get(movie_url).text
        movie_page = BeautifulSoup(movie_html, 'html.parser')
        return movie_page
    except:
        return 'err : _request_get_page'


#각 리뷰 파싱해서 저장
def _parse_review_generator(review_list) :
    try :
        for review in review_list :
            movie_info = review.find('td', class_='title').find('a', class_='movie')
            movie_title = movie_info.text
            params = movie_info['href'].split('&')
            movie_id = ''
            for param in params:
                if param[:5] == 'sword':
                    movie_id = param[6:]
            yield {'id': review.find('td', class_='ac num').text,
                   'score': review.find('td', class_='point').text,
                   'movie_id': movie_id,
                   'movie_title': movie_title,
                   'review': review.find('td', class_='title').contents[4].strip(),
                   'author': review.select('td[class=num] a[class=author]')[0].text,
                   'date': review.select('td[class=num]')[0].text[-8:]
                   }
    except :
        return 'err : _parse_review_generator'



# reivew 전체 갯수와 페이지별 보여주는 review의 개수를 가져와서 총 리뷰 페이지를 계산
def _get_page_cnt(page, review_list):
    review_tot = page.find('strong', class_='c_88 fs_11').text
    review_page_tot = 1 if (int(review_tot) <= len(review_list)) else math.ceil(int(review_tot) / len(review_list))
    return review_page_tot


# review 목록 가져오기
def _parse_review_list(page):
    try:
        return page.select('tbody tr')
    except:
        return 'err : _parse_review_list'


page = _get_page(page_no)

review_list = _parse_review_list(page)
print(len(review_list))
page_tot_cnt = _get_page_cnt(page, review_list)
print(page_tot_cnt)

# todo:::3을 (page_tot_cnt+1)로 바꿔야함!!... 근데 너무 많은데..?....흠..
for page_no in range(1, 100):
    page = _get_page(page_no)
    review_list = _parse_review_list(page)

    for review in _parse_review_generator(review_list) :
        # print(str(review))
        file.write(str(review) + '\n')

file.close()

