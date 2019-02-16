#coding:utf-8

import requests
from retrying import retry

headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
             AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372\
             Safari/604.1",

<<<<<<< HEAD
            'cookie': 'gr_user_id=4e36b607-03ec-4b1a-a044-26e74bbdef8e;\
             _ga=GA1.2.561887751.1548248075; Hm_lvt_a68dc87e09b2a989eec1\
             a0669bfd59eb=1548248075,1548850522,1549365583,1549717086; gr\
             _session_id_bce67daadd1e4d71=875e927c-6439-42d7-ae52-3bc39aeb\
             b96e; _gid=GA1.2.473617437.1549904674; Hm_lpvt_a68dc87e09b2a98\
             9eec1a0669bfd59eb=1549904674; myad=1; gr_session_id_bce67daadd1\
             e4d71_875e927c-6439-42d7-ae52-3bc39aebb96e=true',
            'authority':' www.dy2018.com',
            'method': 'GET',
            'path': '/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':' gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9'
        }

@retry(stop_max_attempt_number = 10)
=======

        }

@retry(stop_max_attempt_number = 20)
>>>>>>> e29552aa425780386f1c6ff9edc699434c411744
def _parse_url(url):
    print('*'*10)
    response = requests.get(url,headers=headers)
    assert response.status_code == 200
    return response.content.decode()

def parse_url(url):

    try:
        html_str = _parse_url(url)
    except:
        html_str = None

    return html_str


if __name__ == '__main__':
    rst = parse_url('https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288')
    print(rst)


