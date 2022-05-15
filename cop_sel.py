import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome('/Users/nhn/Downloads/chromedriver', options=options)
driver.implicitly_wait(3)


# 쿠팡 '커피' 검색 결과 페이지 접속
driver.get('https://www.coupang.com/np/search?component=&q=%EC%BB%A4%ED%94%BC&channel=user')
time.sleep(1)

products = driver.find_elements_by_css_selector('li.search-product')

# 검색 결과 페이지로 계속 돌아올 것이기 때문에 저장해 놓기
search_result_window = driver.current_window_handle

for product in products:
    # 아이템 클릭
    product.click()
    time.sleep(1)

    # 아이템 상세 페이지로 포커스 이동
    driver.switch_to.window(driver.window_handles[1])

    # 아이템 상세 페이지에서 필요한 정보 가져오기

    # 아이템 상세 페이지 닫기
    driver.close()

    # 검색 결과 페이지로 포커스 이동 - 그래야 아이템 (product)를 클릭할 수 있음
    driver.switch_to.window(search_result_window)

driver.quit()