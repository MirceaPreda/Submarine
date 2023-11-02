import pandas as pd
import json
import glob



def dataCleaner():

    tableHeaders = ['Latitude', 'Longitude', 'Temperature', 'Windspeed', 'Day']
    allFiles = glob.glob('./engine/propeller/*.csv')
    dfs = []
    #try:
    for file in allFiles:
            readFile = pd.read_csv(file, names=tableHeaders)
            print(readFile.to_string())

            temp = dfs.append(readFile)
            print(temp)
    #except:
    print('Issue cleaning the data')

dataCleaner()