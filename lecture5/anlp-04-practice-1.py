import requests
import sys

if __name__=="__main__":
	url = sys.argv[1]
	#url = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid=dj00aiZpPUZZa3pmS1F3NDdnVyZzPWNvbnN1bWVyc2VjcmV0Jng9YTM-&genre_category_id=635&sort=-sold"
	response = requests.get(url)
	sys.stdout.buffer.write(response.content)