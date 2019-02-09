
import requests

class TiebaSpider(object):

    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}&pn={}'
        self.headers={
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
             AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372\
             Safari/604.1"
        }

    def make_url_list(self):

        return [ self.url.format(self.tieba_name,i*50) for i in range(200)]



    def save(self,response,index):
        #李毅-第1页.html
        save_dir ="{}-第{}页.html".format(self.tieba_name,index)
        with open(save_dir,'w') as f:
            f.write(response.text)
        print(save_dir)

    def run(self):
        #构造请求列表
        req_lists = self.make_url_list()

        #主要逻辑
        for req in req_lists:
            response = requests.get(req,headers=self.headers)
            #保存
            page_num = req_lists.index(req) + 1
            self.save(response,page_num)


if __name__ == '__main__':
    liyi = TiebaSpider('李毅')
    liyi.run()
