import pandas as pd
import pickle
import numpy as np
from train_model import create_diff_row, create_player_dict, parse_match, stats_analysis, write_csv, player_compare
import statistics

def year_sim(year):
    matches_df = pd.read_csv(f'Match_Data/atp_matches_{year}.csv')
    player_dict = create_player_dict()
    matches_correct_model = 0
    matches_correct_v1 = 0
    matches_simulated = 0
    score_diff_arr = []
    balance = 0
    min_score_diff_arr = []
    for index, row in matches_df.iterrows():
        player1_id = row[7]
        player2_id = row[15]
        try:
            diff_row = create_diff_row(player_dict, player1_id, player2_id)
        except:
            continue

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

        diff_row = [ abs(i) for i in diff_row]

        X_to_pred = diff_row
        X_new = np.array(X_to_pred)
        X_new = X_new.reshape(1, -1)

        filename = 'finalized_match_score_model.pkl'
        with open(filename, 'rb') as file:
            pickle_model = pickle.load(file)
        
        match_score_pred = pickle_model.predict(X_new)

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

        # Calculating player scores
        player_df_raw = pd.read_csv('player_stats.csv')
        player_1_score, player_2_score = player_compare(player_df_raw, player1_id, player2_id, perc_through_year)

        X_to_pred = [player_1_score, player_2_score]
        X_new = np.array(X_to_pred)
        X_new = X_new.reshape(1, -1)


        filename = 'finalized_player_score_model.pkl'
        with open(filename, 'rb') as file:
            pickle_model = pickle.load(file)
        
        player_score_pred = pickle_model.predict(X_new)

        if player_score_pred < 0.5:
            matches_correct_model += 1
        
        if match_score_pred > 1.75:
            if abs(player_1_score - player_2_score) > 3:
                if player_1_score > player_2_score:
                    balance = balance - 10 + 10 * 1.3
                    matches_correct_v1 += 1
                else:
                    balance -= 10
                matches_simulated += 1

        player_dict = parse_match(row, player_dict, player1_id, player2_id, year)
        player_dict = stats_analysis(player_dict, player1_id, player2_id)
        write_csv(player_dict)
        

        score_diff = abs(match_score_pred - new_score)
        if score_diff < 0.25:
            min_score_diff_arr.append(score_diff)
        score_diff_arr.append(score_diff)
        print('-------------------------------------------')
        print(f"Predicted Match Score: {match_score_pred}")
        print(f"Actual Match Score: {new_score}")
        print(f"Avg Diff: {np.mean(score_diff_arr)}")
        print(f"<0.25 Num: {len(min_score_diff_arr)/len(score_diff_arr) * 100}")
        
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Matches Correct Model: {matches_correct_model}")
        print(f"Matches Simulated: {matches_simulated}")
        try:
            print(f"Accuracy Model: {matches_correct_model / matches_simulated * 100}")
        except:
            print("Accuracy Null")
        print("-------------------------------------------")

        print("++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Matches Correct: {matches_correct_v1}")
        print(f"Matches Simulated: {matches_simulated}")
        try:
            print(f"Accuracy V1: {matches_correct_v1 / matches_simulated * 100}")
        except:
            print("Accuracy Null")
        print("-------------------------------------------")
        print(f"BALANCE: {balance}")
        

    return matches_correct, matches_simulated

if __name__ == "__main__":
    matches_correct, matches_simulated = year_sim(2020)
    print(f"Matches Correct: {matches_correct}")
    print(f"Matches Simulated: {matches_simulated}")
    print(f"Accuracy: {matches_correct / matches_simulated * 100}")
