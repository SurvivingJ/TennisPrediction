from sklearn.linear_model import LinearRegression
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import re
import statistics
import numpy as np
from time import sleep
import pickle
import random
import csv
import PySimpleGUI as sg

def create_diff_row(player_dict, player1_id, player2_id):
    print(player1_id, player2_id)
    rank = player_dict[player1_id][2] - player_dict[player2_id][2]
    career_win_perc = player_dict[player1_id][21] - player_dict[player2_id][21]
    career_double_fault_perc = player_dict[player1_id][22] - player_dict[player2_id][22]
    career_ace_perc = player_dict[player1_id][23] - player_dict[player2_id][23]
    career_break_pt_svd_perc = player_dict[player1_id][24] - player_dict[player2_id][24]
    career_won_top_10_perc = player_dict[player1_id][25] - player_dict[player2_id][25]
    career_won_hard_court_perc = player_dict[player1_id][26] - player_dict[player2_id][26]
    career_won_clay_court_perc = player_dict[player1_id][27] - player_dict[player2_id][27]
    career_ace_against_perc = player_dict[player1_id][30] - player_dict[player2_id][30]
    career_first_serve_pts_return_won_perc = player_dict[player1_id][33] - player_dict[player2_id][33]
    career_points_won_perc = player_dict[player1_id][36] - player_dict[player2_id][36]
    curr_yr_win_perc = player_dict[player1_id][52] - player_dict[player2_id][52]
    curr_yr_double_fault_perc = player_dict[player1_id][53] - player_dict[player2_id][53]
    curr_yr_ace_perc = player_dict[player1_id][54] - player_dict[player2_id][54]
    curr_yr_break_pt_svd_perc = player_dict[player1_id][55] - player_dict[player2_id][55]
    curr_yr_won_top_10_perc = player_dict[player1_id][56] - player_dict[player2_id][56]
    curr_yr_won_hard_court_perc = player_dict[player1_id][57] - player_dict[player2_id][57]
    curr_yr_won_clay_court_perc = player_dict[player1_id][58] - player_dict[player2_id][58]
    curr_yr_ace_against_perc = player_dict[player1_id][61] - player_dict[player2_id][61]
    curr_yr_first_serve_pts_return_won_perc = player_dict[player1_id][64] - player_dict[player2_id][64]
    curr_yr_won_perc = player_dict[player1_id][67] - player_dict[player2_id][67]

    row = [rank,career_win_perc,career_double_fault_perc,career_ace_perc,career_break_pt_svd_perc,career_won_top_10_perc,career_won_hard_court_perc,career_won_clay_court_perc,career_ace_against_perc,career_first_serve_pts_return_won_perc,
    career_points_won_perc,curr_yr_win_perc,curr_yr_double_fault_perc,curr_yr_ace_perc,curr_yr_break_pt_svd_perc,curr_yr_won_top_10_perc,curr_yr_won_hard_court_perc,curr_yr_won_clay_court_perc,curr_yr_ace_against_perc,curr_yr_first_serve_pts_return_won_perc,curr_yr_won_perc]
    
    return row

def parse_match(row, player_dict, player1_id, player2_id, year):
    matches_yr = year
    curr_yr = year

    # Career Stats
    try:
        # Add to # of matches played
        player_dict[player1_id][4] += 1
        player_dict[player2_id][4] += 1

        # Add to winner score
        player_dict[player1_id][5] += 1

        # Player Height
        player_dict[player1_id][6] = row[11]
        player_dict[player2_id][6] = row[19]

        # Player Age
        player_dict[player1_id][7] = row[13]
        player_dict[player2_id][7] = row[21]

        # # of Aces
        player_dict[player1_id][8] += row[26]
        player_dict[player2_id][8] += row[35]

        # # of Double Faults
        player_dict[player1_id][9] += row[27]
        player_dict[player2_id][9] += row[36]

        # # Serve Points
        player_dict[player1_id][10] += row[28]
        player_dict[player2_id][10] += row[37]

        # # First serve won
        player_dict[player1_id][11] += row[30]
        player_dict[player2_id][11] += row[39]

        # # Second serve won
        player_dict[player1_id][12] += row[31]
        player_dict[player2_id][12] += row[40]

        # # Break Points saved
        player_dict[player1_id][13] += row[33]
        player_dict[player2_id][13] += row[42]

        # # Break Points faced
        player_dict[player1_id][14] += row[34]
        player_dict[player2_id][14] += row[43]

        # # Aces against
        player_dict[player1_id][28] += row[35]
        player_dict[player2_id][28] += row[26]

        # # Serve Points Against
        player_dict[player1_id][29] += row[37]
        player_dict[player2_id][29] += row[28]

        # # First Serve Points Against
        player_dict[player1_id][31] += row[38]
        player_dict[player2_id][31] += row[29]

        # # First Serve Points Return Won
        player_dict[player1_id][32] += (row[38] - row[39])
        player_dict[player2_id][32] += (row[29] - row[30])

        # # Points Played
        player_dict[player1_id][34] += (row[28] + row[37])
        player_dict[player2_id][34] += (row[28] + row[37])

        # # Points Won (1st won + 2nd won) + (svpt - df - 1st won - 2nd won)
        player_dict[player1_id][35] += ((row[30] + row[31]) + (row[28] - row[27] - row[30] - row[31]))
        player_dict[player2_id][35] += ((row[39] + row[40]) + (row[37] - row[36] - row[39] - row[40]))

        if row[44] <= 10:
            # Played against Top 10 players
            player_dict[player2_id][15] += 1

        if row[46] <= 10:
            # Wins against Top 10 players
            player_dict[player1_id][16] += 1

            # Played against Top 10 players
            player_dict[player1_id][15] += 1

        if row[1] == 'Hard':
            # Played on Hard court
            player_dict[player1_id][17] += 1

            # Won on Hard court
            player_dict[player1_id][18] += 1

            # Played on Hard court
            player_dict[player2_id][17] += 1
        elif row[1] == 'Clay':
            # Played on Clay court
            player_dict[player1_id][19] += 1

            # Won on Clay court
            player_dict[player1_id][20] += 1

            # Played on Clay court
            player_dict[player2_id][19] += 1
    except Exception as e:
        print(e)

    # Current Year Stats
    if matches_yr == curr_yr:
        try:
            # Add to # of matches played
            player_dict[player1_id][37] += 1
            player_dict[player2_id][37] += 1

            # Add to winner score
            player_dict[player1_id][38] += 1

            # # of Aces
            player_dict[player1_id][39] += row[26]
            player_dict[player2_id][39] += row[35]

            # # of Double Faults
            player_dict[player1_id][40] += row[27]
            player_dict[player2_id][40] += row[36]

            # # Serve Points
            player_dict[player1_id][41] += row[28]
            player_dict[player2_id][41] += row[37]

            # # First serve won
            player_dict[player1_id][42] += row[30]
            player_dict[player2_id][42] += row[39]

            # # Second serve won
            player_dict[player1_id][43] += row[31]
            player_dict[player2_id][43] += row[40]

            # # Break Points saved
            player_dict[player1_id][44] += row[33]
            player_dict[player2_id][44] += row[42]

            # # Break Points faced
            player_dict[player1_id][45] += row[34]
            player_dict[player2_id][45] += row[43]

            # # Aces against
            player_dict[player1_id][59] += row[35]
            player_dict[player2_id][59] += row[26]

            # # Serve Points Against
            player_dict[player1_id][60] += row[37]
            player_dict[player2_id][60] += row[28]

            # # First Serve Points Against
            player_dict[player1_id][62] += row[38]
            player_dict[player2_id][62] += row[29]

            # # First Serve Points Return Won
            player_dict[player1_id][63] += (row[38] - row[39])
            player_dict[player2_id][63] += (row[29] - row[30])

            # # Points Won (1st won + 2nd won) + (svpt - df - 1st won - 2nd won)
            player_dict[player1_id][66] += ((row[30] + row[31]) + (row[28] - row[27] - row[30] - row[31]))
            player_dict[player2_id][66] += ((row[39] + row[40]) + (row[37] - row[36] - row[39] - row[40]))

            if row[44] <= 10:
                # Player against Top 10 players
                player_dict[player2_id][46] += 1

            if row[46] <= 10:
                # Wins against Top 10 players
                player_dict[player1_id][47] += 1

                # Played against Top 10 players
                player_dict[player1_id][46] += 1

            if row[1] == 'Hard':
                # Played on Hard court
                player_dict[player1_id][48] += 1

                # Won on Hard court
                player_dict[player1_id][49] += 1

                # Played on Hard court
                player_dict[player2_id][48] += 1
            elif row[1] == 'Clay':
                # Played on Clay court
                player_dict[player1_id][50] += 1

                # Won on Clay court
                player_dict[player1_id][51] += 1

                # Played on Clay court
                player_dict[player2_id][50] += 1
        except Exception as e:
            print(e)
            
    print("Match Finished")
    return player_dict

def stats_analysis(player_dict, player1_id, player2_id):
    for player in [player1_id, player2_id]:
        # Career Win %
        try:
            career_win_perc = player_dict[player][5] / player_dict[player][4]
        except:
            career_win_perc = 0
        
        player_dict[player][21] = career_win_perc

        # Career Double Fault %
        try:
            career_double_fault_perc = player_dict[player][9] / player_dict[player][10]
        except:
            career_double_fault_perc = 0

        player_dict[player][22] = career_double_fault_perc

        # Career Ace %
        try:
            career_ace_perc = player_dict[player][8] / player_dict[player][10]
        except:
            career_ace_perc = 0
        
        player_dict[player][23] = career_ace_perc

        # Career Break Point Saved %
        try:
            career_break_pt_svd_perc = player_dict[player][13] / player_dict[player][14]
        except:
            career_break_pt_svd_perc = 0

        player_dict[player][24] = career_break_pt_svd_perc

        # Career Won against Top 10 %
        try:
            career_won_top_10_perc = player_dict[player][16] / player_dict[player][15]
        except:
            career_won_top_10_perc = 0

        player_dict[player][25] = career_won_top_10_perc
        
        # Career Won on Hard Court %
        try:
            career_won_hard_court_perc = player_dict[player][18] / player_dict[player][17]
        except:
            career_won_hard_court_perc = 0

        player_dict[player][26] = career_won_hard_court_perc

        # Career Won on Clay Court %
        try:
            career_won_clay_court_perc = player_dict[player][20] / player_dict[player][19]
        except:
            career_won_clay_court_perc = 0
        
        player_dict[player][27] = career_won_clay_court_perc

        # Career Ace Against %
        try:
            career_ace_against_perc = player_dict[player][28] / player_dict[player][29]
        except:
            career_ace_against_perc = 0

        player_dict[player][30] = career_ace_against_perc

        # Career First Serve Points Return Won %
        try:
            career_first_serve_pts_return_won_perc = player_dict[player][32] / player_dict[player][31]
        except:
            career_first_serve_pts_return_won_perc = 0

        player_dict[player][33] = career_first_serve_pts_return_won_perc

        # Career Points Won %
        try:
            career_pts_won_perc = player_dict[player][35] / player_dict[player][34]
        except:
            career_pts_won_perc = 0

        player_dict[player][36] = career_pts_won_perc

        # Current Year Win %
        try:
            curr_yr_win_perc = player_dict[player][38] / player_dict[player][37]
        except:
            curr_yr_win_perc = 0
        
        player_dict[player][52] = curr_yr_win_perc

        # Current Year Double Fault %
        try:
            curr_yr_double_fault_perc = player_dict[player][40] / player_dict[player][41]
        except:
            curr_yr_double_fault_perc = 0

        player_dict[player][53] = curr_yr_double_fault_perc

        # Current Year Ace %
        try:
            curr_yr_ace_perc = player_dict[player][39] / player_dict[player][41]
        except:
            curr_yr_ace_perc = 0

        player_dict[player][54] = curr_yr_ace_perc

        # Current Year Break Point Saved %
        try:
            curr_yr_break_pt_svd_perc = player_dict[player][44] / player_dict[player][45]
        except:
            curr_yr_break_pt_svd_perc = 0

        player_dict[player][55] = curr_yr_break_pt_svd_perc

        # Current Year Won against Top 10 %
        try:
            curr_yr_won_top_10_perc = player_dict[player][47] / player_dict[player][46]
        except:
            curr_yr_won_top_10_perc = 0

        player_dict[player][56] = curr_yr_won_top_10_perc
        
        # Current Year Won on Hard Court %
        try:
            curr_yr_won_hard_court_perc = player_dict[player][49] / player_dict[player][48]
        except:
            curr_yr_won_hard_court_perc = 0

        player_dict[player][57] = curr_yr_won_hard_court_perc

        # Current Year Won on Clay Court %
        try:
            curr_yr_won_clay_court_perc = player_dict[player][51] / player_dict[player][50]
        except:
            curr_yr_won_clay_court_perc = 0

        player_dict[player][58] = curr_yr_won_clay_court_perc

        # Current Year Ace Against %
        try:
            curr_yr_ace_against_perc = player_dict[player][59] / player_dict[player][60]
        except:
            curr_yr_ace_against_perc = 0

        player_dict[player][61] = curr_yr_ace_against_perc

        # Current Year First Serve Points Return Won %
        try:
            curr_yr_first_serve_pts_return_won_perc = player_dict[player][63] / player_dict[player][62]
        except:
            curr_yr_first_serve_pts_return_won_perc = 0

        player_dict[player][64] = curr_yr_first_serve_pts_return_won_perc

        # Current Year Points Won %
        try:
            curr_yr_pts_won_perc = player_dict[player][66] / player_dict[player][65]
        except:
            curr_yr_pts_won_perc = 0

        player_dict[player][67] = curr_yr_pts_won_perc

    print("Stats Analysis Complete")
    return player_dict

def create_player_dict():
    player_dict_raw = pd.read_csv('player_stats.csv')
    player_dict = {}
    for index, row in player_dict_raw.iterrows():
        player_dict[row[0]] = row
    print("Player Dictionary Complete")
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
    return("CSV Complete")

def player_compare(player_stats_df, player1, player2, perc_through_year):
    # Reset variables
    player1_id = 0
    player2_id = 0

    player1_score = 0
    player2_score = 0

    # Find players' ids
    player1_id = player_stats_df.index[player_stats_df["player_id"] == player1].tolist()[0]
    player2_id = player_stats_df.index[player_stats_df["player_id"] == player2].tolist()[0]

    # Relevant columns for analysis
    rel_columns_pos = [[3, 0.6368], [21, 0.6303], [23, 0.5351], [24, 0.5351], [25, 0.5009], [26, 0.5836], [27, 0.5642], [33, 0.5300],
                        [36, 0.4477], [52, perc_through_year], [54,perc_through_year], [55, perc_through_year], [56, perc_through_year], [57, perc_through_year], [58, perc_through_year], [64, perc_through_year], [67, perc_through_year]]
    rel_columns_neg = [[2, 0.6365], [22, 0.5016], [30, 0.5318], [53, perc_through_year], [61, perc_through_year]]

    # Compare players' values and score them
    for column in rel_columns_pos:
        index = column[0]
        if player_stats_df.iloc[player1_id][index] > player_stats_df.iloc[player2_id][index]:
            player1_score += (1 * column[1])
        elif player_stats_df.iloc[player1_id][index] < player_stats_df.iloc[player2_id][index]:
            player2_score += (1 * column[1])
        else:
            continue
    
    for column in rel_columns_neg:
        index = column[0]
        if player_stats_df.iloc[player1_id][index] < player_stats_df.iloc[player2_id][index]:
            player1_score += (1 * column[1])
        elif player_stats_df.iloc[player1_id][index] > player_stats_df.iloc[player2_id][index]:
            player2_score += (1 * column[1])
        else:
            continue

    return player1_score, player2_score

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
    
    matches_fin_df = pd.DataFrame(columns=['Rank', 'Career Win %','Career Double Fault %','Career Ace %','Career Break Point Saved %','Career Won against Top 10 %','Career Won on Hard Court %','Career Won on Clay Court %','Career Ace Against %', 
    'Career First Serve Points Return Won %', 'Career Points Won %','Current Year Win %','Current Year Double Fault %','Current Year Ace %','Current Year Break Point Saved %','Current Year Won against Top 10 %','Current Year Won on Hard Court %',
    'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %', 'Score'])

    player_df_raw = pd.read_csv('player_stats.csv')
    player_df = player_df_raw[['player_id','Rank', 'Career Win %','Career Double Fault %','Career Ace %','Career Break Point Saved %','Career Won against Top 10 %','Career Won on Hard Court %','Career Won on Clay Court %','Career Ace Against %', 
    'Career First Serve Points Return Won %', 'Career Points Won %','Current Year Win %','Current Year Double Fault %','Current Year Ace %','Current Year Break Point Saved %','Current Year Won against Top 10 %','Current Year Won on Hard Court %',
    'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %']]

    player_comb_df = pd.DataFrame(columns=['Rank', 'Career Win %','Career Double Fault %','Career Ace %','Career Break Point Saved %','Career Won against Top 10 %','Career Won on Hard Court %','Career Won on Clay Court %','Career Ace Against %', 
    'Career First Serve Points Return Won %', 'Career Points Won %','Current Year Win %','Current Year Double Fault %','Current Year Ace %','Current Year Break Point Saved %','Current Year Won against Top 10 %','Current Year Won on Hard Court %',
    'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %'])

    player_score_df = pd.DataFrame(columns=['Player 1 Score', 'Player 2 Score', 'Winner'])

    player_dict = create_player_dict()

    year = 2000
    total_items = len(matches_df)
    i = 0
    for index, row in matches_df.iterrows():
        i += 1
        sg.one_line_progress_meter('My meter', i, total_items, 'my meter' )
        player1_id = row[7]
        player2_id = row[15]

        new_row = create_diff_row(player_dict, player1_id, player2_id)

        score_raw = row[23]
        score = score_raw.split()
        new_score = 0
        for s in score:
            if '[' in s:
                continue
            if 'W/O' in s or 'RET' in s or 'Def' in s:
                print("UH OH")
                continue
            num = s.split('-')
            try:
                int(num[0][0])
                int(num[1][0])
            except:
                continue
            if int(num[0][0]) > int(num[1][0]):
                new_score += 1
            else:
                new_score -= 1

        new_row.append(new_score)

        new_row = [ abs(i) for i in new_row]

        
        matches_fin_df.loc[len(matches_fin_df)] = new_row

        # Calculating percent through year
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = str(row[5])[4:6]
        day = str(row[5])[6:]
        day_of_year = 0
        for x in months:
            if x != month:
                day_of_year += month_len[int(x)-1]
            else:
                break
        day_of_year += int(day)
        perc_through_year = float(day_of_year) / float(365.0)

        prev_year_val = year
        year = row[0][0:4]

        if prev_year_val != year:
            for player in player_dict:
                for i in range(37, 68):
                    player_dict[player][i] = 0

        # Calculating player scores
        player_1_score, player_2_score = player_compare(player_df_raw, player1_id, player2_id, perc_through_year)
        player_score_row = [player_1_score, player_2_score, 0]
        print("--------------------------------------------")
        print(f"SCORES: {player_1_score} || {player_2_score}")
        print("--------------------------------------------")
        switch = random.randint(1, 2)

        if switch == 2:
            player_score_row = [player_2_score, player_1_score, 1]
        
        player_score_df.loc[len(player_score_df)] = player_score_row
        
        player_dict = parse_match(row, player_dict, player1_id, player2_id, year)
        player_dict = stats_analysis(player_dict, player1_id, player2_id)
        write_csv(player_dict)
        print('---------------------------------------------')
        print(f"Match | {player1_id} | v | {player2_id} | Complete")
        print('---------------------------------------------')

        '''
        match_df = pd.DataFrame(new_row, columns=['Rank', 'Career Win %','Career Double Fault %','Career Ace %','Career Break Point Saved %','Career Won against Top 10 %','Career Won on Hard Court %','Career Won on Clay Court %','Career Ace Against %', 
        'Career First Serve Points Return Won %', 'Career Points Won %','Current Year Win %','Current Year Double Fault %','Current Year Ace %','Current Year Break Point Saved %','Current Year Won against Top 10 %','Current Year Won on Hard Court %',
        'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %', 'Score'])
        matches_fin_df = matches_fin_df.append(match_df)
        '''
    return matches_fin_df, player_score_df

def display(results):
    print(f'Best parameters are: {results.best_params_}')
    print("\n")
    mean_score = results.cv_results_['mean_test_score']
    std_score = results.cv_results_['std_test_score']
    params = results.cv_results_['params']
    for mean,std,params in zip(mean_score,std_score,params):
        print(f'{round(mean,3)} + or -{round(std,3)} for the {params}')

    return

def model_train_match_score(matches_fin_df):
    x = matches_fin_df.iloc[:, 0:-1].values
    y = matches_fin_df.iloc[:, -1].values
    print(x.shape)
    print(y.shape)

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the dataset
    from sklearn.ensemble import RandomForestRegressor

    reg = RandomForestRegressor(n_estimators=250, max_depth=8)
    #from sklearn.model_selection import GridSearchCV
    #cv = GridSearchCV(reg,parameters,cv=5)
    #cv.fit(X_train,y_train.ravel())
    #display(cv)
    reg.fit(X_train,y_train)

    # Testing the dataset on trained model
    y_pred = reg.predict(X_test)
    score = reg.score(X_test,y_test)*100
    print("R square value:" , score)
    sleep(5)
    print(y_pred, y_test)

    # save the model to disk
    filename = 'finalized_match_score_model.pkl'
    pickle.dump(reg, open(filename, 'wb'))

    return "Overall Score Model Complete"

def model_train_player_score(player_score_df):
    x = player_score_df.iloc[:, 1:-1].values
    y = player_score_df.iloc[:, -1].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the dataset
    from sklearn.ensemble import RandomForestRegressor
    reg = RandomForestRegressor(n_estimators=100,max_features=None)
    reg.fit(X_train,y_train)

    # Testing the dataset on trained model
    y_pred = reg.predict(X_test)
    score = reg.score(X_test,y_test)*100
    print("R square value:" , score)
    sleep(5)
    print(y_pred, y_test)

    # save the model to disk
    filename = 'finalized_player_score_model.pkl'
    pickle.dump(reg, open(filename, 'wb'))

    return "Overall Score Model Complete"

def df_from_csv():
    matches_fin_df = pd.read_csv('match_dif_stats.csv')
    player_score_df = pd.read_csv('player_score_stats.csv')

    return matches_fin_df, player_score_df

if __name__ == '__main__':
    #matches_fin_df, player_score_df = match_data_clean(2001, 2020)
    print("---------------------")
    print("Dataframes Completed")
    print("---------------------")
    #matches_fin_df.to_csv('match_dif_stats.csv', encoding="utf-8")
    #player_score_df.to_csv('player_score_stats.csv', encoding="utf-8")
    matches_fin_df, player_score_df = df_from_csv()
    model_train_match_score(matches_fin_df)
    print("---------------------")
    print("Overall Score Model Compelete")
    print("---------------------")
    #model_train_player_score(player_score_df)
    print("---------------------")
    print("Player Score Model Complete")
    print("---------------------")