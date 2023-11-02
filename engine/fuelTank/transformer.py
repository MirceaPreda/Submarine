import json
import csv
import glob
from datetime import datetime

#global variables and lists
numberOfFiles = []
dataForTransformation = []
transformationDate = datetime.today().strftime('%Y%m%d%H%M%S')

#prepare the data for transformation
def baseData():
    try:
        extractedFiles = glob.glob('./engine/fuel/*.json')
        for file in extractedFiles:
            openFile = open(file)
            loadJSON = json.load(openFile)
            numberOfFiles.append(loadJSON)
        return numberOfFiles
    except:
        print('Issue loading extracted file')

#transform the data to a CSV
def transformer():
    try:
        for element in numberOfFiles:
                  with open(f'./engine/propeller/baseDataFrom{transformationDate}.csv', 'a+', newline='') as individualFile:
                        dataWriter = csv.writer(individualFile)
                        for item in element:
                        # headers
                            currentWeatherHeader = item['current_weather']
                        # base data
                            currentLatitude = item['latitude']
                            currentLongitude = item['longitude']
                            currentTemperature = currentWeatherHeader['temperature']
                            currentWindspeed = currentWeatherHeader['windspeed']
                            timeAtExtraction = currentWeatherHeader['time']
                            isItDay = currentWeatherHeader['is_day']
                            # put all needed items into a list
                            dataForTransformation = [currentLatitude,
                                                    "{:.2f}".format(currentLongitude),
                                                    currentTemperature,
                                                    currentWindspeed,
                                                    timeAtExtraction,
                                                    isItDay]
                            dataWriter.writerow(dataForTransformation)
    except:
        print('Issue transforming data')

baseData()
transformer()
