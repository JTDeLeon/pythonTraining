# Selenium Tutorial #1 
# https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("Test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_class_name("g")
    for article in articles: 
        header = article.find_element_by_tag_name("h3")
        print(header.text)
finally:
    driver.quit()



# print(main.text)
# print(driver.page_source)

# time.sleep(5)

# driver.quit()