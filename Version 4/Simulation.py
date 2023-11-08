from time import sleep
from numpy.core.fromnumeric import mean
import pandas as pd
import pickle
import numpy as np
from Train_Model import create_player_dict
from Format_data import create_diff_row, stats_analysis, parse_match
import statistics
from sklearn import *
import math

def year_sim(year):
    matches_df = pd.read_csv(f'Match_Data/atp_matches_{year}.csv')
    player_dict = create_player_dict()
    matches_correct = 0
    matches_simulated = 0
    total_matches = 0

    for index, row in matches_df.iterrows():
        total_matches += 1
        player1_id = row[7]
        player2_id = row[15]
        try:
            diff_row = create_diff_row(player_dict, player1_id, player2_id)
        except:
            continue
        
        try:
            # Player 1 Prediction
            diff_row_p1 = diff_row

            X_to_pred_p1 = diff_row_p1
            X_new_p1 = np.array(X_to_pred_p1)
            X_new_p1 = X_new_p1.reshape(1, -1)
        except:
            continue

        try:
            filename_p1 = f'Player_Models/{str(player1_id) + ".0"}.pkl'
            with open(filename_p1, 'rb') as file:
                pickle_model_p1 = pickle.load(file)
        except:
            continue

        try:   
            match_score_pred_p1 = pickle_model_p1.predict(X_new_p1)

            # Player 1 Prediction
            diff_row_p2 = [-i for i in diff_row]

            X_to_pred_p2 = diff_row_p2
            X_new_p2 = np.array(X_to_pred_p2)
            X_new_p2 = X_new_p2.reshape(1, -1)
        except:
            continue

        try:
            filename_p2 = f'Player_Models/{str(player2_id) + ".0"}.pkl'
            with open(filename_p2, 'rb') as file:
                pickle_model_p2 = pickle.load(file)
        except:
            continue
        
        try:
            match_score_pred_p2 = pickle_model_p2.predict(X_new_p2)
        except:
            continue
        
        print(f"P1: {match_score_pred_p1} ||||| P2: {match_score_pred_p2}")
        if match_score_pred_p1 == 0 and match_score_pred_p2 == 1:
            matches_simulated += 1
        elif match_score_pred_p1 == 1 and match_score_pred_p2 == 0:
            matches_simulated += 1
            matches_correct += 1
        else:
            continue

        player_dict = parse_match(row, player_dict, player1_id, player2_id, year)
        player_dict = stats_analysis(player_dict, player1_id, player2_id)        
        
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Matches Correct Model: {matches_correct}")
        print(f"Matches Simulated: {matches_simulated}")
        try:
            print(f"Accuracy Model: {matches_correct / matches_simulated * 100}")
        except:
            print("Accuracy Null")
        print("-------------------------------------------")        

    return matches_correct, matches_simulated, total_matches

def year_sim_mega(year):
    matches_df = pd.read_csv(f'Match_Data/atp_matches_{year}.csv')
    player_dict = create_player_dict()
    matches_correct = 0
    matches_simulated = 0
    total_matches = 0
    match_score_correct = 0
    score_diff = []
    balance = 100
    for index, row in matches_df.iterrows():
        total_matches += 1
        player1_id = row[7]
        player2_id = row[15]

        try:
            diff_row = create_diff_row(player_dict, player1_id, player2_id)

        except Exception as e:
            print(e)
            print("OOPS")
            continue
        '''
        try:
            # Player 1 Prediction
            diff_row_p1 = diff_row

            X_to_pred_p1 = diff_row_p1
            X_new_p1 = np.array(X_to_pred_p1)
            X_new_p1 = X_new_p1.reshape(1, -1)
        except:
            continue

        try:
            filename_p1 = f'Player_Models/{str(player1_id) + ".0"}.pkl'
            with open(filename_p1, 'rb') as file:
                pickle_model_p1 = pickle.load(file)
        except:
            continue

        try:   
            indiv_pred_p1 = pickle_model_p1.predict(X_new_p1)

            # Player 1 Prediction
            diff_row_p2 = [-i for i in diff_row]

            X_to_pred_p2 = diff_row_p2
            X_new_p2 = np.array(X_to_pred_p2)
            X_new_p2 = X_new_p2.reshape(1, -1)
        except:
            continue

        try:
            filename_p2 = f'Player_Models/{str(player2_id) + ".0"}.pkl'
            with open(filename_p2, 'rb') as file:
                pickle_model_p2 = pickle.load(file)
        except:
            continue
        
        try:
            indiv_pred_p2 = pickle_model_p2.predict(X_new_p2)
        except:
            continue
        '''
        try:
            # Player 1 Prediction
            diff_row_p1 = diff_row

            X_to_pred_p1 = diff_row_p1
            X_new_p1 = np.array(X_to_pred_p1)
            X_new_p1 = X_new_p1.reshape(1, -1)
        except:
            continue

        try:
            filename_p1 = f'Player_Models/Mega_Model_Logistic_New.pkl'
            with open(filename_p1, 'rb') as file:
                pickle_model_p1 = pickle.load(file)
        except:
            continue

        try:   
            match_score_pred_p1 = pickle_model_p1.predict(X_new_p1)
            prob_pred_p1 = pickle_model_p1.predict_proba(X_new_p1)
        except Exception as e:
            print(e)
            continue

        try:
            # Player 1 Prediction
            diff_row_p2 = [-i for i in diff_row]
            
            if abs(diff_row_p2[-1]) == 1:
                diff_row_p2[-1] = 0
            else:
                diff_row_p2[-1] = 1
            X_to_pred_p2 = diff_row_p2
            X_new_p2 = np.array(X_to_pred_p2)
            X_new_p2 = X_new_p2.reshape(1, -1)
        except Exception as e:
            print(e)
            continue

        try:
            filename_p2 = f'Player_Models/Mega_Model_Logistic_New.pkl'
            with open(filename_p2, 'rb') as file:
                pickle_model_p2 = pickle.load(file)
        except:
            continue
        
        try:
            match_score_pred_p2 = pickle_model_p2.predict(X_new_p2)
            prob_pred_p2 = pickle_model_p1.predict_proba(X_new_p2)
        except:
            continue
        '''
        try:
            abs_diff_row = [abs(i) for i in diff_row]
            X_to_pred_score = abs_diff_row
            X_new_score = np.array(X_to_pred_score)
            X_new_score = X_new_score.reshape(1, -1)
            filename_score = 'Player_Models/finalized_match_score_model.pkl'
            with open(filename_score, 'rb') as file:
                pickle_model_score = pickle.load(file)
            match_score_pred = pickle_model_score.predict(X_new_score)
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
        except Exception as e:
            print(e)
            sleep(100)
            continue
        print(f"P1: {match_score_pred_p1} ||||| P2: {match_score_pred_p2}")

        
        
        print(f"P1: {match_score_pred_p1} ||||| P2: {match_score_pred_p2}")
        print(match_score_pred * 3, score)
        diff = abs(float(match_score_pred) * 3 - float(new_score))
        score_diff.append(diff)
        '''        
        print(f"P1: {match_score_pred_p1} ||||| P2: {match_score_pred_p2}")
        print(f"P1: {prob_pred_p1[0][1]} ||| P2: {prob_pred_p2[0][1]}")
        if match_score_pred_p2 > match_score_pred_p1:
            if prob_pred_p2[0][1] > 0.9998:
                matches_simulated += 1
            '''
            if indiv_pred_p1 == 0 and indiv_pred_p2 == 1:
                print("")
            elif indiv_pred_p1 == 1 and indiv_pred_p2 == 0:
                matches_simulated += 1
                balance -= balance * 0.308
               ''' 
        elif match_score_pred_p2 < match_score_pred_p1:
            if prob_pred_p1[0][1] > 0.9998:
                matches_simulated += 1
                matches_correct += 1
            '''
            if indiv_pred_p1 == 0 and indiv_pred_p2 == 1:
                matches_correct += 1
                matches_simulated += 1
                balance += (0.308 * balance) * 1.8
            elif indiv_pred_p1 == 1 and indiv_pred_p2 == 0:
                print("")
            #if (match_score_pred > 0.62):
                #match_score_correct += 1
            #matches_simulated += 1
            
            #matches_correct += 1
            '''            
            
        player_dict = parse_match(row, player_dict)
        player_dict = stats_analysis(player_dict, player1_id, player2_id)        
        
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Matches Correct Model: {matches_correct}")
        print(f"Matches Simulated: {matches_simulated}")
        print(f"Match Score Correct: {match_score_correct}")
        #print(f"Mean Score Off By: {mean(score_diff)}")
        print(f"Balance: ${balance}")
        try:
            print(f"Accuracy Model: {matches_correct / matches_simulated * 100}")
        except:
            print("Accuracy Null")
        print("-------------------------------------------")        

    return matches_correct, matches_simulated, total_matches, match_score_correct

if __name__ == "__main__":
    matches_correct, matches_simulated, total_matches, match_score_correct = year_sim_mega(2021)
    print(f"Total Matches: {total_matches}")
    print(f"Matches Correct: {matches_correct}")
    print(f"Matches Simulated: {matches_simulated}")
    print(f"Accuracy: {matches_correct / matches_simulated * 100}")
    print(f"Match Score Correct: {match_score_correct}")
    print(f"Accuracy: {match_score_correct / matches_simulated * 100}")