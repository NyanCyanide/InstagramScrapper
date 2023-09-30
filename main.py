# import necssary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import time
import csv

# fill these two lines username and password
username = "username"
password = "password"


exhaustlimit = 500

def tabAndEnter(num, activate=True):
    for i in range(num):
        ActionChains(driver)\
            .key_down(Keys.TAB)\
            .perform()\
        
    if activate:
        ActionChains(driver)\
            .key_down(Keys.ENTER)\
            .perform()\


def getProfileName(link):
    return link.split("/")[-1]

## Initiate the driver and start running
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized") ## Mazimises the screen
options.add_experimental_option("detach", True) ## Detaches the browser from the code
options.add_argument("--disable-notifications")
driver = webdriver.Edge(options=options) ## Create driver


## Login Window
driver.get('http://instagram.com')
sleep(2)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-").click()
sleep(7)

## Go to Profile Section
tabAndEnter(9)

sleep(5)

## Followers Screen
tabAndEnter(4, False)
active = driver.switch_to.active_element
no_followers = int(active.find_element(By.TAG_NAME, "span").get_attribute("title"))
print(no_followers)
if no_followers < exhaustlimit:
    exhaustlimit = no_followers
tabAndEnter(0)
sleep(2)
tabAndEnter(1, False)
close_button = driver.switch_to.active_element
tabAndEnter(2, False)

def scrapeFollowers():
    count = 0
    # bad = 10
    tabs = None
    with open("./followers.csv", mode="a+", newline="") as file:
        writer = csv.writer(file)
        
        while(count != exhaustlimit):
            active = driver.switch_to.active_element

                
            print(active, active.tag_name)
            if active.tag_name == "button":
                ActionChains(driver)\
                .key_down(Keys.SHIFT)\
                .key_down(Keys.TAB)\
                .perform()
                ActionChains(driver)\
                .key_up(Keys.SHIFT)\
                .perform()
                sleep(2)
                tabAndEnter(1, False)
            
            active = driver.switch_to.active_element
            try:
                # if image tag is present
                imgtag = active.find_element(By.TAG_NAME, "img")
            except:
                # if not present
                imgtag = None
            profile_link = active.get_attribute("href")[:-10] # gets profile link
            profile_name = getProfileName(profile_link)
            
            if imgtag == None:
                imgtag = "False"
                profile_img = None
                tabAndEnter(1, False)
                active = driver.switch_to.active_element
                print(active.text)
                print(active)
                if active.text == "Follow":
                    print("reached")
                    tabs = 2
                else:
                    tabs = 1
            else:
                profile_img = imgtag.get_attribute("src")
                tabAndEnter(2, False)
                active = driver.switch_to.active_element
                if active.text == "Follow":
                    tabs = 2
                else:
                    tabs = 1
            count += 1

            writer.writerow([profile_name, profile_link, profile_img])
            print(f"Profile Name: {profile_name}\nProfile Link: {profile_link}\nProfile Image: {profile_img}")
            tabAndEnter(tabs, False)
            
    close_button.click()
    
driver.__exit__()