from Stat_Comparison_betting import read_data, player_compare, match_analysis
from Data_cleaning import cleaning
from MatchScraper import sportsbet_scraper_tennis, close_driver
import pandas as pd
import csv
import datetime
#from TennisDataScraper import scrape_data

if __name__ == "__main__":
    weights_dicts = [{3: 0.19690384820438128, 4: 0.10639827477561731, 5: 0.17559272598681447, 6: 0.17432643498749784, 7: 0.12760200807871439, 8: 0.24910098647513845, 9: 0.10463278786506686, 10: 0.838882573570547, 11: 0.5003750765160171, 12: 0.35302592360168916, 13: 0.6725653490130471, 14: 0.7637904771524071, 15: 0.7049693127141243, 16: 0.6024090154800354, 17: 0.20873738175244727, 18: 0.809086480396399, 19: 0.17311930048894464, 20: 0.33205660827779904, 21: 0.3294414918841816, 22: 0.9939275933685108, 23: 0.9751639210256987, 24: 0.6817478463834473, 25: 0.6432947179512744, 26: 0.18500655470500157, 27: 0.9562028332239938, 28: 0.5153965746279571, 29: 0.3907284665999111, 30: 0.9520759404958941, 31: 0.47586300384549973, 32: 0.9397501682330759, 33: 0.31081766889341067, 34: 0.8950602988332453, 35: 0.3631434398195448, 36: 0.9985135254448796, 37: 0.38137119152356147, 38: 0.6215050169150312, 39: 0.117501118156667, 40: 0.5437555038431205, 41: 0.456252240178879, 42: 0.25959571310385476, 43: 0.16611971575218692, 44: 0.36896114818649317, 45: 0.6345392978861084, 46: 0.9844296672304442, 47: 0.5480330799161377, 48: 0.83961129783806, 49: 0.5527382201971582, 50: 0, 0: 0.1079748514334899, 1: 0.8348302669852998, 2: 0.33403010323360405},
                    {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}]

    player_list = sportsbet_scraper_tennis()
    print(player_list)
    score_diff_hurdle = [5.75, 0]
    for weights_dict in weights_dicts:
        for hurdle in score_diff_hurdle:
            matches_to_bet = []
            for match in player_list:
                try:
                    player_1_score, player_2_score = player_compare(match[0], match[1], 'Clay', 'Outdoor', weights_dict)
                    if abs(player_1_score - player_2_score) > hurdle:
                        if player_1_score > player_2_score:
                            matches_to_bet.append((match, match[0], (player_1_score - player_2_score)))
                        else:
                            matches_to_bet.append((match, match[1], (player_2_score - player_1_score)))
                except:
                    continue
            print(matches_to_bet, hurdle)

    close_driver()