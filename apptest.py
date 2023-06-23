import tkinter as tk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time
import json
from src.instadm import InstaDM
from tkinter import *

# Top level window
frame = tk.Tk()
frame.title("Amr Zhwh instagram bot")
frame.geometry('800x800')
# Function for getting Input
# from textbox and printing it
# at label widget
def sleep_for_period_of_time():
    limit = random.randint(7,10)
    time.sleep(limit)

f = open('infos/accounts.json',)
accounts = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]


for account in accounts:    
   user = account["username"]
   pwd = account["password"]
  

def follow():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    time.sleep(5)

    


    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    # not_now = browser.find_element_by_xpath("//div[@class='cmbtv']/button")
    # not_now.click()
    # sleep_for_period_of_time()

    tra = trackingName.get(1.0, "end-1c")
    browser.get(f"https://www.instagram.com/{tra}")
    sleep_for_period_of_time()

    followers_link = browser.find_element_by_xpath("//ul/li[2]/a")
    followers_link.click()
    sleep_for_period_of_time()

    inp = inputtxt.get(1.0, "end-1c")

    while(True):
        try:
            i = 0

            list_of_followers = browser.find_elements(By.XPATH, '//button/div/div[contains(text(), "Follow")]')
            for person in list_of_followers:
                if person.text == "Follow":
                        person.click()
                        time.sleep(5)
                        print("Followed!")
                        i +=1
                        print(i)
                        sleep_for_period_of_time()
                else:
                    pass
                if i >= int(inp):
                    break
              
           
           

            users_followers = set()        
            browser.execute_script("arguments[0].scrollIntoView(true);", list_of_followers[i])
            texte =  browser.find_elements(By.XPATH, '//div/div/div/span/a/span/div')
            n = 0
            for f in texte: 
                if n <= int(inp):
                    print(f.text)
                    n +=1
                    users_followers.add(f.text)
                else:
                    break

            with open('infos/usernames.txt', 'w') as file:
                file.write('\n'.join(users_followers) + "\n")
 
            answer = input("The programm finished! Click on 'e' to exit.. ")
            if answer.lower().startswith("e"):
                browser.quit()
                exit()

        except Exception as e:
            print(e)


def unfollowBySevedAccounts():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    time.sleep(5)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    # not_now = browser.find_element_by_xpath("//div[@class='cmbtv']/button")
    # not_now.click()
    # sleep_for_period_of_time()
    for userr in usernames:
       if not usernames:
            break
       ig_user = userr
       browser.get(f"https://www.instagram.com/{ig_user}")
       sleep_for_period_of_time()
       followers_link = browser.find_element_by_xpath("//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abb0 _abcm']/button[@class='_acan _acap _acat']")
       followers_link.click()
       sleep_for_period_of_time()
       unfollow_button = browser.find_element_by_xpath("//button[@class='_a9-- _a9-_']")
       unfollow_button.click()
       sleep_for_period_of_time()
       break

    answer = input("The programm finished! Click on 'e' to exit.. ")
    if answer.lower().startswith("e"):
        browser.quit()
        exit()

def like():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    sleep_for_period_of_time()

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    tra = trackingName.get(1.0, "end-1c")
    browser.get(f"https://www.instagram.com/{tra}")
    sleep_for_period_of_time()

    first_pic = browser.find_element_by_xpath("//article[@class='_aayp']/div/div/div[1]/div[1]/a")
    first_pic.click()

    inp = inputtxt.get(1.0, "end-1c")
    sleep_for_period_of_time()

    for i in range(int(inp)):

        # Like a post 
        like_post = browser.find_element_by_xpath("//div[@class= '_abm0 _abl_']")
        like_post.click()
        print("Liked!")
        sleep_for_period_of_time()

        #Move on to the next Post
        next_post = browser.find_element_by_xpath("//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']")
        next_post.click()
        print("post " + str(i) + " done!")
        print("Next!")
        sleep_for_period_of_time()

    #Quit the Program
    answer = input("The programm finished! Click on 'e' to exit.. ")
    if answer.lower().startswith("e"):
        browser.quit()
        exit()

def likeStory():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    time.sleep(5)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()
    browser.get("https://www.instagram.com")
    inp = inputtxt.get(1.0, "end-1c")

    sleep_for_period_of_time()

    followers_link = browser.find_element_by_xpath("//li[@class='_acaz']")
    followers_link.click()

    i = 0
    while i < int(inp):
      sleep_for_period_of_time()
      followers_linkk = browser.find_element_by_xpath("//div[@class='_abm0 _abl_']")
      followers_linkk.click()
      i +=1    
      if i < int(inp):
        browser.quit()
        exit()
    answer = input("The programm finished! Click on 'e' to exit.. ")
    if answer.lower().startswith("e"):
        browser.quit()
        exit()

def comment():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    sleep_for_period_of_time()

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    tra = trackingName.get(1.0, "end-1c")
    browser.get(f"https://www.instagram.com/{tra}")
    sleep_for_period_of_time()

    first_pic = browser.find_element_by_xpath("//article[@class='_aayp']/div/div/div[1]/div[1]/a")
    first_pic.click()

    inp = inputtxt.get(1.0, "end-1c")
    cmmt = commment.get(1.0, "end-1c")
    sleep_for_period_of_time()

    for i in range(int(inp)):


        #Comment on a post
        cmmt_post = browser.find_element_by_xpath("//form/textarea[@class='xnalus7']")
        cmmt_post.click()
        cmmt_post.send_keys(cmmt)
        cmmt_post.send_keys(Keys.ENTER)
        print("Commented!")
        time.sleep(5)

        
        #Move on to the next Post
        next_post = browser.find_element_by_xpath("//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']")
        next_post.click()
        print("post " + str(i) + " done!")
        print("Next!")
        sleep_for_period_of_time()

    #Quit the Program
    answer = input("The programm finished! Click on 'e' to exit.. ")
    if answer.lower().startswith("e"):
        browser.quit()
        exit()

def sendMessagee():
   while True:
    if not usernames:
        print('Finished usernames.')
        break
    
    inp = inputtxt.get(1.0, "end-1c")

    for account in accounts:
        if not usernames:
            break
        # Auto login
        insta = InstaDM(username=account["username"],
                        password=account["password"], headless=False)

        for i in range(inp):

            if not usernames:
                break

            username = usernames.pop()
            # Send message
            insta.sendMessage(
                user=username, message=random.choice(messages))

        insta.teardown()


# Label Creation
sum_label0 = tk.Label(text="saved names:")
sum_label0.pack()
lbl = tk.Label(frame, text = "")
lbl.pack()

sum_label1 = tk.Label(text="how many:")
sum_label1.pack()

# TextBox Creation
inputtxt = tk.Text(frame,
				height = 5,
				width = 20)

inputtxt.pack()

sum_label2 = tk.Label(text="traking name:")
sum_label2.pack()

trackingName = tk.Text(frame,
				height = 5,
				width = 20)

trackingName.pack()

sum_label3 = tk.Label(text="comment:")
sum_label3.pack()

commment = tk.Text(frame,
				height = 5,
				width = 20)
commment.pack()

# Button Creation
likeStoryButton = tk.Button(frame,
						text = "likeStory : need to 'how many' !!!! ",
						command = likeStory)
likeStoryButton.pack()

followButton = tk.Button(frame,
						text = "follow and save names : need to 'how many' && 'traking name' !!!!",
						command = follow)
followButton.pack()

unfollowBySevedAccountsButton = tk.Button(frame,
						text = "Unfollow Saved Names",
						command = unfollowBySevedAccounts)
unfollowBySevedAccountsButton.pack()

likeButton = tk.Button(frame,
						text = "like : need to 'how many' && 'traking name' !!!!",
						command = like)
likeButton.pack()

sendMessageeButton = tk.Button(frame,
						text = "send Message Saved Names : need to 'how many' !!!!",
						command = sendMessagee)
sendMessageeButton.pack()

commentButton = tk.Button(frame,
						text = "comment : need to 'how many' && 'traking name' && 'comment' !!!!",
						command = comment)
commentButton.pack()
def main():
  with open("infos/usernames.txt", "r") as f:
    lbl.config(text=f.read())  
if __name__ == "__main__":
    main()

frame.mainloop()
