import csv
from typing import AsyncGenerator
from numpy.lib.function_base import diff
import pandas as pd
import numpy as np
import datetime
from time import sleep
import math
from Train_Model import create_player_dict
import PySimpleGUI as sg

global player_dict
player_dict = {}

def read_players(players_list_file):
    df = pd.read_csv(players_list_file)
    global player_dict
    for index, row in df.iterrows():
        try:
            name = row[1] + ' ' + row[2]
        except:
            continue

        try:
            player_id = row[0]
        except:
            continue

        player_dict[row[0]] = [player_id, name, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0]
        '''
        #### Columns ####
        Player Id
        Name
        Rank
        Ranking Points
        Career Played
        Career Won
        Height
        Age
        Career Aces
        Career Double Faults
        Career Serve Points
        Career First Serve Won
        Career Second Serve Won
        Career Break Points Saved
        Career Break Points Faced
        Career Played against Top 10
        Career Won against Top 10
        Career Played on Hard court
        Career Won on Hard Court
        Career Played on Clay Court
        Career Won on Clay Court
        Career Win %
        Career Double Fault %
        Career Ace %
        Career Break Point Saved %
        Career Won against Top 10 %
        Career Won on Hard Court %
        Career Won on Clay Court %
        Career Ace Against
        Career Serve Points Against
        Career Ace Against %
        Career First Serve Points Against
        Career First Serve Points Return Won
        Career First Serve Points Return Won %
        Career Points Played
        Career Points Won
        Career Points Won %

        Current Year Played
        Current Year Won
        Current Year Aces
        Current Year Double Faults
        Current Year Serve Points
        Current Year First Serve Won
        Current Year Second Serve Won
        Current Year Break Points Saved
        Current Year Break Points Faced
        Current Year Played against Top 10
        Current Year Won against Top 10
        Current Year Played on Hard court
        Current Year Won on Hard Court
        Current Year Played on Clay Court
        Current Year Won on Clay Court
        Current Year Win %
        Current Year Double Fault %
        Current Year Ace %
        Current Year Break Point Saved %
        Current Year Won against Top 10 %
        Current Year Won on Hard Court %
        Current Year Won on Clay Court %
        Current Year Ace Against
        Current Year Serve Points Against
        Current Year Ace Against %
        Current Year First Serve Points Against
        Current Year First Serve Points Return Won
        Current Year First Serve Points Return Won %
        Current Year Points Played
        Current Year Points Won
        Current Year Points Won %

        Win Streak
        '''

    print('Complete player dictionary template')
    return player_dict

def read_rank(rank_list_file, player_dict):
    df = pd.read_csv(rank_list_file)

    for index, row in df.iterrows():
        # Rank
        player_dict[row[2]][2] = row[1]
        
        # Ranking Points
        player_dict[row[2]][3] = row[3]


    print("Rankings finished")
    return player_dict

def parse_match(row, player_dict):

    # Career Stats
    try:
        # Player ID
        p1 = row[7]
        player_dict[p1][0] = p1
        p2 = row[15]
        player_dict[p2][0] = p2

        # Name
        player_dict[p1][24] = row[10]
        player_dict[p2][24] = row[18]

        # Rank
        player_dict[p1][1] = row[45]
        player_dict[p2][1] = row[47]

        # Ranking Points
        player_dict[p1][2] = row[46]
        player_dict[p2][2] = row[48]

        # Add to # of matches played
        player_dict[p1][3] += 1
        player_dict[p2][3] += 1

        # Add to # of matches won
        player_dict[p1][4] += 1

        # Player Height
        if row[11] == 0:
            player_dict[p1][5] = 182.9
        else:
            player_dict[p1][5] = row[12]
        
        if row[19] == 0:
            player_dict[p2][5] = 182.9
        else:    
            player_dict[p2][5] = row[20]

        # Player Age
        if row[13] == 0:
            player_dict[p1][6] = 26.51
        else:    
            player_dict[p1][6] = row[14]

        if row[21] == 0:
            player_dict[p2][6] = 26.51
        else:    
            player_dict[p2][6] = row[22]

        # Player Hand
        if row[13] == "L":
            player_dict[p1][7] = 0
        elif row[13] == "R":
            player_dict[p1][7] = 1
        else:
            player_dict[p1][7] = 0.5

        # Player Hand
        if row[19] == "L":
            player_dict[p2][7] = 0
        elif row[19] == "R":
            player_dict[p2][7] = 1
        else:
            player_dict[p2][7] = 0.5

        # # of Aces
        player_dict[p1][8] += row[27]
        player_dict[p2][8] += row[36]

        # # of Double Faults
        player_dict[p1][9] += row[28]
        player_dict[p2][9] += row[37]

        # # Serve Points
        player_dict[p1][10] += row[29]
        player_dict[p2][10] += row[38]

        # # First serve in
        player_dict[p1][11] += row[30]
        player_dict[p2][11] += row[39]

        # # First serve won
        player_dict[p1][12] += row[31]
        player_dict[p2][12] += row[40]

        # # Second serve in
        player_dict[p1][13] += (row[29] - row[30])
        player_dict[p2][13] += (row[38] - row[39])

        # # Second serve won
        player_dict[p1][14] += row[32]
        player_dict[p2][14] += row[41]

        # # Break Points saved
        player_dict[p1][15] += row[34]
        player_dict[p2][15] += row[43]

        # # Break Points faced
        player_dict[p1][16] += row[35]
        player_dict[p2][16] += row[44]

        # Win Streak
        if player_dict[p1][17] < 0:
            player_dict[p1][17] = 1
        else:
            player_dict[p1][17] += 1

        if player_dict[p2][17] > 0:
            player_dict[p2][17] = 0
        else:
            player_dict[p2][17] -= 1

    except Exception:
        pass
    
    print("Match Finished")
    return player_dict
        
def write_csv(player_dict):
    column_headers = ['player_id',
    'Name',
    'Rank',
    'Ranking Points',
    'Career Played',
    'Career Won',
    'Height',
    'Age',
    'Career Aces',
    'Career Double Faults',
    'Career Serve Points',
    'Career First Serve Won',
    'Career Second Serve Won',
    'Career Break Points Saved',
    'Career Break Points Faced',
    'Career Played against Top 10',
    'Career Won against Top 10',
    'Career Played on Hard court',
    'Career Won on Hard Court',
    'Career Played on Clay Court',
    'Career Won on Clay Court',
    'Career Win %',
    'Career Double Fault %',
    'Career Ace %',
    'Career Break Point Saved %',
    'Career Won against Top 10 %',
    'Career Won on Hard Court %',
    'Career Won on Clay Court %',
    'Career Ace Against',
    'Career Serve Points Against',
    'Career Ace Against %',
    'Career First Serve Points Against',
    'Career First Serve Points Return Won',
    'Career First Serve Points Return Won %',
    'Career Points Played',
    'Career Points Won',
    'Career Points Won %',
    'Current Year Played',
    'Current Year Won',
    'Current Year Aces',
    'Current Year Double Faults',
    'Current Year Serve Points',
    'Current Year First Serve Won',
    'Current Year Second Serve Won',
    'Current Year Break Points Saved',
    'Current Year Break Points Faced',
    'Current Year Played against Top 10',
    'Current Year Won against Top 10',
    'Current Year Played on Hard court',
    'Current Year Won on Hard Court',
    'Current Year Played on Clay Court',
    'Current Year Won on Clay Court',
    'Current Year Win %',
    'Current Year Double Fault %',
    'Current Year Ace %',
    'Current Year Break Point Saved %',
    'Current Year Won against Top 10 %',
    'Current Year Won on Hard Court %',
    'Current Year Won on Clay Court %',
    'Current Year Ace Against',
    'Current Year Serve Points Against',
    'Current Year Ace Against %',
    'Current Year First Serve Points Against',
    'Current Year First Serve Points Return Won',
    'Current Year First Serve Points Return Won %',
    'Current Year Points Played',
    'Current Year Points Won',
    'Current Year Points Won %',
    'Win Streak']

    #CSV File Setup
    player_stats = 'player_stats.csv'
    with open(player_stats, "w") as f:
        file_writer = csv.writer(f, delimiter=',', lineterminator='\n')
        file_writer.writerow(column_headers)

        for player in player_dict:
            file_writer.writerow(player_dict[player])
    f.close()
    print("CSV Complete")

def create_diff_row(player_dict, player1_id, player2_id):
    rank = (1 - (player_dict[player1_id][1] / 1000))- (1 - (player_dict[player2_id][1] / 1000))
    try:
        ranking_pts_p1 = (math.log(player_dict[player1_id][2]) / 10)
    except:
        ranking_pts_p1 = 0

    try:
        ranking_pts_p2 = (math.log(player_dict[player2_id][2]) / 10)
    except:
        ranking_pts_p2 = 0

    ranking_points = ranking_pts_p1 - ranking_pts_p2
    height = float(player_dict[player1_id][5]) - float(player_dict[player2_id][5])
    age = player_dict[player1_id][6] - player_dict[player2_id][6]
    hand = player_dict[player1_id][7] - player_dict[player2_id][7]
    win_streak = player_dict[player1_id][17] - player_dict[player2_id][17]
    career_win_perc = player_dict[player1_id][18] - player_dict[player2_id][18]
    career_double_fault_perc = player_dict[player1_id][19] - player_dict[player2_id][19]
    career_ace_perc = player_dict[player1_id][20] - player_dict[player2_id][20]
    career_break_pt_svd_perc = player_dict[player1_id][21] - player_dict[player2_id][21]
    career_1st_serve_won_perc = player_dict[player1_id][22] - player_dict[player2_id][22]
    career_2nd_serve_won_perc = player_dict[player1_id][23] - player_dict[player2_id][23]

    row = [rank, ranking_points, height, age, hand, win_streak, career_win_perc, career_double_fault_perc, career_ace_perc, career_break_pt_svd_perc, career_1st_serve_won_perc, career_2nd_serve_won_perc]
    print(row)
    return row

def stats_analysis(player_dict, player1_id, player2_id):
    for player in [player1_id, player2_id]:
        # Career Win %
        try:
            career_win_perc = player_dict[player][4] / player_dict[player][3]
        except:
            career_win_perc = 0

        player_dict[player][18] = career_win_perc

        # Career Double Fault %
        try:
            career_double_fault_perc = player_dict[player][9] / player_dict[player][10]
        except:
            career_double_fault_perc = 0

        player_dict[player][19] = career_double_fault_perc

        # Career Ace %
        try:
            career_ace_perc = player_dict[player][8] / player_dict[player][10]
        except:
            career_ace_perc = 0
            
        player_dict[player][20] = career_ace_perc

        # Career Break Point Saved %
        try:
            career_break_pt_svd_perc = player_dict[player][15] / player_dict[player][16]
        except:
            career_break_pt_svd_perc = 0

        player_dict[player][21] = career_break_pt_svd_perc

        # Career First Serve Won %
        try:
            career_1st_serve_won_perc = player_dict[player][12] / player_dict[player][11]
        except:
            career_1st_serve_won_perc = 0
        
        player_dict[player][22] = career_1st_serve_won_perc

        # Career Second Serve Won %
        try:
            career_2nd_serve_won_perc = player_dict[player][14] / player_dict[player][13]
        except:
            career_2nd_serve_won_perc = 0

        player_dict[player][23] = career_2nd_serve_won_perc

    print("Stats Analysis Complete")
    return player_dict

def create_player_dict():
    player_dict_raw = pd.read_csv('player_stats.csv')
    player_dict = {}
    for index, row in player_dict_raw.iterrows():
        player_dict[row[0]] = row
    print("Player Dictionary Complete")
    return player_dict

def rand_string_check():
    matches_df = pd.read_csv(f'Match_Data/atp_matches_{1968}.csv')
    for i in range(1969, 2021):
        print(f"Matches DF Curr YR: {i}")
        temp_matches_df = pd.read_csv(f'Match_Data/atp_matches_{i}.csv')
        matches_df = pd.concat([matches_df, temp_matches_df])

    for index, row in matches_df.iterrows():
        score_raw = str(row[23])
        score = score_raw.split()
        new_score = 0
        for s in score:
            if '[' in s:
                continue
            if 'W/O' in s or 'RET' in s or 'Def' in s:
                continue
            num = s.split('-')

            try:
                a = int(num[0][0])
                b = int(num[1][0])
            except:
                print(num)
    return "COMPLETE"

def match_data_clean(year_begin, year_end):
    matches_df = pd.read_csv(f'Match_Data/atp_matches_{year_begin}.csv')
    for i in range(year_begin+1, year_end):
        print(f"Matches DF Curr YR: {i}")
        temp_matches_df = pd.read_csv(f'Match_Data/atp_matches_{i}.csv')
        matches_df = pd.concat([matches_df, temp_matches_df])

    total_items = len(matches_df)
    j = 0
    player_dict = create_player_dict()
    
    for index, row in matches_df.iterrows():
        j += 1
        sg.one_line_progress_meter('My meter', j, total_items, 'my meter' )
        # Skip if rank is equal to zero
        if row[45] == 0  or row[47] == 0:
            continue
        
        w_id = row["winner_id"]
        l_id = row["loser_id"]
        
        if w_id not in player_dict:
            player_dict[w_id] = []
            i = 0
            for i in range(25):
                player_dict[w_id].append(0)

        if l_id not in player_dict:
            player_dict[l_id] = []
            i = 0
            for i in range(25):
                player_dict[l_id].append(0)
                
        player_dict = parse_match(row, player_dict)
        player_dict = stats_analysis(player_dict, w_id, l_id)

        diff_row = create_diff_row(player_dict, w_id, l_id)
        diff_row.append(1)
        print(diff_row)
        with open('matches.csv', 'a', newline='') as f:
            # Create the csv writer
            writer = csv.writer(f)

            # Write a row to the csv file
            writer.writerow(diff_row)
        
    with open('player_stats.csv', 'w', newline='') as f:
        # Create the csv writer
        writer = csv.writer(f)

        for player in player_dict:
            # Write dictionary to the csv
            writer.writerow(player_dict[player])

    return player_dict

if __name__ == "__main__":
    player_dict = match_data_clean(1991,2021)

    with open('player_stats.csv', 'w', newline='') as f:
        # Create the csv writer
        writer = csv.writer(f)

        for player in player_dict:
            # Write dictionary to the csv
            writer.writerow(player_dict[player])

    print("Script Complete")