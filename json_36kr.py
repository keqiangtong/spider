# #coding:utf-8
#
# from parse_url import parse_url
# from pprint import pprint
# import json
#
# html_str = parse_url('https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1549853289041')
#
# pprint(json.loads(html_str))
#



# coding=utf-8
import re
import json
import requests
from parse_url import parse_url
from pprint import pprint

url = "https://www.36kr.com"
html_str = parse_url(url)

html_str = re.findall(r'<script>var props=(.*?),locationnal=',html_str)[0]

# html_str_json= json.loads(html_str)

with open('36kr.json', 'w') as f:
    f.write(html_str)

# json.loads把json字符串转化为python类型
ret1 = json.loads(html_str)
pprint(ret1)
print(type(ret1))

# json.dumps能够把python类型转化为json字符串
# with open("douban.json","w",encoding="utf-8") as f:
#     f.write(json.dumps(ret1,ensure_ascii=False,indent=4))
#     # f.write(str(ret1))