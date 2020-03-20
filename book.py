# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from time import sleep

"""DRIVERS"""# Don't mess with this part if you don't know what you are doing.
driver = webdriver.Chrome(r'C:\Users\DELLL\Downloads\chromedriver_win32\chromedriver.exe') # Chrome driver
driver.get("https://libgen.is/") # URL of the site

name = "atkins physical chemistry"
inp = driver.find_element_by_id('searchform')
inp.send_keys(name)
inp.send_keys(Keys.RETURN)

top_result = driver.find_elements_by_xpath('//*[(@id)]')[2] # Returns top result
top_result.click()

torrent_link = driver.find_elements_by_xpath("//td[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]//a")[0]
torrent_link.click()