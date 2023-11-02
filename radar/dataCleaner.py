import pandas as pd
import json
import glob



def dataCleaner():

    headers = ['Latitude', 'Longitude', 'Temperature', 'Windspeed', 'Day']
    allFiles = glob.glob('./engine/fuel/*.json')
    dfs = []
    #try:
    for file in allFiles:
            readFile = pd.read_json(file, lines=True)
            print(readFile.to_string())

            temp = dfs.append(readFile)
            print(temp)

            completeData = pd.json_normalize(temp)
            print(completeData)
    #except:
    print('Issue cleaning the data')

dataCleaner()