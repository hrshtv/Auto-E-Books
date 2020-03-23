# Imports
import os
import glob
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from difflib import get_close_matches as gcm
from selenium.webdriver.common.keys import Keys

# Extracts the title from a string containing some extra data
def title_extractor(text):
    ind = text.find("[")
    return text[:ind]

"""CUSTOMIZE"""

download_path = r"C:\Users\DELLL\OneDrive\Desktop\E-Books\\" # Enter the path where you want the book to be downloaded
name = "hall and knight algebra" # Enter the correct title of the book you want
save_as = name + ".torrent" # The name of the file in the folder

# Don't mess with these parts if you don't know what you are doing.
"""DRIVERS-AND-OPTIONS""" 
options = webdriver.ChromeOptions()
options.add_argument("--headless") # chrome windows open in the background
prefs = { "download.default_directory": download_path, "directory_upgrade": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome( options = options) # Chrome driver
driver.get("https://libgen.is/") # URL of the website

name.strip()
inp = driver.find_element_by_id('searchform')
inp.send_keys(name)
inp.send_keys(Keys.RETURN) # Press enter to search

main_url = driver.current_url
driver.close() # Close current window
page = requests.get(main_url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.select("a[title='']") # Selecting all the books obtained after the search
n = len(results)

if n: # If we obtain any results
    titles = []
    links = []
    
    for r in results:
        
        link = "http://libgen.is/" + r['href']
        links.append(link)
        
        title = r.text
        titles.append(title)
        
    titles = [title_extractor(i).strip() for i in titles] # List-Comprehension
    closest = gcm(name,titles,cutoff = 0,n=1)[0] # Closest match to the entered book name
    index = titles.index(closest)
    link = links[index]
    
    driver = webdriver.Chrome(options=options) # Open new browser window in the background
    driver.get(link) # URL of the site where the E-book resides
    
    download = driver.find_element_by_xpath('//td[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]//a')
    download.click()

    sleep(3) # Time taken to download
    driver.close() # Close the window
    
    """RENAMING THE FILE AND STORING"""
    new_path = download_path + save_as
    list_of_files = glob.glob(download_path + "*.torrent")
    latest_file = max(list_of_files, key=os.path.getctime)
    os.rename(latest_file, new_path)
    
else:
    print("Sorry, the book you want isn't available! Please recheck whether your input matches the actual title")