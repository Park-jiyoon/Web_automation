import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/nhn/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/orangebottle/index')
time.sleep(1)

branch_infos = []

# 모든 지점에 대한 태그 가져오기

for branch in driver.find_elements_by_css_selector('div.branch'):
    # 각 태그에서 지점 이름, 전화번호 가져오기
    branch_name = branch.find_element_by_css_selector('p.city').text
    address = branch.find_element_by_css_selector('p.address').text
    phone_number = branch.find_element_by_css_selector('span.phoneNum').text
    branch_infos.append([branch_name, address, phone_number])

# 출력 코드
print(branch_infos)

driver.quit()