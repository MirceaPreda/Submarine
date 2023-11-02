import pandas as pd
#import matplotlib.pyplot as plot
import glob



def dataCleaner():

    tableHeaders = ['Latitude', 'Longitude', 'Temperature', 'Windspeed', 'Date', 'Day']
    allFiles = glob.glob('./engine/propeller/*.csv')
    dfs = []
    #try:
    for file in allFiles:
            readFile = pd.read_csv(file, names=tableHeaders)
            #print(readFile.to_string())
            df = pd.DataFrame(data=readFile)
            print(df)
            #dfs.append(readFile)

        #dataframes location
    #except:
    print('Issue cleaning the data')

dataCleaner()