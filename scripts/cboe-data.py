from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(options=option)
browser.implicitly_wait(15)
url="https://www.cboe.com/us/options/market_statistics/historical_data/"
browser.get(url)