import requests
import json
from datetime import datetime
from pathlib import Path


def dataExtractor():
    latitude = [52.52, 51.5, 48.8, 38]
    longitude = [13.41, 0.1, 2.3, 116]

    completeFile = []
    currentDate = datetime.today()
    filtererdDate = currentDate.strftime("%Y%m%d%H%M%S")


    for index, element in enumerate(latitude):
        try:
            # cycle through links and extract them
            baseURL = f"https://api.open-meteo.com/v1/forecast?latitude={element}&longitude={longitude[index]}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
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

dataExtractor()