import requests
import bs4

base_url = "http://books.toscrape.com/"

raw_data = requests.get(base_url)
arranged_data = bs4.BeautifulSoup(raw_data.text,'lxml')
categories = arranged_data.select('.side_categories')[0]('a')
for category in categories:
    print(category.text)
