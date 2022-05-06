import time
from selenium import webdriver
from openpyxl import Workbook

# 웹 드라이버 설정
driver = webdriver.Chrome('/Users/nhn/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)


# 워크북 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['이미지 주소', '내용', '해시태그', '좋아요 수','댓글 수'])
# 로그인
driver.find_element_by_css_selector('.top-nav__login-link').click()
time.sleep(1)

driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')

driver.find_element_by_css_selector('.login-container__login-button').click()
time.sleep(1)

# 페이지 끝까지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 모든 썸네일 요소 가져오기
posts = driver.find_elements_by_css_selector('.post-list__post')

for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 이미지 주소 가져오기
    style_attr = driver.find_element_by_css_selector('.post-container__image').get_attribute('style')
    image_url = style_attr.split('"')[1]
    #나머지 주소 가가져오기
    content = driver.find_element_by_css_selector('content__text').text.strip()
    hashtags = driver.find_element_by_css_selector('content__tag-cover').text.strip()
    like_count = driver.find_element_by_css_selector('content__like-count').text.strip()
    comment_count = driver.find_element_by_css_selector('content__comment-count').text.strip()
    ws.append([image_url, content, hashtags, like_count, comment_count])
    # 닫기 버튼 클릭
    driver.find_element_by_css_selector('.close-btn').click()
    time.sleep(0.5)

driver.quit()
wb.save('코스타그램.xlsx')