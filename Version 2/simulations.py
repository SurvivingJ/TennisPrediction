import pandas as pd
from time import sleep
import csv
import linecache
import sys
import statistics
import pickle
import numpy as np

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))


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

def parse_matches(row, player_dict, player1_id, player2_id):
    matches_yr = '2019'
    curr_yr = '2019'

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
        PrintException()

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
            PrintException()
            
    print("Matches Finished")
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
    print("HI")
    # Reset variables
    player1_id = 0
    player2_id = 0

    player1_score = 0
    player2_score = 0

    # Find players' ids
    for index, row in player_stats_df.iterrows():
        if player1_id != 0 and player2_id != 0:
            break

        if row[1] == player1:
            player1_id = index
        elif row[1] == player2:
            player2_id = index
        else:
            continue
    print(player1)
    print(player2)
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

def comparison_sim():
    matches_df = pd.read_csv('Version 2/Match_Data/atp_matches_2019.csv')    
    matches_simulated = 0
    matches_correct = 0

    # Read in player data
    player_stats_df = pd.read_csv('Version 2/player_stats.csv')

    player_dict = create_player_dict()

    balance = 0

    for index, row in matches_df.iterrows():
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
        
        player1 = row[10]
        player2 = row[18]
        
        player1_id = row[7]
        player2_id = row[15]
        
        player1_score, player2_score = player_compare(player_stats_df, player1, player2, perc_through_year)
        print(player1_score, player2_score)
        score_diff = abs(player1_score - player2_score)
        print(score_diff)
        if score_diff > 4.4436:
            matches_simulated += 1
            if player1_score > player2_score:
                matches_correct += 1



        '''
        with open('scores.txt', "a") as f:
            f.write(f"{str(score_diff)} \n")
        f.close()
        '''
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Matches Correct: {matches_correct}")
        print(f"Matches Simulated: {matches_simulated}")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++") 
        #player_dict = parse_matches(row, player_dict, player1_id, player2_id)
        #player_dict = stats_analysis(player_dict, row[7], row[15])
    
    write_csv(player_dict)
        
    
    return matches_correct, matches_simulated


def player_compare_weight_calc(player_stats_df, player1, player2, column):
    # Reset variables
    player1_id = 0
    player2_id = 0

    player1_score = 0
    player2_score = 0

    # Find players' ids
    for index, row in player_stats_df.iterrows():
        if player1_id != 0 and player2_id != 0:
            break

        if row[1] == player1:
            player1_id = index
        elif row[1] == player2:
            player2_id = index
        else:
            continue
    
    # Relevant columns for analysis
    rel_columns_pos = [3, 21, 23, 24, 25, 26, 27, 33, 36, 52, 54, 55, 56, 57, 58, 64, 67]
    rel_columns_neg = [2, 22, 30, 53, 61]

    print(f"Player 1: {player_stats_df.iloc[player1_id][column]}")
    print(f"Player 2: {player_stats_df.iloc[player2_id][column]}")
    # Compare players' values and score them
    if player_stats_df.iloc[player1_id][column] != 0 and player_stats_df.iloc[player2_id][column] != 0:
        if column in rel_columns_pos:
            if player_stats_df.iloc[player1_id][column] > player_stats_df.iloc[player2_id][column]:
                player1_score += 1
            elif player_stats_df.iloc[player1_id][column] < player_stats_df.iloc[player2_id][column]:
                player2_score += 1
            else:
                print("")
        elif column in rel_columns_neg:
            if player_stats_df.iloc[player1_id][column] < player_stats_df.iloc[player2_id][column]:
                player1_score += 1
            elif player_stats_df.iloc[player1_id][column] > player_stats_df.iloc[player2_id][column]:
                player2_score += 1
            else:
                print("")
    else:
        player1_score = 0
        player2_score = 0

    return player1_score, player2_score


def comparison_sim_weight_calc():
    matches_df = pd.read_csv('./Match_Data/atp_matches_2019.csv')    
    matches_simulated = 0
    matches_correct = 0
    columns = [56, 57, 58, 67]
    # Read in player data
    player_stats_df = pd.read_csv('player_stats.csv')

    player_dict = create_player_dict()
    
    for column in columns:
        print(f"Column:{column}")
        matches_correct = 0
        matches_simulated = 0
        for index, row in matches_df.iterrows():
            player1 = row[10]
            player2 = row[18]
            player1_id = row[7]
            player2_id = row[15]
            player1_score, player2_score = player_compare_weight_calc(player_stats_df, player1, player2, column)
            

            if player1_score > player2_score:
                matches_correct += 1
                matches_simulated += 1
            elif player1_score == 0 and player2_score == 0:
                print("")
            elif player2_score > player1_score:
                matches_simulated += 1
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"Matches Correct: {matches_correct}")
            print(f"Matches Simulated: {matches_simulated}")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")

            player_dict = parse_matches(row, player_dict, player1_id, player2_id)
            player_dict = stats_analysis(player_dict, row[7], row[15])
        
        with open('results.txt', "a") as f:
            f.write(f"{matches_correct}, {matches_simulated}, {column} \n")
        f.close()

        player_dict = create_player_dict()
        
    
    return matches_correct, matches_simulated


def comparison_sim_forest():
    matches_df = pd.read_csv('Match_Data/atp_matches_2021.csv')    
    matches_simulated = 0
    matches_correct = 0

    for index, row in matches_df.iterrows():
        player1 = row[10]
        player2 = row[18]
        player1_id = row[7]
        player2_id = row[15]
        player_dict = create_player_dict()
        
        X_to_pred = create_diff_row(player_dict, player1_id, player2_id)
        X_new = np.array(X_to_pred)
        X_new = X_new.reshape(1, -1)
        print(X_new)

        filename = 'finalized_model.pkl'
        with open(filename, 'rb') as file:
            pickle_model = pickle.load(file)
        
        y_new = pickle_model.predict(X_new)
        
        #with open('forest_results.txt', 'a') as f:
        #    f.write(str(y_new[0]))
        #    f.write('\n')
        
        print(y_new)
        if abs(y_new[0]) > 1.3:
            if y_new > 0:
                matches_correct += 1
                matches_simulated += 1
            elif y_new < 0:
                matches_simulated += 1
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Matches Correct: {matches_correct}")
        print(f"Matches Simulated: {matches_simulated}")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")

        player_dict = parse_matches(row, player_dict, player1_id, player2_id)
        player_dict = stats_analysis(player_dict, row[7], row[15])
        
    return matches_correct, matches_simulated

def forest_score():
    matches_df = pd.read_csv('Match_Data/atp_matches_2021.csv')    
    matches_simulated_forest = 0
    matches_correct_forest = 0
    matches_simulated_v1 = 0
    matches_correct_v1 = 0
    player_stats_df = pd.read_csv('player_stats.csv')

    for index, row in matches_df.iterrows():
        player1 = row[10]
        player2 = row[18]
        player1_id = row[7]
        player2_id = row[15]
        player_dict = create_player_dict()
        
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

        # See prediction using Version 1 system
        player1_score, player2_score = player_compare(player_stats_df, player1, player2, perc_through_year)

        X_to_pred = create_diff_row(player_dict, player1_id, player2_id)
        X_new = np.array(X_to_pred)
        X_new = X_new.reshape(1, -1)
        print(X_new)

        filename = 'finalized_model.pkl'
        with open(filename, 'rb') as file:
            pickle_model = pickle.load(file)
        
        y_new = pickle_model.predict(X_new)
        
        #with open('forest_results.txt', 'a') as f:
        #    f.write(str(y_new[0]))
        #    f.write('\n')
        
        print(y_new)
        if abs(y_new[0]) > 0.5:
            if player1_score > player2_score:
                matches_correct_v1 += 1
                matches_simulated_v1 += 1
            else:
                matches_simulated_v1 += 1

            if y_new > 0:
                matches_correct_forest += 1
                matches_simulated_forest += 1
            elif y_new < 0:
                matches_simulated_forest += 1
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Matches Correct Forest: {matches_correct_forest}")
        print(f"Matches Correct V1: {matches_correct_v1}")
        print(f"Matches Simulated: {matches_simulated_v1}")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")

        player_dict = parse_matches(row, player_dict, player1_id, player2_id)
        player_dict = stats_analysis(player_dict, row[7], row[15])

    return matches_correct_v1, matches_correct_forest, matches_simulated_forest, matches_simulated_v1

def forest_list():
    f = open('forest_results.txt', 'r+')
    lines = [line for line in f.readlines()]
    f.close()
    matches_simulated = 0
    matches_correct = 0
    balance = 100
    for item in lines:
        if abs(float(item)) > 0.5:
            if float(item) > 0:
                balance = balance - 50 + 50*1.15
                matches_correct += 1
                matches_simulated += 1
            else:
                balance = balance - 50
                matches_simulated += 1
    print(f"Balance: {balance}")
    return matches_correct, matches_simulated

def calc_score_stats():
    scores = []
    with open('scores.txt', "r") as f:
            for line in f:
                scores.append(float(line))
    f.close()

    mean = statistics.mean(scores)
    st_dev_hurdle = statistics.stdev(scores)
    print(mean)
    print(st_dev_hurdle)
    print(f"1 stdev above: {mean + st_dev_hurdle}")
    print(f"2 stdev above: {mean + 2 * st_dev_hurdle}")

    
if __name__ == '__main__':
    #calc_score_stats()
    #sleep(5)

    matches_correct_v1, matches_correct_forest, matches_simulated_forest, matches_simulated_v1 = forest_score()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Matches Correct Forest: {matches_correct_forest}")
    print(f"Forest Accuracy: {matches_correct_forest/matches_simulated_v1*100}")
    print(f"Matches Correct Forest: {matches_correct_v1}")
    print(f"Forest Accuracy: {matches_correct_v1/matches_simulated_v1*100}")
    print(f"Matches Simulated: {matches_simulated_v1}")
    print(f"PROGRAM COMPLETE")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    