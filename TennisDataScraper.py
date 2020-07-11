from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from lxml import html
import requests
import webbrowser
import csv
from bs4 import BeautifulSoup

#Variables Setup
column_headers = ['player_id', 'name', 'age', 'weight_kg', 'height_cm', 'singles_rank', 'career_wins', 'career_losses', 'current_year_wins', 'current_year_losses', 'current_year_fedex', 'career_fedex', 'current_year_tiebreaks_fedex',
                    'career_tiebreaks_fedex', 'current_year_top10_fedex', 'career_top10_fedex', 'current_year_finals_fedex', 'career_finals_fedex', 'current_year_deciding_set_fedex', 'career_deciding_set_fedex',
                    'current_year_5th_set_fedex', 'career_5th_set_fedex', 'clay_current_year_fedex', 'clay_career_fedex', 'grass_current_year_fedex', 'grass_career_fedex', 'hard_current_year_fedex', 'hard_career_fedex',
                    'carpet_current_year_fedex', 'carpet_career_fedex', 'indoor_current_year_fedex', 'indoor_career_fedex', 'outdoor_current_year_fedex', 'outdoor_career_fedex', 'after_winning_1st_set_current_year_fedex',
                    'after_winning_1st_set_career_fedex', 'after_losing_1st_set_current_year_fedex', 'after_losing_1st_set_career_fedex', 'aces', 'double_faults', 'first_serve', 'first_serve_points_won',
                    'second_serve_points_won', 'service_games_played', 'service_games_won', 'total_service_points_won', 'first_serve_return_points_won', 'second_serve_return_points_won', 'break_points_converted',
                    'return_points_won', 'total_points_won']

# Selenium setup
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
print("Driver invoked")

#Links
links = ['https://www.atptour.com/en/rankings/singles','https://www.atptour.com/en/rankings/singles?rankDate=2020-03-16&rankRange=101-200','https://www.atptour.com/en/rankings/singles?rankDate=2020-03-16&rankRange=201-300','https://www.atptour.com/en/rankings/singles?rankDate=2020-03-16&rankRange=301-400',
            'https://www.atptour.com/en/rankings/singles?rankDate=2020-03-16&rankRange=401-500']

#CSV File Setup
records = 'Tennis_Records.csv'
with open(records, "w") as f:
    file_writer = csv.writer(f, delimiter=',', lineterminator='\n')
    file_writer.writerow(column_headers)
f.close()
def scrape_data():
    for j in range(0, 5):
        url_rankings = links[j]
        print(links[j])
        for i in range(1, 101):  
            column_headers = []
            driver.get(url_rankings)

            player_overview_link = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/div/table/tbody/tr[' + str(i) + ']/td[4]/a')
            player_overview_link.click()
            url = str(driver.current_url)
            page = requests.get(url)
            tree = html.fromstring(page.content)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            name = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/text()')[0] + '-' + tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/text()')[0]
            player_id = url.replace('https://www.atptour.com/en/players/', '').replace(name.lower(), '').replace('/overview', '').replace('/', '')
            
            #Overview Stats
            name = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/text()')[0] + ' ' + tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/text()')[0][0] + '.'
            age = soup.find(class_="table-big-value").text.split()[0]
            age = float(age)
            try:
                weight_kg = soup.find(class_="table-weight-kg-wrapper").text.split()[0].strip('(').strip(')').strip('kg')
                weight_kg = float(weight_kg)
            except:
                weight_kg = 0
            
            try:
                height_cm = soup.find(class_="table-height-cm-wrapper").text.split()[0].strip('(').strip(')').strip('cm')
                height_cm = float(height_cm)
            except:
                height_cm = 0

            singles_rank = i + (100 * j)
            #singles_rank = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[2]/div[1]/text()')[0])
            career_wins = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[2]/td[3]/div[1]/text()')[0].split('-')[0])
            career_losses = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[2]/td[3]/div[1]/text()')[0].split('-')[1])
            current_year_wins = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[4]/div[1]/text()')[0].split('-')[0])
            current_year_losses = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[4]/div[1]/text()')[0].split('-')[1])

            #Win/Loss Stats
            try:
                win_loss_link = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/ul/li[4]/a')
                win_loss_link.click()
                url = driver.current_url
                page = requests.get(url)
                tree = html.fromstring(page.content)

                current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[1]/tbody/tr[1]/td[3]/text()')[0])
                career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[1]/tbody/tr[1]/td[5]/text()')[0])
                current_year_tiebreaks_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[1]/td[3]/text()')[0])
                career_tiebreaks_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[1]/td[5]/text()')[0])
                current_year_top10_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/text()')[0])
                career_top10_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[5]/text()')[0])
                current_year_finals_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[3]/td[3]/text()')[0])
                career_finals_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[3]/td[5]/text()')[0])
                current_year_deciding_set_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[4]/td[3]/text()')[0])
                career_deciding_set_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[4]/td[5]/text()')[0])
                current_year_5th_set_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[5]/td[3]/text()')[0])
                career_5th_set_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[2]/tbody/tr[5]/td[5]/text()')[0])

                clay_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[1]/td[3]/text()')[0])
                clay_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[1]/td[5]/text()')[0])
                grass_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[2]/td[3]/text()')[0])
                grass_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[2]/td[5]/text()')[0])
                hard_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[3]/td[3]/text()')[0])
                hard_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[3]/td[5]/text()')[0])
                carpet_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[4]/td[3]/text()')[0])
                carpet_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[4]/td[5]/text()')[0])
                indoor_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[5]/td[3]/text()')[0])
                indoor_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[5]/td[5]/text()')[0])
                outdoor_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[6]/td[3]/text()')[0])
                outdoor_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[3]/tbody/tr[6]/td[5]/text()')[0])

                after_winning_1st_set_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[4]/tbody/tr[1]/td[3]/text()')[0])
                after_winning_1st_set_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[4]/tbody/tr[1]/td[5]/text()')[0])
                after_losing_1st_set_current_year_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[4]/tbody/tr[2]/td[3]/text()')[0])
                after_losing_1st_set_career_fedex = float(tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/div[1]/table[4]/tbody/tr[2]/td[5]/text()')[0])
            except:
                current_year_fedex = 0
                career_fedex = 0
                current_year_tiebreaks_fedex = 0
                career_tiebreaks_fedex = 0
                current_year_top10_fedex = 0
                career_top10_fedex = 0
                current_year_finals_fedex = 0
                career_finals_fedex = 0
                current_year_deciding_set_fedex = 0
                career_deciding_set_fedex = 0
                current_year_5th_set_fedex = 0
                career_5th_set_fedex = 0
                clay_current_year_fedex = 0
                clay_career_fedex = 0
                grass_current_year_fedex = 0
                grass_career_fedex = 0
                hard_current_year_fedex = 0
                hard_career_fedex = 0
                carpet_current_year_fedex = 0
                carpet_career_fedex = 0
                indoor_current_year_fedex = 0
                indoor_career_fedex = 0
                outdoor_current_year_fedex = 0
                outdoor_career_fedex = 0
                after_winning_1st_set_current_year_fedex = 0
                after_winning_1st_set_career_fedex = 0
                after_losing_1st_set_current_year_fedex = 0
                after_losing_1st_set_career_fedex = 0

            #Player Stats
            try:
                player_stats_link = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/ul/li[6]/a')
                player_stats_link.click()
                url = driver.current_url
                page = requests.get(url)
                tree = html.fromstring(page.content)

                aces = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[1]/td[2]/text()')[0].replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                aces = float(aces)
                double_faults = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[2]/td[2]/text()')[0].replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                double_faults = float(double_faults)
                first_serve = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[3]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                first_serve = float(first_serve) / 100
                first_serve_points_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[4]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                first_serve_points_won = float(first_serve_points_won) / 100
                second_serve_points_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[5]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                second_serve_points_won = float(second_serve_points_won) / 100
                break_points_faced = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[6]/td[2]/text()')[0].replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                break_points_faced = float(break_points_faced)
                break_points_saved = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[7]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                break_points_saved = float(break_points_saved) / 100
                service_games_played = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[8]/td[2]/text()')[0].replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                service_games_played = float(service_games_played)
                service_games_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[9]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                service_games_won = float(service_games_won) / 100
                total_service_points_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[1]/tbody/tr[10]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                total_service_points_won = float(total_service_points_won) / 100
                first_serve_return_points_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[2]/tbody/tr[1]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                first_serve_return_points_won = float(first_serve_return_points_won) / 100
                second_serve_return_points_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[2]/tbody/tr[2]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                second_serve_return_points_won = float(second_serve_return_points_won) / 100
                break_points_converted = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[2]/tbody/tr[4]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                break_points_converted = float(break_points_converted) / 100
                return_points_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[2]/tbody/tr[7]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                return_points_won = float(return_points_won) / 100
                total_points_won = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/div[2]/table[2]/tbody/tr[8]/td[2]/text()')[0].replace('%', '').replace('\r', '').replace('\t', '').replace('\n', '').replace(',', '')
                total_points_won = float(total_points_won) / 100
            except:
                aces = 0
                double_faults = 0
                first_serve = 0
                first_serve_points_won = 0
                second_serve_points_won = 0
                service_games_played = 0
                service_games_played = 0
                service_games_won = 0
                total_service_points_won = 0
                first_serve_return_points_won = 0
                second_serve_return_points_won = 0
                break_points_converted = 0
                return_points_won = 0
                total_points_won = 0

            column_headers = [player_id, name, age, weight_kg, height_cm, singles_rank, career_wins, career_losses, current_year_wins, current_year_losses, current_year_fedex, career_fedex, current_year_tiebreaks_fedex,
                            career_tiebreaks_fedex, current_year_top10_fedex, career_top10_fedex, current_year_finals_fedex, career_finals_fedex, current_year_deciding_set_fedex, career_deciding_set_fedex,
                            current_year_5th_set_fedex, career_5th_set_fedex, clay_current_year_fedex, clay_career_fedex, grass_current_year_fedex, grass_career_fedex, hard_current_year_fedex, hard_career_fedex,
                            carpet_current_year_fedex, carpet_career_fedex, indoor_current_year_fedex, indoor_career_fedex, outdoor_current_year_fedex, outdoor_career_fedex, after_winning_1st_set_current_year_fedex,
                            after_winning_1st_set_career_fedex, after_losing_1st_set_current_year_fedex, after_losing_1st_set_career_fedex, aces, double_faults, first_serve, first_serve_points_won,
                            second_serve_points_won, service_games_played, service_games_won, total_service_points_won, first_serve_return_points_won, second_serve_return_points_won, break_points_converted,
                            return_points_won, total_points_won]
            
            with open(records, "a") as f:
                file_writer = csv.writer(f, delimiter=',', lineterminator='\n')
                file_writer.writerow(column_headers)
            f.close()
            print(i)