from player_comparison import player_compare
from simulations import create_player_dict
import pandas as pd
from train_players import create_diff_row
import pickle
from simulations import create_player_dict
import numpy as np

if __name__ == '__main__':
    player_stats_df = pd.read_csv('player_stats.csv')
    p1 = 'Illya Marchenko'
    p2 = 'Marco Cecchinato'
    odds1 = 0
    odds2 = 0
    player1_score, player2_score = player_compare(player_stats_df, p1, p2)
    score_diff = abs(player1_score - player2_score)
    print(score_diff)

    player_dict = create_player_dict()
    player1_id = 0
    player2_id = 0
    for index, player in player_dict.items():
        if player[1] == p1:
            player1_id = index
        elif player[1] == p2:
            player2_id = index
        elif player1_id != 0 and player2_id != 0:
            break
        else:
            next
    
    X_to_pred = create_diff_row(player_dict, player1_id, player2_id)
    X_new = np.array(X_to_pred)
    X_new = X_new.reshape(1, -1)
    print(X_new)

    filename = 'finalized_model.pkl'
    with open(filename, 'rb') as file:
        pickle_model = pickle.load(file)
    
    y_new = pickle_model.predict(X_new)
    print(y_new)
    

    if player1_score > player2_score:
        print("Bet on " + p1)
    else:
        print("Bet on " + p2)

    if score_diff > 6.4419:
        print("Bet $30")
    elif score_diff <= 6.4419 and score_diff > 4.4436:
        print("Bet $10")