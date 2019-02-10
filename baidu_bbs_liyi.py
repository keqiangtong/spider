
import requests
def main():

    pn = 0
    spider(pn)
    print('*'*1000)
    
    pn = 50
    while pn < 200:
        spider(pn)
        pn += 50
        print('?'*1000)

def spider(pn):
    
    url = 'https://tieba.baidu.com/f?kw={}&pn={}'.format('李毅',pn)
    headers={
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
            }
    response = requests.get(url,headers=headers)
    print(response.content)
    




if __name__=='__main__':
    main()
