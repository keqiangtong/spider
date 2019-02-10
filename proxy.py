import requests

headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
             AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372\
             Safari/604.1"
        }

proxies = {
    "http":"120.234.138.99:53779"
}

response = requests.get('http://www.baidu.com',proxies=proxies)
print(response.status_code)