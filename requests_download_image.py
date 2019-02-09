def main():
	import requests

	response = requests.get('http://flask.pocoo.org/docs/1.0/_static/flask.png')

        

	with open('a.png','wb') as f:
            f.write(response.content)


if __name__ =='__main__':
	main()
