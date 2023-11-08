import pandas as pd
from Train_Model import create_diff_row
import pickle
from Simulation import create_player_dict
import numpy as np

if __name__ == '__main__':
    player_stats_df = pd.read_csv('player_stats.csv')
    p1 = 'Renis Shapovalov'
    p2 = 'Cameron Norrie'
    odds1 = 0
    odds2 = 0

    player_dict = create_player_dict()
    player1_id = 0
    player2_id = 0
    for index, player in player_dict.items():
        print(index)
        print(player)
        if player[1] == p1:
            player1_id = index
        elif player[1] == p2:
            player2_id = index
        elif player1_id != 0 and player2_id != 0:
            break
        else:
            next
    
    diff_row = create_diff_row(player_dict, player1_id, player2_id)
    try:    
        # Player 1 Prediction
        diff_row_p1 = diff_row

        X_to_pred_p1 = diff_row_p1
        X_new_p1 = np.array(X_to_pred_p1)
        X_new_p1 = X_new_p1.reshape(1, -1)
    except:
        print("")

    try:
        filename_p1 = f'Player_Models/{str(player1_id) + ".0"}.pkl'
        with open(filename_p1, 'rb') as file:
            pickle_model_p1 = pickle.load(file)
    except:
        print("")

    try:   
        indiv_pred_p1 = pickle_model_p1.predict(X_new_p1)

        # Player 1 Prediction
        diff_row_p2 = [-i for i in diff_row]

        X_to_pred_p2 = diff_row_p2
        X_new_p2 = np.array(X_to_pred_p2)
        X_new_p2 = X_new_p2.reshape(1, -1)
    except:
        print("")

    try:
        filename_p2 = f'Player_Models/{str(player2_id) + ".0"}.pkl'
        with open(filename_p2, 'rb') as file:
            pickle_model_p2 = pickle.load(file)
    except:
        print("")

    try:
        indiv_pred_p2 = pickle_model_p2.predict(X_new_p2)
    except:
        print("")

    try:
        # Player 1 Prediction
        diff_row_p1 = diff_row

        X_to_pred_p1 = diff_row_p1
        X_new_p1 = np.array(X_to_pred_p1)
        X_new_p1 = X_new_p1.reshape(1, -1)
    except:
        print("!!")

    try:
        filename_p1 = f'Player_Models/Mega_Model_Rand_Forest.pkl'
        with open(filename_p1, 'rb') as file:
            pickle_model_p1 = pickle.load(file)
    except:
        print("!!!")

    try:   
        match_score_pred_p1 = pickle_model_p1.predict(X_new_p1)
    except Exception as e:
        print(e)
        print("!?")

    try:
        # Player 1 Prediction
        diff_row_p2 = [-i for i in diff_row]

        X_to_pred_p2 = diff_row_p2
        X_new_p2 = np.array(X_to_pred_p2)
        X_new_p2 = X_new_p2.reshape(1, -1)
    except Exception as e:
        print(e)
        print("!!!!")

    try:
        filename_p2 = f'Player_Models/Mega_Model_Rand_Forest.pkl'
        with open(filename_p2, 'rb') as file:
            pickle_model_p2 = pickle.load(file)
    except:
        print("!!!!!")
    
    try:
        match_score_pred_p2 = pickle_model_p2.predict(X_new_p2)
    except:
        print("!!!!!!")

    if abs(match_score_pred_p1) == 0 and abs(match_score_pred_p2) == 1:
            if indiv_pred_p1 == 1 and indiv_pred_p2 == 0:
                print(f"{p2} will WIN.")
    elif abs(match_score_pred_p1) == 1 and abs(match_score_pred_p2) == 0:
        if indiv_pred_p1 == 0 and indiv_pred_p2 == 1:
            print(f"{p1} will WIN.")