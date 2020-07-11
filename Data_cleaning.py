import csv
import pandas as pd
import math

def cleaning(*args):
    for record in args:
        data = pd.read_csv(record, encoding='utf-8')

        for index, row in data[1:].iterrows():
            if row.loc["Comment"] == "Completed":
                continue
            else:
                data = data.drop(index, axis=0)
        
        ######################################
        #for index, row in data[1:].iterrows():
        #    for column in row:
        #        if pd.isna(column) is True:
        #            data = data.drop(index, axis=0)
        #            print("Null Dropped")
        #            break
        ######################################
        data = data.drop(columns=["ATP", "Location", "Tournament", "Date", "Series", "W1", "L1",
                            "W2", "L2", "W3", "L3", "W4", "L4", "W5", "L5", "Wsets", "Lsets", "Comment"])
        data = data.drop(0, axis=0)
        print(data.shape)
        print(data.dtypes)
        data.to_csv(record)
        print("Data exported")

