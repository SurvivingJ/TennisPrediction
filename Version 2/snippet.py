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

    # Compare players' values and score them
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

    return player1_score, player2_score


def comparison_sim_weight_calc():
    matches_df = pd.read_csv('./Match_Data/atp_matches_2019.csv')    
    matches_simulated = 0
    matches_correct = 0
    columns = [3, 21, 23, 24, 25, 26, 27, 33, 36, 52, 54, 55, 56, 57, 58, 64, 67, 2, 22, 30, 53, 61]
    # Read in player data
    player_stats_df = pd.read_csv('player_stats.csv')

    player_dict = create_player_dict()
    
    for column in columns:
        for index, row in matches_df.iterrows():
            player1 = row[10]
            player2 = row[18]
            player1_id = row[7]
            player2_id = row[15]
            player1_score, player2_score = player_compare_weight_calc(player_stats_df, player1, player2, column)
            matches_simulated += 1

            if player1_score > player2_score:
                matches_correct += 1
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"Matches Correct: {matches_correct}")
            print(f"Matches Simulated: {matches_simulated}")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")

            player_dict = parse_matches(row, player_dict, player1_id, player2_id)
            player_dict = stats_analysis(player_dict, row[7], row[15])
        
        with open('results.txt', "a") as f:
            f.write([matches_correct, matches_simulated, column])
        f.close()

        player_dict = create_player_dict()
        
    
    return matches_correct, matches_simulated


