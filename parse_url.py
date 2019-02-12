#coding:utf-8

import requests
from retrying import retry

headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
             AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372\
             Safari/604.1",


        }

@retry(stop_max_attempt_number = 20)
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


