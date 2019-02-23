
import requests
from lxml import etree

class QiuBaiSpider():

    def __init__(self):

        self.start_url = 'https://www.qiushibaike.com/text/'

        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Mobile Safari/537.36"}

    def parse_url(self,url):

        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def get_content_list(self,html_str):

        html = etree.HTML(html_str) #etree object

        div_list= html.xpath("//div[contains(@article,'item')]") #分组

        print(div_list)


        content_list = []
        for div in div_list:
            dict={}
            dict['name'] = div.xpath("./div[contains(@class,'author clearfix')//h2/text()]") \
                if len(div.xpath("./div[contains(@class,'author clearfix')//h2/text()]"))>0 else None

            dict['age'] = div.xpath("./div[contains(@class,'author clearfix')/div[@class='articleGender']/text()") \
                if len(div.xpath("./div[contains(@class,'author clearfix')/div[@class='articleGender']/text()"))>0 else None



        return content_list

    def save_content_list(self,content_list):
        file_path = 'qiubai.html'
        with open(file_path,'a') as f:

            f.write(content_list)
            f.write('\n')

    def run(self):
        #1.start_url
        #2.pares_url

        next_url =self.start_url

        while next_url is not None:
            html_str = self.parse_url(next_url)

            #3.get_content_list
            content_list ,next_url = self.get_content_list(html_str)

            #4.save_content_list
            self.save_content_list(html_str)


if __name__ == '__main__':
    qiubai= QiuBaiSpider()
    qiubai.run()