import csv
import pandas as pd
import numpy as np
import datetime
from time import sleep

global player_dict
player_dict = {}

def read_players(players_list_file):
    df = pd.read_csv(players_list_file)
    global player_dict
    for index, row in df.iterrows():
        try:
            name = row[1] + ' ' + row[2]
        except:
            continue

        try:
            player_id = row[0]
        except:
            continue

        player_dict[row[0]] = [player_id, name, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0]
        '''
        #### Columns ####
        Player Id
        Name
        Rank
        Ranking Points
        Career Played
        Career Won
        Height
        Age
        Career Aces
        Career Double Faults
        Career Serve Points
        Career First Serve Won
        Career Second Serve Won
        Career Break Points Saved
        Career Break Points Faced
        Career Played against Top 10
        Career Won against Top 10
        Career Played on Hard court
        Career Won on Hard Court
        Career Played on Clay Court
        Career Won on Clay Court
        Career Win %
        Career Double Fault %
        Career Ace %
        Career Break Point Saved %
        Career Won against Top 10 %
        Career Won on Hard Court %
        Career Won on Clay Court %
        Career Ace Against
        Career Serve Points Against
        Career Ace Against %
        Career First Serve Points Against
        Career First Serve Points Return Won
        Career First Serve Points Return Won %
        Career Points Played
        Career Points Won
        Career Points Won %

        Current Year Played
        Current Year Won
        Current Year Aces
        Current Year Double Faults
        Current Year Serve Points
        Current Year First Serve Won
        Current Year Second Serve Won
        Current Year Break Points Saved
        Current Year Break Points Faced
        Current Year Played against Top 10
        Current Year Won against Top 10
        Current Year Played on Hard court
        Current Year Won on Hard Court
        Current Year Played on Clay Court
        Current Year Won on Clay Court
        Current Year Win %
        Current Year Double Fault %
        Current Year Ace %
        Current Year Break Point Saved %
        Current Year Won against Top 10 %
        Current Year Won on Hard Court %
        Current Year Won on Clay Court %
        Current Year Ace Against
        Current Year Serve Points Against
        Current Year Ace Against %
        Current Year First Serve Points Against
        Current Year First Serve Points Return Won
        Current Year First Serve Points Return Won %
        Current Year Points Played
        Current Year Points Won
        Current Year Points Won %

        Win Streak
        '''

    print('Complete player dictionary template')
    return player_dict

def read_rank(rank_list_file, player_dict):
    df = pd.read_csv(rank_list_file)

    for index, row in df.iterrows():
        # Rank
        player_dict[row[2]][2] = row[1]
        
        # Ranking Points
        player_dict[row[2]][3] = row[3]


    print("Rankings finished")
    return player_dict


def parse_matches(matches_file, player_dict):
    matches_df = pd.read_csv(matches_file, index_col=0)
    matches_yr = str(matches_file[25:29])
    current_dt = datetime.datetime.now()
    #curr_yr = str(current_dt.year)
    curr_yr = '2021'

    # Career Stats
    for index, row in matches_df.iterrows():
        try:
            # Add to # of matches played
            player_dict[row[6]][4] += 1
            player_dict[row[14]][4] += 1

            # Add to winner score
            player_dict[row[6]][5] += 1

            # Player Height
            player_dict[row[6]][6] = row[11]
            player_dict[row[14]][6] = row[19]

            # Player Age
            player_dict[row[6]][7] = row[13]
            player_dict[row[14]][7] = row[21]

            # # of Aces
            player_dict[row[6]][8] += row[26]
            player_dict[row[14]][8] += row[35]

            # # of Double Faults
            player_dict[row[6]][9] += row[27]
            player_dict[row[14]][9] += row[36]

            # # Serve Points
            player_dict[row[6]][10] += row[28]
            player_dict[row[14]][10] += row[37]

            # # First serve won
            player_dict[row[6]][11] += row[30]
            player_dict[row[14]][11] += row[39]

            # # Second serve won
            player_dict[row[6]][12] += row[31]
            player_dict[row[14]][12] += row[40]

            # # Break Points saved
            player_dict[row[6]][13] += row[33]
            player_dict[row[14]][13] += row[42]

            # # Break Points faced
            player_dict[row[6]][14] += row[34]
            player_dict[row[14]][14] += row[43]

            # # Aces against
            player_dict[row[6]][28] += row[35]
            player_dict[row[14]][28] += row[26]

            # # Serve Points Against
            player_dict[row[6]][29] += row[37]
            player_dict[row[14]][29] += row[28]

            # # First Serve Points Against
            player_dict[row[6]][31] += row[38]
            player_dict[row[14]][31] += row[29]

            # # First Serve Points Return Won
            player_dict[row[6]][32] += (row[38] - row[39])
            player_dict[row[14]][32] += (row[29] - row[30])

            # # Points Played
            player_dict[row[6]][34] += (row[28] + row[37])
            player_dict[row[14]][34] += (row[28] + row[37])

            # # Points Won (1st won + 2nd won) + (svpt - df - 1st won - 2nd won)
            player_dict[row[6]][35] += ((row[30] + row[31]) + (row[28] - row[27] - row[30] - row[31]))
            player_dict[row[14]][35] += ((row[39] + row[40]) + (row[37] - row[36] - row[39] - row[40]))

            if row[44] <= 10:
                # Played against Top 10 players
                player_dict[row[14]][15] += 1

            if row[46] <= 10:
                # Wins against Top 10 players
                player_dict[row[6]][16] += 1

                # Played against Top 10 players
                player_dict[row[6]][15] += 1

            if row[1] == 'Hard':
                # Played on Hard court
                player_dict[row[6]][17] += 1

                # Won on Hard court
                player_dict[row[6]][18] += 1

                # Played on Hard court
                player_dict[row[14]][17] += 1
            elif row[1] == 'Clay':
                # Played on Clay court
                player_dict[row[6]][19] += 1

                # Won on Clay court
                player_dict[row[6]][20] += 1

                # Played on Clay court
                player_dict[row[14]][19] += 1
        except:
            continue
    
    # Current Year Stats
    if matches_yr == curr_yr:
        for index, row in matches_df.iterrows():
            try:
                # Add to # of matches played
                player_dict[row[6]][37] += 1
                player_dict[row[14]][37] += 1

                # Add to winner score
                player_dict[row[6]][38] += 1

                # # of Aces
                player_dict[row[6]][39] += row[26]
                player_dict[row[14]][39] += row[35]

                # # of Double Faults
                player_dict[row[6]][40] += row[27]
                player_dict[row[14]][40] += row[36]

                # # Serve Points
                player_dict[row[6]][41] += row[28]
                player_dict[row[14]][41] += row[37]

                # # First serve won
                player_dict[row[6]][42] += row[30]
                player_dict[row[14]][42] += row[39]

                # # Second serve won
                player_dict[row[6]][43] += row[31]
                player_dict[row[14]][43] += row[40]

                # # Break Points saved
                player_dict[row[6]][44] += row[33]
                player_dict[row[14]][44] += row[42]

                # # Break Points faced
                player_dict[row[6]][45] += row[34]
                player_dict[row[14]][45] += row[43]

                # # Aces against
                player_dict[row[6]][59] += row[35]
                player_dict[row[14]][59] += row[26]

                # # Serve Points Against
                player_dict[row[6]][60] += row[37]
                player_dict[row[14]][60] += row[28]

                # # First Serve Points Against
                player_dict[row[6]][62] += row[38]
                player_dict[row[14]][62] += row[29]

                # # First Serve Points Return Won
                player_dict[row[6]][63] += (row[38] - row[39])
                player_dict[row[14]][63] += (row[29] - row[30])

                # # Points Won (1st won + 2nd won) + (svpt - df - 1st won - 2nd won)
                player_dict[row[6]][66] += ((row[30] + row[31]) + (row[28] - row[27] - row[30] - row[31]))
                player_dict[row[14]][66] += ((row[39] + row[40]) + (row[37] - row[36] - row[39] - row[40]))

                if row[44] <= 10:
                    # Player against Top 10 players
                    player_dict[row[14]][46] += 1

                if row[46] <= 10:
                    # Wins against Top 10 players
                    player_dict[row[6]][47] += 1

                    # Played against Top 10 players
                    player_dict[row[6]][46] += 1
                print(row[1])
                if row[1] == 'Hard':
                    # Played on Hard court
                    player_dict[row[6]][48] += 1

                    # Won on Hard court
                    player_dict[row[6]][49] += 1

                    # Played on Hard court
                    player_dict[row[14]][48] += 1
                elif row[1] == 'Clay':
                    # Played on Clay court
                    player_dict[row[6]][50] += 1

                    # Won on Clay court
                    player_dict[row[6]][51] += 1

                    # Played on Clay court
                    player_dict[row[14]][50] += 1
            except:
                continue
            
    print("Matches Finished")
    return player_dict
        
def stats_analysis(player_dict):
    for player in player_dict:
        # Career Win %
        try:
            career_win_perc = player_dict[player][5] / player_dict[player][4]
        except:
            career_win_perc = 0
        
        player_dict[player][21] = career_win_perc

        # Career Double Fault %
        try:
            career_double_fault_perc = player_dict[player][9] / player_dict[player][10]
        except:
            career_double_fault_perc = 0

        player_dict[player][22] = career_double_fault_perc

        # Career Ace %
        try:
            career_ace_perc = player_dict[player][8] / player_dict[player][10]
        except:
            career_ace_perc = 0
        
        player_dict[player][23] = career_ace_perc

        # Career Break Point Saved %
        try:
            career_break_pt_svd_perc = player_dict[player][13] / player_dict[player][14]
        except:
            career_break_pt_svd_perc = 0

        player_dict[player][24] = career_break_pt_svd_perc

        # Career Won against Top 10 %
        try:
            career_won_top_10_perc = player_dict[player][16] / player_dict[player][15]
        except:
            career_won_top_10_perc = 0

        player_dict[player][25] = career_won_top_10_perc
        
        # Career Won on Hard Court %
        try:
            career_won_hard_court_perc = player_dict[player][18] / player_dict[player][17]
        except:
            career_won_hard_court_perc = 0

        player_dict[player][26] = career_won_hard_court_perc

        # Career Won on Clay Court %
        try:
            career_won_clay_court_perc = player_dict[player][20] / player_dict[player][19]
        except:
            career_won_clay_court_perc = 0
        
        player_dict[player][27] = career_won_clay_court_perc

        # Career Ace Against %
        try:
            career_ace_against_perc = player_dict[player][28] / player_dict[player][29]
        except:
            career_ace_against_perc = 0

        player_dict[player][30] = career_ace_against_perc

        # Career First Serve Points Return Won %
        try:
            career_first_serve_pts_return_won_perc = player_dict[player][32] / player_dict[player][31]
        except:
            career_first_serve_pts_return_won_perc = 0

        player_dict[player][33] = career_first_serve_pts_return_won_perc

        # Career Points Won %
        try:
            career_pts_won_perc = player_dict[player][35] / player_dict[player][34]
        except:
            career_pts_won_perc = 0

        player_dict[player][36] = career_pts_won_perc

        # Current Year Win %
        try:
            curr_yr_win_perc = player_dict[player][38] / player_dict[player][37]
        except:
            curr_yr_win_perc = 0
        
        player_dict[player][52] = curr_yr_win_perc

        # Current Year Double Fault %
        try:
            curr_yr_double_fault_perc = player_dict[player][40] / player_dict[player][41]
        except:
            curr_yr_double_fault_perc = 0

        player_dict[player][53] = curr_yr_double_fault_perc

        # Current Year Ace %
        try:
            curr_yr_ace_perc = player_dict[player][39] / player_dict[player][41]
        except:
            curr_yr_ace_perc = 0

        player_dict[player][54] = curr_yr_ace_perc

        # Current Year Break Point Saved %
        try:
            curr_yr_break_pt_svd_perc = player_dict[player][44] / player_dict[player][45]
        except:
            curr_yr_break_pt_svd_perc = 0

        player_dict[player][55] = curr_yr_break_pt_svd_perc

        # Current Year Won against Top 10 %
        try:
            curr_yr_won_top_10_perc = player_dict[player][47] / player_dict[player][46]
        except:
            curr_yr_won_top_10_perc = 0

        player_dict[player][56] = curr_yr_won_top_10_perc
        
        # Current Year Won on Hard Court %
        try:
            curr_yr_won_hard_court_perc = player_dict[player][49] / player_dict[player][48]
        except:
            curr_yr_won_hard_court_perc = 0

        player_dict[player][57] = curr_yr_won_hard_court_perc

        # Current Year Won on Clay Court %
        try:
            curr_yr_won_clay_court_perc = player_dict[player][51] / player_dict[player][50]
        except:
            curr_yr_won_clay_court_perc = 0

        player_dict[player][58] = curr_yr_won_clay_court_perc

        # Current Year Ace Against %
        try:
            curr_yr_ace_against_perc = player_dict[player][59] / player_dict[player][60]
        except:
            curr_yr_ace_against_perc = 0

        player_dict[player][61] = curr_yr_ace_against_perc

        # Current Year First Serve Points Return Won %
        try:
            curr_yr_first_serve_pts_return_won_perc = player_dict[player][63] / player_dict[player][62]
        except:
            curr_yr_first_serve_pts_return_won_perc = 0

        player_dict[player][64] = curr_yr_first_serve_pts_return_won_perc

        # Current Year Points Won %
        try:
            curr_yr_pts_won_perc = player_dict[player][66] / player_dict[player][65]
        except:
            curr_yr_pts_won_perc = 0

        player_dict[player][67] = curr_yr_pts_won_perc

    print("Stats Analysis Complete")
    return player_dict

def write_csv(player_dict):
    column_headers = ['player_id',
    'Name',
    'Rank',
    'Ranking Points',
    'Career Played',
    'Career Won',
    'Height',
    'Age',
    'Career Aces',
    'Career Double Faults',
    'Career Serve Points',
    'Career First Serve Won',
    'Career Second Serve Won',
    'Career Break Points Saved',
    'Career Break Points Faced',
    'Career Played against Top 10',
    'Career Won against Top 10',
    'Career Played on Hard court',
    'Career Won on Hard Court',
    'Career Played on Clay Court',
    'Career Won on Clay Court',
    'Career Win %',
    'Career Double Fault %',
    'Career Ace %',
    'Career Break Point Saved %',
    'Career Won against Top 10 %',
    'Career Won on Hard Court %',
    'Career Won on Clay Court %',
    'Career Ace Against',
    'Career Serve Points Against',
    'Career Ace Against %',
    'Career First Serve Points Against',
    'Career First Serve Points Return Won',
    'Career First Serve Points Return Won %',
    'Career Points Played',
    'Career Points Won',
    'Career Points Won %',
    'Current Year Played',
    'Current Year Won',
    'Current Year Aces',
    'Current Year Double Faults',
    'Current Year Serve Points',
    'Current Year First Serve Won',
    'Current Year Second Serve Won',
    'Current Year Break Points Saved',
    'Current Year Break Points Faced',
    'Current Year Played against Top 10',
    'Current Year Won against Top 10',
    'Current Year Played on Hard court',
    'Current Year Won on Hard Court',
    'Current Year Played on Clay Court',
    'Current Year Won on Clay Court',
    'Current Year Win %',
    'Current Year Double Fault %',
    'Current Year Ace %',
    'Current Year Break Point Saved %',
    'Current Year Won against Top 10 %',
    'Current Year Won on Hard Court %',
    'Current Year Won on Clay Court %',
    'Current Year Ace Against',
    'Current Year Serve Points Against',
    'Current Year Ace Against %',
    'Current Year First Serve Points Against',
    'Current Year First Serve Points Return Won',
    'Current Year First Serve Points Return Won %',
    'Current Year Points Played',
    'Current Year Points Won',
    'Current Year Points Won %',
    'Win Streak']

    #CSV File Setup
    player_stats = 'player_stats.csv'
    with open(player_stats, "w") as f:
        file_writer = csv.writer(f, delimiter=',', lineterminator='\n')
        file_writer.writerow(column_headers)

        for player in player_dict:
            file_writer.writerow(player_dict[player])
    f.close()
    print("CSV Complete")


if __name__ == "__main__":
    player_dict = read_players('./Match_Data/atp_players.csv')
    player_dict = read_rank('./Match_Data/atp_rankings_current.csv', player_dict)
    i = 1968
    for i in range(1968, 2021):
        year = f'./Match_Data/atp_matches_{i}.csv'
        print(i)
        player_dict = parse_matches(year, player_dict)
        i += 1
    
    player_dict = stats_analysis(player_dict)
    write_csv(player_dict)
    print("Script Complete")