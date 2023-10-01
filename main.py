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

def scrapeFollowers():
    exhaustlimit = 500
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
    count = 1
    # bad = 10
    follow = None
    tabs = None
    blue = None
    with open("./followers.csv", mode="a+", newline="") as file:
        writer = csv.writer(file)
        
        while(count < exhaustlimit):
            active = driver.switch_to.active_element

                
            # print(active, active.tag_name)
            while active.tag_name == "button" and active.text != "Remove":
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
                # imgtag = "False"
                profile_img = "False"
                try:
                    blue_check = driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                    if blue_check.tag_name == "svg":
                        blue = "True"
                except:
                    blue = "False"
                tabAndEnter(1, False)
                active = driver.switch_to.active_element
                # print(active.text)
                # print(active)
                if active.text == "Follow":
                    # print("reached")
                    follow = "False"
                    tabs = 2
                else:
                    follow = "True"
                    tabs = 1
            else:
                profile_img = imgtag.get_attribute("src")
                tabAndEnter(1, False)
                try:
                    blue_check = driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                    if blue_check.tag_name == "svg":
                        blue = "True"
                except:
                    blue = "False"
                tabAndEnter(1, False)
                active = driver.switch_to.active_element
                if active.text == "Follow":
                    follow = "False"
                    tabs = 2
                else:
                    follow = "True"
                    tabs = 1
            count += 1

            writer.writerow([profile_name, profile_link, profile_img, follow, blue])
            print(f"Profile Name: {profile_name}\nProfile Link: {profile_link}\nProfile Image: {profile_img}\n Follow: {follow}\n Blue Check: {blue}")
            tabAndEnter(tabs, False)
    
    file.close()
    close_button.click()
    
    
def scrapeFollowing():
    exhaustlimit = 500
    tabAndEnter(1, False)
    no_following = int(driver.switch_to.active_element.find_element(By.TAG_NAME, "span").get_attribute("title"))
    if no_following < exhaustlimit:
        exhaustlimit = no_following
    sleep(2)
    print("reached")
    count = 1
    tabAndEnter(1, False)
    close_button = driver.switch_to.active_element
    tabs = None
    blue = None
    tabAndEnter(2, False)
    with open("./following.csv", mode="a+", newline="") as file:
        writer = csv.writer(file)
        
        while(count <= exhaustlimit):
            active = driver.switch_to.active_element
            
            while active.tag_name == "button" and active.text !=    "Following":
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
                profile_img = "False"
                try:
                    blue_check = driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                    if blue_check.tag_name == "svg":
                        blue = "True"
                except:
                    blue = "False"
                tabAndEnter(2, False)
            else:
                profile_img = imgtag.get_attribute("src")
                tabAndEnter(1, False)
                try:
                    blue_check = driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "div")
                    blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                    if blue_check.tag_name == "svg":
                        blue = "True"
                except:
                    blue = "False"
                tabAndEnter(2, False)
            count += 1
                
            writer.writerow([profile_name, profile_link, profile_img, blue])
            print(f"Profile Name: {profile_name}\nProfile Link: {profile_link}\nProfile Image: {profile_img}\n Blue Check: {blue}")
            
    file.close()
    close_button.click()
            
scrapeFollowers()
sleep(2)
scrapeFollowing()
driver.quit()