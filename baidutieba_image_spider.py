#coding:utf-8

import requests
from lxml import etree

class BaiduImageSpider():

    def __init__(self,item):
        self.start_url = 'https://tieba.baidu.com/mo/?\
        word={}&sub4=%E8%BF%9B%E5%90%A7n6=bdISP&tn4=bdKSW&'.format(item)

        self.header = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'


    def parse_url(self,url):

        response = requests.get(url,headers=self.header)
        html_str = response.content.decode()

        return html_str

    def get_info(self,html_str):


    def run(self):
        #1.start_url

        #2.请求
        html_str = self.parse_url(self.start_url)


        #3.提取数据
        content = self.get_info(html_str)

            #1.帖子题目
            #2.帖子图片

        #4.保存

if __name__ == '__main__':
    baidu = BaiduImageSpider()
    baidu.run()