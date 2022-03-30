from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome('/Users/nhn/Downloads/chromedriver')

driver.get('https://codeit.kr')