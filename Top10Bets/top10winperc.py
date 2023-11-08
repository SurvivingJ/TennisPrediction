import pandas as pd
from time import sleep
year = 2002
year_end_bal = []
year_end_avg_odds = []
year_end_acc = []

while year != 2022:
    print(f"YEAR: {year}")
    matches=f'{year}.csv'
    try:
        df = pd.read_csv(matches)
        wins = 0
        losses = 0
        bal = 100
        num_matches = 0
        odds = 0
        rank = 4
        perc_bet = 0.1
        # Percentage Bet
        for index, row in df.iterrows():
            try:
                if row[7] == '1st Round' or row[7] == '2nd Round':
                    if int(row[11]) < rank or int(row[12]) < rank:
                        
                        if int(row[11]) < rank:
                            odds += float(row['B365W'])
                            num_matches += 1
                            wins += 1
                            bal = bal - bal * perc_bet + bal * perc_bet * float(row['B365W'])
                        else:
                            losses += 1
                            bal = bal - bal * perc_bet
                    
            except Exception as e:
                print(e)
                continue
        '''
        # Flat Bet
        flat_bet = 10
        for index, row in df.iterrows():
            if row[7] == '1st Round' or row[7] == '2nd Round':
                if row[11] < rank or row[12] < rank:
                    
                    if row[11] < rank:
                        odds += row[19]
                        num_matches += 1
                        wins += 1
                        bal = bal - flat_bet + flat_bet * row[19]
                    else:
                        losses += 1
                        bal = bal - flat_bet
        '''
        accuracy = wins / (wins + losses)
        avg_odds = odds / num_matches
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Accuracy: {accuracy}")
        print(f"Balance: {bal}")
        print(f"Avg Odds: ${avg_odds}")
        year_end_bal.append(bal)
        year_end_avg_odds.append(avg_odds)
        year_end_acc.append(accuracy)
        year += 1
    except Exception as e:
        print(e)
        year += 1
        continue

print(f"BALANCES: {year_end_bal}")
print(f"ODDS: {year_end_avg_odds}")
print(f"ACCURACY: {year_end_acc}")