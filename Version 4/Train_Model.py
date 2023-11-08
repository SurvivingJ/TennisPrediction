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
import multiprocessing as mp
from multiprocessing import cpu_count
import tqdm
from tqdm_multi_thread import TqdmMultiThreadFactory
import random

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
    'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %', 'Score', 'Player 1 ID', 'Player 2 ID'])

    player_df_raw = pd.read_csv('player_stats.csv')
    player_df = player_df_raw[['player_id','Rank', 'Career Win %','Career Double Fault %','Career Ace %','Career Break Point Saved %','Career Won against Top 10 %','Career Won on Hard Court %','Career Won on Clay Court %','Career Ace Against %', 
    'Career First Serve Points Return Won %', 'Career Points Won %','Current Year Win %','Current Year Double Fault %','Current Year Ace %','Current Year Break Point Saved %','Current Year Won against Top 10 %','Current Year Won on Hard Court %',
    'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %']]

    player_comb_df = pd.DataFrame(columns=['Rank', 'Career Win %','Career Double Fault %','Career Ace %','Career Break Point Saved %','Career Won against Top 10 %','Career Won on Hard Court %','Career Won on Clay Court %','Career Ace Against %', 
    'Career First Serve Points Return Won %', 'Career Points Won %','Current Year Win %','Current Year Double Fault %','Current Year Ace %','Current Year Break Point Saved %','Current Year Won against Top 10 %','Current Year Won on Hard Court %',
    'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %'])

    player_dict = create_player_dict()

    year = 2021
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
        new_row.append(player1_id)
        new_row.append(player2_id)
        
        matches_fin_df.loc[len(matches_fin_df)] = new_row
        
        player_dict = parse_match(row, player_dict, player1_id, player2_id, year)
        player_dict = stats_analysis(player_dict, player1_id, player2_id)

        print('---------------------------------------------')
        print(f"Match | {player1_id} | v | {player2_id} | Complete")
        print('---------------------------------------------')

    return matches_fin_df

def model_train_match_score(player_id, matches_fin_df):
    try:
        x = matches_fin_df.iloc[:, 0:-4].values
        y = matches_fin_df.iloc[:, -3].values

        # Splitting the dataset into the Training set and Test set
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

        # Feature Scaling
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        # Training the dataset
        from sklearn.linear_model import LogisticRegression
        from sklearn.ensemble import RandomForestRegressor

        reg = RandomForestRegressor()
        #reg = LogisticRegression(solver = 'lbfgs')
        reg.fit(X_train,y_train)

        # Testing the dataset on trained model
        y_pred = reg.predict(X_test)
        score = reg.score(X_test,y_test)*100
        
        print("---------------------------------------------")
        print(f"Player: {player_id}")
        print("R square value:" , score)
        print("---------------------------------------------")
        
        # save the model to disk
        filename = f'Player_Models/{player_id}.pkl'
        pickle.dump(reg, open(filename, 'wb'))
    except:
        print(f"{player_id} Failed")
        return f"{player_id} Failed"
    return f"{player_id} Complete"

def df_from_csv():
    matches_fin_df = pd.read_csv('matches.csv')

    return matches_fin_df

def player_match_to_df(player_id, matches_df):
    player_match_list = []
    for index, row in matches_df.iterrows():
        new_row = row
        if new_row[-2] == player_id:
            new_row[-3] = 1
            player_match_list.append(new_row)
        elif new_row[-1] == player_id:
            new_row[-3] = 0
            inv_row = [-i for i in new_row]
            player_match_list.append(inv_row)
        else:
            continue
    
    i = 0
    for match in player_match_list:
        if match[-3] == 1:
            i+= 1
        else:
            continue
    
    player_match_arr = np.array(player_match_list)
    if i == 0:
        player_match_df = pd.DataFrame([])
    else:
        #print(len(player_match_arr))
        #print(type(player_match_arr))
        player_match_df = pd.DataFrame(player_match_arr)


    return player_match_df

def player_eval(player):
    matches_fin_df = df_from_csv()
    player_matches = player_match_to_df(player, matches_fin_df)

    if len(player_matches) == 0:
        print(f"Player {player}: No Matches")
    else:
        model_train_match_score(player, player_matches)
        print(f"Player {player}: Analysis Complete")

    return f"Player {player} Complete"

def player_selection():
    matches_df = df_from_csv()
    player_dict = {}

    for index, row in matches_df.iterrows():
        if row[-2] in player_dict:
            player_dict[row[-2]] += 1
        else:
            player_dict[row[-2]] = 1
        
        if row[-1] in player_dict:
            player_dict[row[-1]] += 1
        else:
            player_dict[row[-1]] = 1

    threshold_player_dict = {}

    for player in player_dict:
        if player_dict[player] >= 10:
            threshold_player_dict[player] = 1
    
    return threshold_player_dict

def mega_match_df():
    matches_df = df_from_csv()
    list_matches_df = matches_df.values.tolist()
    flipped_matches_df = matches_df.values.tolist()
    match_list = []
    total_items = len(flipped_matches_df)
    i = 0
    for match in list_matches_df:
        new_match = match

        rand_int = random.randint(0, 1)

        if rand_int == 0:
            new_match = [-i for i in new_match]
            new_match[-1] = 0
        
        match_list.append(new_match)
    
    for match in flipped_matches_df:
        i += 1
        sg.one_line_progress_meter('My meter', i, total_items, 'my meter' )
        new_match = match
        new_match = [round(-i, 4) for i in match]
        new_match[-1] = abs(new_match[-1])

        if new_match[-1] == 0:
            new_match[-1] = 1
        else:
            new_match[-1] = 0

        
        match_list.append(new_match)
    f32_match_list = np.float32(match_list)
    final_flipped_match_df = pd.DataFrame(f32_match_list)
    #f32_list_matches_df = np.float32(list_matches_df)
    #original_match_df = pd.DataFrame(f32_list_matches_df)
    print(len(final_flipped_match_df))
    #final_flipped_match_df.to_csv('match_dif_stats.csv', encoding="utf-8")

    #final_match_df = pd.concat([original_match_df, final_flipped_match_df])
    #final_match_df.pop(0)
    #final_match_df.pop(1)
    #final_match_df.pop(2)
    #final_match_df.pop(3)
    #final_match_df.pop(4)
    #final_match_df.pop(5)
    #final_match_df.pop(6)
    #final_match_df.pop(7)
    #final_match_df.pop(8)
    #print(final_match_df)
    #print(len(final_match_df))
    print("Mega Match Dataframe Complete")
    return final_flipped_match_df

def train_mega_model(matches_fin_df):
    x = matches_fin_df.iloc[:, 0:-1].values
    y = matches_fin_df.iloc[:, -1].values
    print(y)
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.10, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the dataset
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestRegressor

    reg = RandomForestRegressor(n_estimators=500, max_depth=10)
    #reg = LogisticRegression(solver = 'lbfgs')
    reg.fit(X_train,y_train)

    # Testing the dataset on trained model
    y_pred = reg.predict(X_test)
    score = reg.score(X_test,y_test)*100
    
    print("---------------------------------------------")
    print("R square value:" , score)
    print("---------------------------------------------")
    
    # save the model to disk
    filename = f'Player_Models/Mega_Model_Rand_Forest_New.pkl'
    pickle.dump(reg, open(filename, 'wb'))

    return f"Model Complete"

def match_score_df():
    match_df = df_from_csv()
    abs_match_list = []

    for index, row in match_df.iterrows():
        new_row = [abs(i) for i in row]
        print(new_row[-3])
        new_row[-3] = float(new_row[-3] / 3)
        #print(new_row[-3])
        abs_match_list.append(new_row)
    
    f32_abs_match_list = np.float32(abs_match_list)
    f32_match_df = pd.DataFrame(f32_abs_match_list)
    return f32_match_df

'''
def model_train_match_score(matches_fin_df):
    x = matches_fin_df.iloc[:, 0:-4].values
    y = matches_fin_df.iloc[:, -3].values
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
    reg = RandomForestRegressor(n_estimators=500, max_depth=10)
    #from sklearn.model_selection import GridSearchCV
    #cv = GridSearchCV(reg,parameters,cv=5)
    #cv.fit(X_train,y_train.ravel())
    #display(cv)
    reg.fit(X_train,y_train)

    # Testing the dataset on trained model
    y_pred = reg.predict(X_test)
    score = reg.score(X_test,y_test)*100
    print("R square value:" , score)
    print(y_pred, y_test)

    # save the model to disk
    filename = 'finalized_match_score_model.pkl'
    pickle.dump(reg, open(filename, 'wb'))

    return "Overall Score Model Complete"
'''
if __name__ == '__main__':
    #matches_fin_df = match_data_clean(1991, 2021)
    #matches_fin_df.to_csv('match_dif_stats.csv', encoding="utf-8")
    '''matches_fin_df = df_from_csv()
    print(matches_fin_df)
    print("---------------------")
    print("Dataframes Completed")
    print("---------------------")
    
    i= 0
    total_items = len(player_dict)
    for player in player_dict:
        i += 1
        sg.one_line_progress_meter('My meter', i, total_items, 'my meter' )
        print(f"Player: {player}")
    '''

    #player_dict = player_selection()
    match_df = mega_match_df()
    train_mega_model(match_df)

    #match_scores_df = match_score_df()
    #model_train_match_score(match_scores_df)
    
    # Progress Bar
    #total_items = len(player_dict)
    #pbar = tqdm.tqdm(total=total_items)
    '''
    for player in player_dict:
        player_eval(player)
        pbar.update(1)
    
    # Multiprocessing
    cpus = cpu_count()
    threads = 4 * (cpus - 1)
    pool_args = [player for player in player_dict]
    p=mp.Pool(threads)
    p.map(player_eval, pool_args)
    #tqdm.tqdm(p.imap(player_eval, pool_args), total=len(pool_args))
    p.close()
    p.join()
    '''    
    