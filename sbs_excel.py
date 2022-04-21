import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 워크북 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['기간', '순위', '프로그램', '시청률'])

for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            # 웹 페이지 가져와서 BeautifulSoup 생성
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, weekIndex)
            response = requests.get(url)
            rating_page = response.text
            soup = BeautifulSoup(rating_page, 'html.parser')

            for tr_tag in soup.select('tr')[1:]:
                # 데이터 행의 채널이 SBS인 경우만 데이터 행 저장
                channel = tr_tag.select_one('td.channel').get_text()
                if channel == 'SBS':
                    # 데이터 행의 기간, 순위, 프로그램, 시청률 저장
                    period = "{}년 {}월 {}주차".format(year, month, weekIndex + 1)
                    td_tags = tr_tag.select('td')
                    rank = td_tags[0].get_text()
                    program = td_tags[2].get_text()
                    percent = td_tags[3].get_text()
                    ws.append([period, rank, program, percent])

wb.save('SBS_데이터.xlsx')