# 네이버 뷰탭 - 블로그 정보 가져오기
# 블로그 랭킹, 저자, 제목, 링크

import requests
from bs4 import BeautifulSoup

keyword = input('키워드를 입력하세요. : ')
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={keyword}'
headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

items = soup.select('.view_wrap')

blog_infos = []
rank = 1

for item in items:
  add = item.select('.spblog.ico_ad')
  if add:
    continue

  author = item.select_one('.name').text
  title = item.select_one('.title_link').text
  link = item.select_one('.title_link')['href']

  blog_infos.append({
    "rank": rank,
    "author": author,
    "title": title,
    "link": link,
  })

  rank += 1