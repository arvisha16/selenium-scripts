import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.google.com")

search = browser.find_element(By.NAME, "q")
search.send_keys("Python script for web pages login")
search.send_keys(Keys.RETURN)  # hit return after you enter search text
time.sleep(10)  # sleep for 5 seconds so you can see the results

search = browser.find_element(By.NAME, "q")
search.send_keys("Selenium python script for web pages button clicks")
search.send_keys(Keys.RETURN)  # hit return after you enter search text
browser.quit()
browser.__exit__
