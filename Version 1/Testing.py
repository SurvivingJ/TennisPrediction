import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import time
sns.set_style("darkgrid")

data = pd.read_csv("2019_results.csv", low_memory=False)
data.Date = data.Date.apply(lambda x:datetime.strptime(x, '%m/%d/%Y'))

balance = 0

#Betting based on odds
for index, row in data.iterrows():
    B365W_odds = row['B365W']
    B365L_odds = row['B365L']

    if B365W_odds < B365L_odds:
        balance = balance - 5 + (5*B365W_odds)
    else:
        balance = balance - 5

print("Final balance: " + str(balance))

balance = 0
print(balance)
#Betting based on highest rank
for index, row in data.iterrows():
    Rank_winner = row['WRank']
    Rank_loser = row['LRank']
    B365W_odds = row['B365W']
    B365L_odds = row['B365L']
    print(B365W_odds, B365L_odds)

    if pd.isna(row['B365W']) == True or pd.isna(row['B365L']) == True:
        next
    elif Rank_winner > Rank_loser:
        balance = balance - 5 + (5*B365W_odds)
    else:
        balance = balance - 5
    #print(balance)
    #time.sleep(1)

print("Final balance: " + str(balance))
