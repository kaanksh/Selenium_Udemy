from selenium import webdriver

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.get("https://google.com")
searchBox = driver.find_element_by_name("q")
searchBox.send_keys("Akanksha")
