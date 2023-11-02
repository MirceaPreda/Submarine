import json
import csv
import glob
from datetime import datetime

#global variables
numberOfFiles = []
dataForTransformation = []
transformationDate = datetime.today().strftime('%Y%m%d%H%M%S')

#prepare the data
def baseData():
    try:
        extractedFiles = glob.glob('./engine/fuel/*.json')
        for file in extractedFiles:
            openFile = open(file)
            loadJSON = json.load(openFile)
            numberOfFiles.append(loadJSON)
            #print(numberOfFiles)
        return numberOfFiles
    except:
        print('Issue loading extracted file')

#transform the data to a CSV
def transformer():
    try:
        for element in numberOfFiles:
                  with open(f'./engine/propeller/baseDataFrom{transformationDate}.csv', 'a+', newline='') as individualFile:
                        dataWriter = csv.writer(individualFile)
                        for index, item in enumerate(element):
                        # headers
                            currentWeatherHeader = item['current_weather']
                        # base data
                            currentLatitude = item['latitude']
                            currentLongitude = item['longitude']
                            currentTemperature = currentWeatherHeader['temperature']
                            currentWindspeed = currentWeatherHeader['windspeed']
                            isItDay = currentWeatherHeader['is_day']

                            dataForTransformation = [currentLatitude, "{:.2f}".format(currentLongitude), currentTemperature, currentWindspeed, isItDay]
                            dataWriter.writerow(dataForTransformation)
    except:
        print('Issue transforming data')

baseData()
transformer()
