import requests
import json
from secretKeys import apiSecret

def apiResponse(location):
    apiResponse = requests.get(f"http://api.positionstack.com/v1/forward?access_key={apiSecret}&query={location}")
    #print(apiResponse.status_code)
    return apiResponse.status_code

#apiResponse('Constanta')


def receivedAsRequested(location, regionCode):
    apiResponse = requests.get(f"http://api.positionstack.com/v1/forward?access_key={apiSecret}&query={location}")
    transformToJSON = json.loads(apiResponse.text)
    for locations in transformToJSON['data']:
        region = locations['region_code']
        if regionCode == region:
            return True
        else:
            return False
