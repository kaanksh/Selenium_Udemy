from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path  ="../drivers/chromedriver.exe")
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_tag_name("q").send_keys("Automation step by step")
driver.find_element_by_tag_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()
print("Completed")
