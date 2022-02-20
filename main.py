from twitchAPI.twitch import Twitch
import datetime
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def TwitchLoginToId(twitch, logins):
    ids = []
    temp = twitch.get_users(logins=logins)['data']
    for i in range(len(logins)):
        ids.append(temp[i]['id'])
    return ids

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument("--incognito")
options.add_argument("--nogpu")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,1280")
options.add_argument("--no-sandbox")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(executable_path=r"C:\Users\GigaKOX\Downloads\chromedriver.exe", options=options)
twitch = Twitch('IDkey', 'OAuthkey')
#print(twitch.get_clips(clip_id='ResilientProductiveQueleaOMGScoots-FUKbEuFt6_wFysK6'))
weekago = datetime.datetime.now() - datetime.timedelta(days=7)
#print(weekago)
ids = TwitchLoginToId(twitch, ["overpow", "kubon_"])
#print(twitch.get_users(logins=['kubon_']))
for x in range(0, len(ids)):

    clips = twitch.get_clips(broadcaster_id=ids[x], first=5,started_at=weekago)
    for i in range(0, 5):
        url = str(clips["data"][i]['url'])
        title = clips["data"][i]["title"]
        duration = clips["data"][i]["duration"]
        author = clips["data"][i]['broadcaster_name']
        if duration >= 10:
            print(clips["data"][i])
            driver.get(url)
#print(driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div/div/main/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/video').get_attribute('innerHTML'))


            time.sleep(2)
            elem = driver.find_elements(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[3]/div/div/main/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/video')
            urlmp4 = elem[0].get_attribute('src')
            r = requests.get(urlmp4)
            with open("outs\{}_{}.mp4".format(author, title), 'wb') as f:
                f.write(r.content)
driver.close()
#print(twitch.get_clips(broadcaster_id='kubon_',first=5))
#3jy5egzh9z8ktp6xqk5ptxm58ti93o
