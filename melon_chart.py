# 멜론 차트 - 멜론 top100 정보 가져오기
# 아티스트, 앨범, 곡 제목, 아티스트 채널 링크, 앨범 정보 링크

import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
request = requests.get(url, headers=headers)
soup = BeautifulSoup(request.text, 'html.parser')

def get_link(category, href):
  if category == 'album':
    base_url = 'https://www.melon.com/album/detail.htm?albumId='
  elif category == 'artist':
    base_url = 'https://www.melon.com/artist/timeline.htm?artistId='
  else:
    return None

  url_id = ('').join([letter for letter in href if letter.isdigit()])
  link = base_url + url_id

  return link

items = soup.select('.lst50, .lst100')
infos = []

for rank, item in enumerate(items, start=1):
  title_text = item.select_one('.ellipsis.rank01 a').text

  artist = item.select_one('.ellipsis.rank02 > a')
  artist_text = artist.text
  artist_href = artist['href']
  artist_link = get_link('artist', artist_href)

  album = item.select_one('.ellipsis.rank03 > a')
  album_text = album.text
  album_href = album['href']
  album_link = get_link('album', album_href)

  infos.append({
    'song_title': title_text,
    'artist_name': artist_text,
    'artist_link': artist_link,
    'album_name': album_text,
    'album_link': album_link 
  })  