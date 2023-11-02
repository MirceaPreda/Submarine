import json
import csv
import glob
from datetime import datetime
import pandas as pd

#data = ex.dataExtractor()


# transform existing files to match the needed data
# create new file with the values for dataframes later

def baseData():
    #arrays and variables
    transformationDate = datetime.today().strftime('%Y%m%d%H%M%S')

    dataForTransformation = []
    numberOfFiles = []


    try:
        extractedFiles = glob.glob('./engine/fuel/*.json')
        for file in extractedFiles:
            openFile = open(file)
            loadJSON = json.load(openFile)
            numberOfFiles.append(loadJSON)
            for elementIndex, element in enumerate(loadJSON):
                  with open(f'./engine/propeller/baseDataFrom{transformationDate}.csv', 'a', newline='') as individualFile:
                        dataWriter = csv.writer(individualFile)
                        # headers
                        currentWeatherHeader = element['current_weather']
                        # base data
                        currentLatitude = element['latitude']
                        currentLongitude = element['longitude']
                        currentTemperature = currentWeatherHeader['temperature']
                        currentWindspeed = currentWeatherHeader['windspeed']
                        isItDay = currentWeatherHeader['is_day']

                        dataForTransformation.append([currentLatitude, currentLongitude, currentTemperature, currentWindspeed, isItDay])
                        dataWriter.writerow(dataForTransformation[elementIndex])
                        # BUG comes from index of elementIndex -> does not pass all the items
                        print(dataForTransformation[elementIndex])
    except:
        print("Issue opening the file for transformation or with the transformation")

baseData()
