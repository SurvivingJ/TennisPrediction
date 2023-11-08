from sklearn.linear_model import LinearRegression
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
from simulations import create_player_dict
import re
import statistics
import numpy as np
from time import sleep
import pickle
import random
from sklearn.model_selection import cross_val_score

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



def match_data_clean():
    matches_df = pd.read_csv('Match_Data/atp_matches_2021.csv')
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

    player_dict = create_player_dict()

    for index, row in matches_df.iterrows():
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
            print(num)
            if int(num[0][0]) > int(num[1][0]):
                new_score += 1
            else:
                new_score -= 1
        #print(new_score)
        new_row.append(new_score)
        switch = random.randint(1, 2)

        if switch == 1:
            #print("OLD ROW")
            #print(new_row)
            new_row = [ -i for i in new_row ] 
            #print("NEW ROW")
            #print(new_row)
            #sleep(20)
        
        matches_fin_df.loc[len(matches_fin_df)] = new_row

        '''
        match_df = pd.DataFrame(new_row, columns=['Rank', 'Career Win %','Career Double Fault %','Career Ace %','Career Break Point Saved %','Career Won against Top 10 %','Career Won on Hard Court %','Career Won on Clay Court %','Career Ace Against %', 
        'Career First Serve Points Return Won %', 'Career Points Won %','Current Year Win %','Current Year Double Fault %','Current Year Ace %','Current Year Break Point Saved %','Current Year Won against Top 10 %','Current Year Won on Hard Court %',
        'Current Year Won on Clay Court %', 'Current Year Ace Against %','Current Year First Serve Points Return Won %', 'Current Year Points Won %', 'Score'])
        matches_fin_df = matches_fin_df.append(match_df)
        '''
    return matches_fin_df

def model_train(matches_fin_df):
    x = matches_fin_df.iloc[:, :-1].values
    y = matches_fin_df.iloc[:, -1].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the dataset
    from sklearn.ensemble import RandomForestRegressor
    reg = RandomForestRegressor(n_estimators=1000,max_features=None)
    reg.fit(X_train,y_train)

    # Testing the dataset on trained model
    y_pred = reg.predict(X_test)
    score = reg.score(X_test,y_test)*100
    print("R square value:" , score)
    sleep(5)
    print(y_pred, y_test)

    # save the model to disk
    filename = 'finalized_model.pkl'
    pickle.dump(reg, open(filename, 'wb'))

    # Accuracy
    i = 0
    diff_list = []
    for y in y_pred:
        yt = y_test[i]
        try:
            diff = 1 - (abs(y - yt) / yt)
            # print(f"Accuracy: {diff}")
            diff_list.append(diff)
        except ZeroDivisionError:
            print("ZERO DIV ERROR")
            sleep(3)
            i+= 1
            continue
        i += 1
    
    rounded_diff_list = []
    for d in diff_list:
        d = float(round(d, 2))
        rounded_diff_list.append(d)

    mean = 0
    j = 0
    for item in rounded_diff_list:
        mean += float(round(item, 5))
        j += 1
        mean = float(round(mean, 5))
        print(mean)
    mean = mean / j
    #mean = np.mean(rounded_diff_list,dtype=np.longdouble)
    median = statistics.median(rounded_diff_list)
    stdev = statistics.stdev(rounded_diff_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Stdev: {stdev}")




if __name__ == '__main__':
    matches_fin_df = match_data_clean()
    matches_fin_df.to_csv('match_dif_stats.csv', encoding="utf-8")
    #model_train(matches_fin_df)