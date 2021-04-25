import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

r = requests.get(url);

# To check the status code

# print(r.status_code);

# For the target website

url = 'https://www.youtube.com/c/vahrehvah/videos'

response = requests.get(url);

# To get the entire response of the web page
# print(response.text);

soup = BeautifulSoup(response.text);

print(soup);