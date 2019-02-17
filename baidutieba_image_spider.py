#coding:utf-8

import requests
from lxml import etree
import json

class BaiduImageSpider():

    def __init__(self,item):
        self.name = item
        self.start_url = 'https://tieba.baidu.com/mo/?\
        word={}&sub4=%E8%BF%9B%E5%90%A7n6=bdISP&tn4=bdKSW&'.format(item)

        self.header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

        self.tieba_url = 'https://tieba.baidu.com'

    def parse_url(self,url):

        response = requests.get(url,headers=self.header)


        return response.content

    def get_info(self,html_str):
       
        html = etree.HTML(html_str)


        html_list = html.xpath("//div[@class='i']")

        content_list = []
        for html in html_list:

            dict={}
            dict['title'] = html.xpath('./a/text()')[0] if len(html.xpath('./a/text()'))>0 else None
            dict['link'] = self.tieba_url + html.xpath('./a/@href')[0] if len(html.xpath('./a/@href')) >0 else None
            dict['image'] = self.get_image(dict['link'],[])
            content_list.append(dict)

        # next_url = html.xpath('//')
        return content_list

    def get_image(self,tiezi_url,total_list):

        tiezi_response  = requests.get(tiezi_url,headers=self.header)
        tiezi_response = tiezi_response.content

        html = etree.HTML(tiezi_response)
        image_list = html.xpath("//div[@class = 'i']/a[text()='图']/@href")

        total_list.append(image_list)

        next_url =  'https://tieba.baidu.com/mo/q---6A29DCC617E1619862D39261DFDBD601%3AFG%3D1--1-3-0--2--wapp_1550366534614_187/'+html.xpath("//a[text()='下一页']/@href")[0] if len(html.xpath("//a[text()='下一页']"))>0 else None

        if next_url is not None:
            return self.get_image(next_url,total_list)

        return total_list


    
    def save_info(self,content_list):
        file_path = self.name +'.txt'
        with open(file_path,'a',encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write('\n')

    def run(self):
        #1.start_url

        #2.请求
        html_str = self.parse_url(self.start_url)


        #3.提取数据
        content_list = self.get_info(html_str)

            #1.帖子题目
            #2.帖子图片

        #4.保存
        self.save_info(content_list)

if __name__ == '__main__':
    baidu = BaiduImageSpider('猫')
    baidu.run()