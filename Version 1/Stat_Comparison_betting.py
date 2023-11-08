import pandas as pd
import matplotlib.pyplot as plt
import statistics
import csv
import time
import datetime
import random

def read_data(data, *args):
    data = pd.DataFrame()
    for record in args:
        data_temp = pd.read_csv(record)
        data = data.append(data_temp, ignore_index=True, sort=False)
    print("Data Read")
    print(data.shape)

    return data

def weights_setter(weights_dict):
    i = 3
    for i in range(50):
        weights_dict[i] = random.uniform(0.1, 1.0)
    
    return weights_dict

def player_compare(player1, player2, surface, place, weights_dict):
    data_players = pd.read_csv(r'C:\Users\james\Desktop\Coding\Tennis_Prediction\Tennis_Records.csv')
    try:
        player_1 = data_players.loc[data_players['name'] == player1].to_numpy()
        player_2 = data_players.loc[data_players['name'] == player2].to_numpy()
    except:
        return("Data is missing")
    
    if player_1 == []:
        return(f"Data is missing for: {player1}")
    if player_2 == []:
        return(f"Data is missing for: {player2}")

    #print(f"Player 1 Data: {player_1}")
    #print(f"Player 1 Data Shape: {player_1.shape}")
    #print(f"Player 2 Data: {player_2}")
    #print(f"Player 2 Data Shape: {player_2.shape}")
    player_1_score = 0
    player_2_score = 0

    try:
        if place == "Outdoor":
            if surface == "Hard":
                for i in range(3, 50):
                    if i in [23, 24, 25, 26, 29, 30]:
                        continue
                    elif i in [5, 39]:
                        if player_1[0, i] < player_2[0, i]:
                            player_1_score += (1 * weights_dict[i])
                        elif player_1[0, i] > player_2[0, i]:
                            player_2_score += (1 * weights_dict[i])
                    if player_1[0, i] > player_2[0, i]:
                        player_1_score += (1 * weights_dict[i])
                    elif player_1[0, i] < player_2[0, i]:
                        player_2_score += (1 * weights_dict[i])
                    else:
                        continue
            elif surface == "Clay":
                for i in range(3, 50):
                    if i in [25, 26, 27, 28, 29, 30]:
                        continue
                    elif i in [5, 39]:
                        if player_1[0, i] < player_2[0, i]:
                            player_1_score += (1 * weights_dict[i])
                        elif player_1[0, i] > player_2[0, i]:
                            player_2_score += (1 * weights_dict[i])             
                    if player_1[0, i] > player_2[0, i]:
                        player_1_score += (1 * weights_dict[i])
                    elif player_1[0, i] < player_2[0, i]:
                        player_2_score += (1 * weights_dict[i])
                    else:
                        continue
            elif surface == "Grass":
                for i in range(3, 50):
                    if i in [23, 24, 27, 28, 29, 30]:
                        continue
                    elif i in [5, 39]:
                        if player_1[0, i] < player_2[0, i]:
                            player_1_score += (1 * weights_dict[i])
                        elif player_1[0, i] > player_2[0, i]:
                            player_2_score += (1 * weights_dict[i])
                    if player_1[0, i] > player_2[0, i]:
                        player_1_score += (1 * weights_dict[i])
                    elif player_1[0, i] < player_2[0, i]:
                        player_2_score += (1 * weights_dict[i])
                    else:
                        continue
            else:
                next
        else:
            if surface == "Hard":
                if i in [23, 24, 25, 26, 31, 32]:
                        next
                elif i in [5, 39]:
                    if player_1[0, i] < player_2[0, i]:
                        player_1_score += (1 * weights_dict[i])
                    elif player_1[0, i] > player_2[0, i]:
                        player_2_score += (1 * weights_dict[i])
                for i in range(3, 50):
                    if player_1[0, i] > player_2[0, i]:
                        player_1_score += (1 * weights_dict[i])
                    elif player_1[0, i] < player_2[0, i]:
                        player_2_score += (1 * weights_dict[i])
                    else:
                        continue
            elif surface == "Clay":
                for i in range(3, 50):
                    if i in [25, 26, 27, 28, 31, 32]:
                        continue
                    elif i in [5, 39]:
                        if player_1[0, i] < player_2[0, i]:
                            player_1_score += (1 * weights_dict[i])
                        elif player_1[0, i] > player_2[0, i]:
                            player_2_score += (1 * weights_dict[i])
                    if player_1[0, i] > player_2[0, i]:
                        player_1_score += (1 * weights_dict[i])
                    elif player_1[0, i] < player_2[0, i]:
                        player_2_score += (1 * weights_dict[i])
                    else:
                        continue
            elif surface == "Grass":
                for i in range(3, 50):
                    if i in [23, 24, 27, 28, 31, 32]:
                        continue
                    elif i in [5, 39]:
                        if player_1[0, i] < player_2[0, i]:
                            player_1_score += (1 * weights_dict[i])
                        elif player_1[0, i] > player_2[0, i]:
                            player_2_score += (1 * weights_dict[i])
                    if player_1[0, i] > player_2[0, i]:
                        player_1_score += (1 * weights_dict[i])
                    elif player_1[0, i] < player_2[0, i]:
                        player_2_score += (1 * weights_dict[i])
                    else:
                        continue
            else:
                next
    except:
        return("Data is missing")
    return player_1_score, player_2_score

def match_analysis(std_dev_hurdle, odds_hurdle, data):
    balance = 100
    avg_bet = 0
    matches_analysed = 0
    num_correct = 0
    num_incorrect = 0
    score_diff = []
    avg_odds_bet_win = 0
    avg_odds_bet_lose = 0
    #weights_dict = {3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 
    #                21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 
    #                40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 48: 0, 49: 0, 50: 0}
    #weights_dict = weights_setter(weights_dict)
    weights_dict = {3: 0.19690384820438128, 4: 0.10639827477561731, 5: 0.17559272598681447, 6: 0.17432643498749784, 7: 0.12760200807871439, 8: 0.24910098647513845, 9: 0.10463278786506686, 10: 0.838882573570547, 11: 0.5003750765160171, 12: 0.35302592360168916, 13: 0.6725653490130471, 14: 0.7637904771524071, 15: 0.7049693127141243, 16: 0.6024090154800354, 17: 0.20873738175244727, 18: 0.809086480396399, 19: 0.17311930048894464, 20: 0.33205660827779904, 21: 0.3294414918841816, 22: 0.9939275933685108, 23: 0.9751639210256987, 24: 0.6817478463834473, 25: 0.6432947179512744, 26: 0.18500655470500157, 27: 0.9562028332239938, 28: 0.5153965746279571, 29: 0.3907284665999111, 30: 0.9520759404958941, 31: 0.47586300384549973, 32: 0.9397501682330759, 33: 0.31081766889341067, 34: 0.8950602988332453, 35: 0.3631434398195448, 36: 0.9985135254448796, 37: 0.38137119152356147, 38: 0.6215050169150312, 39: 0.117501118156667, 40: 0.5437555038431205, 41: 0.456252240178879, 42: 0.25959571310385476, 43: 0.16611971575218692, 44: 0.36896114818649317, 45: 0.6345392978861084, 46: 0.9844296672304442, 47: 0.5480330799161377, 48: 0.83961129783806, 49: 0.5527382201971582, 50: 0, 0: 0.1079748514334899, 1: 0.8348302669852998, 2: 0.33403010323360405}
    #weights_dict = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}
    for index, row in data.iterrows():
        try:
            player_1_score, player_2_score = player_compare(row.loc["Winner"], row.loc["Loser"], row.loc["Surface"], row.loc["Court"], weights_dict)
            matches_analysed += 1
        except:
            next

        if player_1_score > player_2_score:
            if abs(player_1_score - player_2_score) > std_dev_hurdle:
                '''
                balance = balance - bet + bet * row.loc['AvgW']
                avg_bet += bet
                num_correct += 1
                avg_odds_bet_win += row.loc['AvgW']
                
                if (player_1_score - player_2_score) > 4.80836:
                    bet = 10
                    balance = balance - bet + bet * row.loc['AvgW']
                    avg_bet += bet
                    num_correct += 1
                    avg_odds_bet_win += row.loc['AvgW']
                '''
                if (player_1_score - player_2_score) > 7.7829 and (player_1_score - player_2_score) < 10:
                    bet = balance * 0.05
                    balance = balance - bet + bet * row.loc['AvgW']
                    avg_bet += bet
                    num_correct += 1
                    avg_odds_bet_win += row.loc['AvgW']
                elif (player_1_score - player_2_score) >= 10 and (player_1_score - player_2_score) < 15:
                    bet = balance * 0.1
                    balance = balance - bet + bet * row.loc['AvgW']
                    avg_bet += bet
                    num_correct += 1
                    avg_odds_bet_win += row.loc['AvgW']
                elif (player_1_score - player_2_score) > 15:
                    bet = balance * 0.2
                    balance = balance - bet + bet * row.loc['AvgW']
                    avg_bet += bet
                    num_correct += 1
                    avg_odds_bet_win += row.loc['AvgW']
        else:
            if abs(player_1_score - player_2_score) > std_dev_hurdle:
                '''
                num_incorrect += 1
                balance = balance - bet
                avg_bet += bet
                avg_odds_bet_lose += row.loc['AvgL']
                
                if (player_1_score - player_2_score) < 4.80836:
                    bet = 10
                    num_incorrect += 1
                    balance = balance - bet
                    avg_bet += bet
                    avg_odds_bet_lose += row.loc['AvgL']
                '''
                if abs(player_1_score - player_2_score) > 7.7829 and abs(player_1_score - player_2_score) < 10:
                    bet = balance * 0.05
                    num_incorrect += 1
                    balance = balance - bet
                    avg_bet += bet
                    avg_odds_bet_lose += row.loc['AvgL']
                elif abs(player_1_score - player_2_score) >= 10 and (player_1_score - player_2_score) < 15:
                    bet = balance * 0.1
                    num_incorrect += 1
                    balance = balance - bet
                    avg_bet += bet
                    avg_odds_bet_lose += row.loc['AvgL']
                elif abs(player_1_score - player_2_score) > 15:
                    bet = balance * 0.2
                    balance = balance - bet + bet * row.loc['AvgW']
                    avg_bet += bet
                    num_correct += 1
                    avg_odds_bet_win += row.loc['AvgW']
                    
        temp_score_diff = player_1_score - player_2_score
        score_diff.append(temp_score_diff)
        try:
            print(f"---------------------BET ================= {bet} ------------------------------")
        except:
            print("EMPTY BET")
        print(f"---------------------BALANCE ============= {balance} --------------------------")
        print(f"--------------------ODDS ============== {row.loc['B365W']}-----------------------")
        print(f"--------------------NUM CORRECT ===== {num_correct} -------- NUM INCORRECT ====== {num_incorrect}")
        print(f"--------------------Date & Time ======== {datetime.datetime.now()} ---------------")
        with open('Balance.csv', 'a') as f:
            file_writer = csv.writer(f, delimiter=',', lineterminator='\n')
            file_writer.writerow([balance, row.loc['AvgW']])
    matches_bet_on = num_correct + num_incorrect
    if matches_bet_on == 0:
        avg_bet = 0
    else:
        avg_bet = avg_bet / matches_bet_on
    if num_correct == 0:
        avg_odds_bet_win = 0
    if num_incorrect == 0:
        avg_odds_bet_lose = 0
    if num_correct != 0 and num_incorrect != 0:
        avg_odds_bet_win = avg_odds_bet_win / num_correct
        avg_odds_bet_lose = avg_odds_bet_lose / num_incorrect
    #Stats Calculations
    avg_score_diff = sum(score_diff) / len(score_diff)
    standard_deviation = statistics.stdev(score_diff)
    return matches_analysed, matches_bet_on, balance, avg_bet, avg_score_diff, standard_deviation, num_correct, num_incorrect, avg_odds_bet_win, avg_odds_bet_lose, weights_dict

print(player_compare('Escoffier A.', 'Fomin S.', 'Clay', 'Outdoor', weights_dict={3: 0.19690384820438128, 4: 0.10639827477561731, 5: 0.17559272598681447, 6: 0.17432643498749784, 7: 0.12760200807871439, 8: 0.24910098647513845, 9: 0.10463278786506686, 10: 0.838882573570547, 11: 0.5003750765160171, 12: 0.35302592360168916, 13: 0.6725653490130471, 14: 0.7637904771524071, 15: 0.7049693127141243, 16: 0.6024090154800354, 17: 0.20873738175244727, 18: 0.809086480396399, 19: 0.17311930048894464, 20: 0.33205660827779904, 21: 0.3294414918841816, 22: 0.9939275933685108, 23: 0.9751639210256987, 24: 0.6817478463834473, 25: 0.6432947179512744, 26: 0.18500655470500157, 27: 0.9562028332239938, 28: 0.5153965746279571, 29: 0.3907284665999111, 30: 0.9520759404958941, 31: 0.47586300384549973, 32: 0.9397501682330759, 33: 0.31081766889341067, 34: 0.8950602988332453, 35: 0.3631434398195448, 36: 0.9985135254448796, 37: 0.38137119152356147, 38: 0.6215050169150312, 39: 0.117501118156667, 40: 0.5437555038431205, 41: 0.456252240178879, 42: 0.25959571310385476, 43: 0.16611971575218692, 44: 0.36896114818649317, 45: 0.6345392978861084, 46: 0.9844296672304442, 47: 0.5480330799161377, 48: 0.83961129783806, 49: 0.5527382201971582, 50: 0, 0: 0.1079748514334899, 1: 0.8348302669852998, 2: 0.33403010323360405}))