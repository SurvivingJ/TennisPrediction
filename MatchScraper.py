from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup
from time import sleep
from lxml import html
import requests
from scraper_tools import bot_sleep
# Driver Setup
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
#options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')


def sportsbet_scraper_tennis():
    # Open website
    driver.get('https://www.sportsbet.com.au/betting/tennis')
    print("Driver invoked")
    sleep(bot_sleep(5, 10, True))
    # Collect page data
    url = str(driver.current_url)
    page = requests.get(url)
    player_list = []
    i = 1

    # Today's matches
    while True:
        try:
            player_1 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[3]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[1]/ul/li[{str(i)}]/div/div/div/div/div[1]/div/div/div/div/button/div/div/div/span/div/span')
            player_2 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[3]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[1]/ul/li[{str(i)}]/div/div/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/span')
            player_1 = player_1.text.split()
            player_2 = player_2.text.split()
            if len(player_1[0]) > 1:
                player_1_name = player_1[1] + ' ' + player_1[0][0] + '.'
            else:
                player_1_name = player_1[1] + ' ' + player_1[0] + '.'
            if len(player_2[0]) > 1:
                player_2_name = player_2[1] + ' ' + player_2[0][0] + '.'
            else:
                player_2_name = player_2[1] + ' ' + player_2[0] + '.'

            player_list.append((player_1_name, player_2_name))
            i += 1
        except:
            break

    # Tomorrow's matches
    i = 1
    while True:
        try:
            player_1 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[3]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[2]/ul/li[{str(i)}]/div/div/div/div/div[1]/div/div/div/div/button/div/div/div/span/div/span')
            player_2 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[3]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[2]/ul/li[{str(i)}]/div/div/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/span')
            player_1 = player_1.text.split()
            player_2 = player_2.text.split()
            player_1_name = player_1[1] + ' ' + player_1[0] + '.'
            player_2_name = player_2[1] + ' ' + player_2[0] + '.'
            player_list.append((player_1_name, player_2_name))
            i += 1
        except:
            break
    return player_list

def close_driver():
    driver.close()
    return True


