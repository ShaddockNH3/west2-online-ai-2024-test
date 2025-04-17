import requests
url = "https://movie.douban.com/subject/26363254/comments?status=P"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

html = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")

comment_contents = soup.find_all('span', class_='short')
for comment in comment_contents:
    print(comment.text.strip())