from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=opt)

driver.get("https://shopee.vn")
#wait = WebDriverWait(driver, 10)
#implicit wait
driver.implicitly_wait(20)
search_input = driver.find_element(By.CLASS_NAME,'shopee-searchbar-input__input')
#search_input = driver.find_element(By.XPATH, '//*[@id="main"]/div/header/div[2]/div/div[1]/form/div/div[1]/input')
#search_input.clear()
search_input.send_keys("củ sen mini")

search_button = driver.find_element(By.CLASS_NAME,'class="shopee-svg-icon"')

search_button.click()
print("Page title is: ")
print(driver.title)