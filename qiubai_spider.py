#coding:utf-8

import requests
from lxml import etree
import pprint

class QiubaiSpider():

    def __init__(self):
        self.url ='https://www.qiushibaike.com/text/'
        self.headers= {

            #这里出了个错误，因为user-agent用的原来的，原来的那个是手机的user，所以导致下面xpath一直出问题
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"

        }

    #page/2/
    def make_url_list(self):

        url_list = [
            self.url
        ]

        i = 2
        url_2_13 = self.url + 'page/{}/'
        while i<14:
            url = url_2_13.format(i)
            url_list.append(url)
            i = i+1
        print(url_list)
        return url_list

    def run(self):
        #1.构造url
        url_list = self.make_url_list()

        for url in url_list:

            #2.发送请求
            rst = requests.get(url,headers=self.headers)
            html_str = rst.content.decode()

            html_str = etree.HTML(html_str)



            span_list = html_str.xpath("//div[@id='content-left']/div")



            for span in span_list:

                dict1 = dict()
                dict1[span_list.index(span)] = span.xpath('.//span/text()') if len(span.xpath('./text()'))>0 else None
                print(dict1)

            break


        #3.分析数据
        #4.保存数据


if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()
