from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com")

print(driver.title)

driver.quit()