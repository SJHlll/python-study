from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs

# 뷰티풀수프 임포트
from bs4 import BeautifulSoup

d = datetime.today()

file_path = f'C:/MyWorkspace/upload/멜론일간차트순위_{d.year}년_{d.month}월_{d.day}일_{d.hour}시 기준.txt'

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해 주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)

driver.get('https://www.melon.com/chart/index.htm')

with codecs.open(file_path, mode='w', encoding='utf-8') as f:

  soup = BeautifulSoup(driver.page_source, 'html.parser')

  for cnt in [50, 100]:
    table_list = soup.select(f'.lst{cnt}')

    for table in table_list:
      song_rank = table.select_one('div.wrap.t_center').text.strip()
      song_title = table.select_one('div.wrap div.ellipsis.rank01 > span > a').text.strip()
      song_singer = table.select_one('div.wrap div.ellipsis.rank02 > a').text.strip()
      song_album = table.select_one('div.wrap div.ellipsis.rank03 > a').text.strip()

      f.write(f'# 순위 : {song_rank}\n')
      f.write(f'# 곡 제목 : {song_title}\n')
      f.write(f'# 가수 : {song_singer}\n')
      f.write(f'# 앨범 : {song_album}\n')
      f.write('--------------------\n')

driver.close()