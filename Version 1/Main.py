from Stat_Comparison_betting import read_data, player_compare, match_analysis
from Data_cleaning import cleaning
import pandas as pd
import csv
import datetime
from time import sleep
from TennisDataScraper import scrape_data

#Notes: 
# Balance is 0, Bet is flat 5
def drange(start, stop, step):
    while start < stop:
        yield start
        start += step

if __name__ == "__main__":
    #scrape_data()
    year = 2020
    counter = 0
    data = pd.DataFrame()
    #cleaning('2018.csv')
    data = read_data(data, '2020.csv')
    #for i in drange(0, 20, 0.25):
        #for j in drange(1, 5, 0.05):
    matches_analysed, matches_bet_on, balance, avg_bet, avg_score_diff, standard_deviation, num_correct, num_incorrect, avg_odds_bet_win, avg_odds_bet_lose, weights_dict = match_analysis(7.7829, 20, data)
    counter += 1
    print(f"Balance is: {balance}")
    print(f"Number of matches analysed: {matches_analysed}")
    print(f"Number of matches bet on: {matches_bet_on}")
    print(f"Average Bet: {avg_bet}")
    print(f"Average Score Difference: {avg_score_diff}")
    print(f"Standard Devation: {standard_deviation}")
    print(f"Number Correct: {num_correct}")
    print(f"Number Incorrect: {num_incorrect}")
    print(f"Time is: {datetime.datetime.now()}")
    print(f" Weights: {weights_dict}")
    if num_correct != 0 and (num_correct + num_incorrect) != 0:
        percentage_correct = num_correct / (num_correct + num_incorrect)
    else:
        percentage_correct = 0
    print(f"Percentage Correct: {percentage_correct}")
    print(f"No. of Different Weights Analysed:{counter}")
    column_headers = [year, balance, matches_analysed, matches_bet_on, avg_bet, avg_score_diff, standard_deviation, num_correct, num_incorrect, avg_odds_bet_win, avg_odds_bet_lose, percentage_correct, 0, 20, weights_dict]
    records = 'Betting_Results.csv'
    with open(records, 'a') as f:
        file_writer = csv.writer(f, delimiter=',', lineterminator='\n')
        file_writer.writerow(column_headers)
    f.close()