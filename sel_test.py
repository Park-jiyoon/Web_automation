#selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome('/Users/nhn/Downloads/chromedriver')
driver.implicitly_wait(3)


driver.get('https://workey.codeit.kr/costagram/index')

driver.find_element_by_css_selector('.top-nav__login-link').click()

driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')

driver.find_element_by_css_selector('.login-container__login-button').click()


