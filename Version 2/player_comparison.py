import pandas as pd
from time import sleep
import datetime

def player_compare(player_stats_df, player1, player2):
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
    
    today = datetime.datetime.now()
    day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
    perc_through_year = float(day_of_year) / 365.0
    
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