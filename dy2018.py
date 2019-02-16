from parse_url import parse_url


class Dy2018Spider():
    def __init__(self):
        pass


    def run(self):
        html_str  = parse_url('http://www.dy2018.com')
        print(html_str)


if __name__ == '__main__':
   dy = Dy2018Spider()
   dy.run()