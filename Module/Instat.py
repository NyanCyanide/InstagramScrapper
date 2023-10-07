# Selenium Libraries for Web Scraping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
import os
import json
import time
import csv



class Instat():
    
    def __init__(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Edge(options=options)
        self.once = True
        self.mainuser = ""
        # return self.driver
    
    def loadPage(self, url):
        self.driver.get(url) # Go to the url
        self.hold(8) # Wait for the Page to completely load
        
    def hold(self, seconds):
        time.sleep(seconds)
        
    def saveCookie(self):
        cookie = self.driver.get_cookies()
        with open("./Module/cookie.json", "w") as jsonfile:
            json.dump(cookie, jsonfile)
            
    def deleteCookie(self):
        self.driver.delete_all_cookies()
        
    def tabAction(self, times):
        for i in range(times):
            ActionChains(self.driver)\
                .key_down(Keys.TAB)\
                .perform()
                
    def enterAction(self):
        ActionChains(self.driver)\
            .key_down(Keys.ENTER)\
            .perform()
            
    def tabShiftAction(self, times):
        for i in range(times):
            ActionChains(self.driver)\
                .key_down(Keys.SHIFT)\
                .key_down(Keys.TAB)\
                .perform()
            ActionChains(self.driver)\
                .key_up(Keys.SHIFT)\
                .perform()
    
    def userNameLink(self, link):
        return link.split("/")[-2]
    
    def mainUserProfile(self):
            self.tabAction(9)
            self.enterAction()
            self.hold(5)
            url = self.driver.current_url
            print(url)
            self.mainuser = self.userNameLink(url)
            
    def getFollowers(self, users = None, exhaustlimit = 500):
        if users == None:
            users = [self.mainuser]
        for user in users:
            self.loadPage(f"https://www.instagram.com/{user}") # Didnt access directly to /followers because you wouldnt get the count of followers
            self.tabAction(11)    
            try:
                active = self.driver.switch_to.active_element
                active = active.find_element(By.TAG_NAME, "span")
                active = active.find_element(By.TAG_NAME, "img")
            except:
                active = self.driver.switch_to.active_element
            if active.tag_name == "img":
                self.tabAction(6)
            else:
                self.tabAction(5)
            active = self.driver.switch_to.active_element
            no_followers = active.find_element(By.TAG_NAME, "span").text
            if no_followers[-1] == "M":
                no_followers = int(float(no_followers[:-1]) * 1000000)
            elif no_followers[-1] == "K":
                no_followers = int(float(no_followers[:-1]) * 1000)
            else:
                no_followers = int(no_followers.replace(",", ""))
            
            print(f"User : {user} has {no_followers} followers")
            if no_followers < exhaustlimit:
                exhaustlimit = no_followers
            self.enterAction()
            self.hold(2)
            self.tabAction(1)
            close_button = self.driver.switch_to.active_element
            if user == self.mainuser:
                self.tabAction(1)
                active = self.driver.switch_to.active_element
                if active.tag_name == "input":
                    self.tabAction(1)
            else:
                self.tabAction(1)
                active = self.driver.switch_to.active_element
                if active.tag_name == "input":
                    self.tabAction(1)
                active = self.driver.switch_to.active_element
                try:
                    a = active.find_element(By.TAG_NAME, "img")
                except:
                    a = None
                if a == None:
                    active = self.driver.switch_to.active_element
                    if active.text == self.mainuser:
                        self.tabAction(1)
                else:
                    self.tabAction(1)
                    active = self.driver.switch_to.active_element
                    if active.text == self.mainuser:
                        self.tabAction(1)
                    
            
            # Define Some Variables
            count = 0
            follow = None
            blue = None
            tabs = None
            
            with open(f"./Data/Followers/{user}_followers.csv", mode = "a+", newline = "") as file:
                writer = csv.writer(file)
                writer.writerow(["Profile Name", "Profile Link", "Profile Image Link", "Following", "Blue Check"])
                
                while(count < exhaustlimit):
                    active = self.driver.switch_to.active_element
                    # print("this is a ", active)
                    temp = 0
                    while((active == close_button)):
                        if temp == 5:
                            break;
                        self.tabShiftAction(1)
                        self.hold(2)
                        self.tabAction(1)
                        active = self.driver.switch_to.active_element
                        temp += 1
                        # print(active.text)
                    if temp == 5:
                        break;
                    active = self.driver.switch_to.active_element
                    # print("this is b ", active)

                    try:
                        imgtag = active.find_element(By.TAG_NAME, "img")
                    except:
                        imgtag = None
                    profile_link = active.get_attribute("href")
                    print(active.get_attribute("href"))
                    print(profile_link)
                    profile_name = self.userNameLink(profile_link)
                    
                    if imgtag == None:
                        profile_img = "False"
                        try:
                            blue_check = self.driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                            if blue_check.tag_name == "svg":
                                blue = "True"
                        except:
                            blue = "False"
                        self.tabAction(1)
                        active = self.driver.switch_to.active_element
                        if active.text == "Follow":
                            if user == self.mainuser:
                                tabs = 2
                            else:
                                tabs = 1
                            follow = "False"
                        elif active.text == "Following":
                            follow = "True"
                            tabs = 1
                        else:
                            follow = "True"
                            tabs = 1
                    else:
                        profile_img = imgtag.get_attribute("src")
                        self.tabAction(1)
                        try:
                            blue_check = self.driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                            if blue_check.tag_name == "svg":
                                blue = "True"
                        except:
                            blue = "False"
                        self.tabAction(1)
                        active = self.driver.switch_to.active_element
                        if active.text == "Follow":
                            if user == self.mainuser:
                                tabs = 2
                            else:
                                tabs = 1
                            follow = "False"
                        elif active.text == "Following":
                            follow = "True"
                            tabs = 1
                        else:
                            follow = "True"
                            tabs = 1
                    count += 1
                        
                    writer.writerow([profile_name, profile_link, profile_img, follow, blue])
                    print(f"Profile Name : {profile_name}\nProfile Link : {profile_link}\nProfile Image : {profile_img}\nFollow : {follow}\nBlue Check : {blue}")
                    self.tabAction(tabs)
            close_button.click()
        
    def getFollowing(self, users = None, exhaustlimit = 500):
        if users == None:
            users = [self.mainuser]
        for user in users:
            self.loadPage(f"https://www.instagram.com/{user}") # Didnt access directly to /followers because you wouldnt get the count of followers
            self.tabAction(11)    
            try:
                active = self.driver.switch_to.active_element
                active = active.find_element(By.TAG_NAME, "span")
                active = active.find_element(By.TAG_NAME, "img")
            except:
                active = self.driver.switch_to.active_element
            if active.tag_name == "img":
                print("reached")
                self.tabAction(7)
            else:
                self.tabAction(6)
            active = self.driver.switch_to.active_element
            no_followers = active.find_element(By.TAG_NAME, "span").text
            if no_followers[-1] == "M":
                no_followers = int(float(no_followers[:-1]) * 1000000)
            elif no_followers[-1] == "K":
                no_followers = int(float(no_followers[:-1]) * 1000)
            else:
                no_followers = int(no_followers.replace(",", ""))
            print(f"User : {user} has {no_followers} following")
            if no_followers < exhaustlimit:
                exhaustlimit = no_followers
            self.enterAction()
            self.hold(2)
            self.tabAction(1)
            close_button = self.driver.switch_to.active_element
            if user == self.mainuser:
                self.tabAction(1)
                active = self.driver.switch_to.active_element
                if active.tag_name == "input":
                    self.tabAction(1)
            else:
                self.tabAction(1)
                active = self.driver.switch_to.active_element
                if active.tag_name == "input":
                    self.tabAction(1)
                active = self.driver.switch_to.active_element
                try:
                    a = active.find_element(By.TAG_NAME, "img")
                except:
                    a = None
                if a == None:
                    active = self.driver.switch_to.active_element
                    if active.text == self.mainuser:
                        self.tabAction(1)
                else:
                    self.tabAction(1)
                    active = self.driver.switch_to.active_element
                    if active.text == self.mainuser:
                        self.tabAction(1)
            
            # Define Some Variables
            count = 0
            follow = None
            blue = None
            tabs = None
            
            with open(f"./Data/Following/{user}_following.csv", mode = "a+", newline = "") as file:
                writer = csv.writer(file)
                writer.writerow(["Profile Name", "Profile Link", "Profile Image Link", "Following", "Blue Check"])
                
                while(count < exhaustlimit):
                    active = self.driver.switch_to.active_element
                    # print("this is a ", active)
                    temp = 0
                    while((active == close_button)):
                        if temp == 5:
                            break;
                        self.tabShiftAction(1)
                        self.hold(2)
                        self.tabAction(1)
                        active = self.driver.switch_to.active_element
                        temp += 1
                        # print(active.text)
                    if temp == 5:
                        break;
                    active = self.driver.switch_to.active_element
                    # print("this is b ", active)

                    try:
                        imgtag = active.find_element(By.TAG_NAME, "img")
                    except:
                        imgtag = None
                    profile_link = active.get_attribute("href")
                    # print(active.get_attribute("href"))
                    # print(profile_link)
                    profile_name = self.userNameLink(profile_link)
                    
                    if imgtag == None:
                        profile_img = "False"
                        try:
                            blue_check = self.driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                            if blue_check.tag_name == "svg":
                                blue = "True"
                        except:
                            blue = "False"
                        self.tabAction(1)
                        active = self.driver.switch_to.active_element
                        if active.text == "Follow":
                            if user == self.mainuser:
                                tabs = 2
                            else:
                                tabs = 1
                            follow = "False"
                        elif active.text == "Following":
                            follow = "True"
                            tabs = 1
                        else:
                            follow = "True"
                            tabs = 1
                    else:
                        profile_img = imgtag.get_attribute("src")
                        self.tabAction(1)
                        try:
                            blue_check = self.driver.switch_to.active_element.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "div")
                            blue_check = blue_check.find_element(By.TAG_NAME, "svg")
                            if blue_check.tag_name == "svg":
                                blue = "True"
                        except:
                            blue = "False"
                        self.tabAction(1)
                        active = self.driver.switch_to.active_element
                        if active.text == "Follow":
                            if user == self.mainuser:
                                tabs = 2
                            else:
                                tabs = 1
                            follow = "False"
                        elif active.text == "Following":
                            follow = "True"
                            tabs = 1
                        else:
                            follow = "True"
                            tabs = 1
                    count += 1
                        
                    writer.writerow([profile_name, profile_link, profile_img, follow, blue])
                    # print(f"Profile Name : {profile_name}\nProfile Link : {profile_link}\nProfile Image : {profile_img}\nFollow : {follow}\nBlue Check : {blue}")
                    self.tabAction(tabs)
            close_button.click()

    def login(self):
        if os.path.getsize("./Module/cookie.json") == 0: # If cookie isn't stored
            with open("./Module/config.json", "r") as jsonfile:
                config = json.load(jsonfile)
                username = config["username"]
                password = config["password"]
                self.driver.find_element(By.NAME, "username").send_keys(username)
                self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-").click()
            self.hold(7) # Wait for 7 seconds to load the page properly
            self.saveCookie() # Save the cookie for future use
            
        else:
            self.deleteCookie()
            with open("./Module/cookie.json", "r") as jsonfile:
                cookie = json.load(jsonfile)
                for c in cookie:
                    self.driver.add_cookie(c)
            self.driver.refresh()
            self.hold(7)