import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
musics = soup.select('table.list-wrap > tbody > tr')
rank = 0
for music in musics:
    title = music.select_one('a.title.ellipsis')
    artist = music.select_one('a.artist.ellipsis')
    # 공백제거
    title = title.text.strip()
    artist = artist.text.strip()
    if len(title) > 0:
        rank+=1
    print(rank,title,artist)