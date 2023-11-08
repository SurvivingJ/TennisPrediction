from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup
from time import sleep
from lxml import html
import requests
from scraper_tools import bot_sleep
import csv
from selenium.webdriver.common.proxy import Proxy, ProxyType

def sportsbet_scraper_tennis():
    # Driver Setup
    options = Options()
    options.add_argument("user-agent=Chrome/84.0.4147.135")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')

    # Open website
    driver.get('https://www.sportsbet.com.au/betting/tennis')
    print("Driver invoked")
    sleep(bot_sleep(5, 10, True))
    upcoming_matches_btn = driver.find_element_by_xpath('/html/body/span/div/div/div[2]/div/div[3]/div/div/div[1]/nav/div[3]/ul/li[2]/div/div/button/div/div/span')
    upcoming_matches_btn.click()
    # Collect page data
    url = str(driver.current_url)
    page = requests.get(url)
    player_list = []
    i = 1
    k = 1
    # Today's matches
    while True:
        try:
            player_1 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[1]/ul/li[{str(i)}]/div/div/div/div/div[1]/div/div/div/div/button/div/div/div/span/div/span')
            player_2 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[1]/ul/li[{str(i)}]/div/div/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/span')
            odds_1 = driver.find_element_by_xpath(f'/html/body/span/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[1]/ul/li[{str(i)}]/div/div/div/div/div[1]/div/div/div/div/button/div/div/div/span/div/div[1]/span')
            odds_2 = driver.find_element_by_xpath(f'/html/body/span/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[1]/ul/li[{str(i)}]/div/div/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/div[1]/span')
            if '/' in player_1.text:
                break
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

            player_list.append((player_1_name, player_2_name, odds_1.text, odds_2.text))
            i += 1
        except:
            if k == 2:
                break
            k = 2
            i += 1
            continue
    sleep(bot_sleep(10,20, True))
    # Tomorrow's matches
    i = 1
    while True:
        try:
            player_1 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[2]/ul/li[{str(i)}]/div/div/div/div/div[1]/div/div/div/div/button/div/div/div/span/div/span')
            player_2 = driver.find_element_by_xpath(f'//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[2]/ul/li[{str(i)}]/div/div/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/span')
            odds_1 = driver.find_element_by_xpath(f'/html/body/span/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[2]/ul/li[{str(i)}]/div/div/div/div/div[1]/div/div/div/div/button/div/div/div/span/div/div[1]/span')
            odds_2 = driver.find_element_by_xpath(f'/html/body/span/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/ul/div[2]/ul/li[{str(i)}]/div/div/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/div[1]/span')
            if '/' in player_1.text:
                break
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
            player_list.append((player_1_name, player_2_name, odds_1.text, odds_2.text))
            i += 1
        except:
            break
    
    driver.close()
    return player_list

def scofascore_scraper():
    # Driver Setup
    options = Options()
    options.add_argument("user-agent=Chrome/84.0.4147.135")
    #options.add_argument("--headless")
    
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = '181.6.191.126'
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(chrome_options=options, desired_capabilities=capabilities, executable_path=r'C:\WebDrivers\chromedriver.exe')
    # Open website
    driver.get('https://www.sofascore.com/tennis')
    print("Driver invoked")
    sleep(bot_sleep(5, 10, True))

    # Collect page data
    url = str(driver.current_url)
    page = requests.get(url)
    player_list = []
    i = 1
    j = 1
    while True:
        try:
            sleep(bot_sleep(5, 10, True))
            player_1 = driver.find_element_by_xpath(f'/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[{j}]/div[2]/a[{i}]/div[3]/div[1]').text
            player_2 = driver.find_element_by_xpath(f'/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[{j}]/div[2]/a[{i}]/div[3]/div[2]').text
            if '/' in player_1:
                i += 1
                continue
            else:
                i += 1
                player_list.append([player_1, player_2, 0, 0])
        except:
            try:
                i = 1
                j += 1
                player_1 = driver.find_element_by_xpath(f'/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[{j}]/div[2]/a[{i}]/div[3]/div[1]').text
                continue
            except:
                break
    driver.close()
    return player_list

if __name__ == '__main__':
    print(scofascore_scraper())
    #print(sportsbet_scraper_tennis())