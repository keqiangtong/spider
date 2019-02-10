
import requests
import json
class BaiduTranslate():

    def __init__(self,trans_str):

        self.trans_str = trans_str
        self.lan_detect_url = 'https://fanyi.baidu.com/langdetect'
        self.lan_detect_data = {"query":self.trans_str}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
                     AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372\
                     Safari/604.1"
        }

    def send_post(self,url,data):

        response =requests.post(url,data=data,headers = self.headers)
        return json.loads(response.content.decode())

    def run(self):
        #1. 检测语言
            #1.post_url,post_data
            #2.发送post请求
        rst_dict = self.send_post(url=self.lan_detect_url,data=self.lan_detect_data)

            #3.解析结果
        if rst_dict.get('lan') == 'en':
            data = {"query": self.trans_str,"from": "en", "to": "zh"}
        else:
            data = {"query": self.trans_str,"from": "zh", "to": "en"}
        #2.发送post

        rst = self.send_post('https://fanyi.baidu.com/basetrans',data=data )

        print(rst)
        print(rst['trans'][0]['dst'])

        #3.解析结果



if __name__ == '__main__':

    baidutranslate = BaiduTranslate('好')
    baidutranslate.run()