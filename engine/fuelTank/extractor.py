import requests
import json
from datetime import datetime
from pathlib import Path
import secretKeys

#global lists
latitudeList = []
longitudeList = []


def locationExtractor(location):

    try:
        locationAPI = f"http://api.positionstack.com/v1/forward?access_key={secretKeys.apiSecret}&query={location}"
        retrieveData = requests.get(locationAPI).text
        convertToJSON = json.loads(retrieveData)
        basePath = convertToJSON['data'][0]
        latitude = basePath['latitude']
        longitude = basePath['longitude']
        latitudeList.append(latitude)
        longitudeList.append(longitude)
    except:
        print('Issue finding the location or data is inaccessible')

def dataExtractor():

    completeFile = []
    currentDate = datetime.today()
    filtererdDate = currentDate.strftime("%Y%m%d%H%M%S")


    for index, element in enumerate(latitudeList):
        try:
            # cycle through links and extract them
            baseURL = f"https://api.open-meteo.com/v1/forecast?latitude={element}&longitude={longitudeList[index]}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
            retrieveData = requests.get(baseURL).text
            convertData = json.loads(retrieveData)
            # push data to an array containing all data for the run
            completeFile.append(convertData)
        except:
            print('Issue getting and extracting the file or elements of it')

    try:
        # create a file with the results
        with open(f"./engine/fuel/{filtererdDate}.json", "w+") as file:
            json.dump(completeFile, file)
    except:
        print('Issue saving the file')


locationExtractor('Constanta')
dataExtractor()

