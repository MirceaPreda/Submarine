*** Settings ***

Library    JSONLibrary
Library    RequestsLibrary
Library    Collections
Library    DateTime
Library    String
Library    ../resources/removeFromString.py

*** Variables ***

## URL information
${baseURL}=    https://api.open-meteo.com/v1/forecast?
${latitude}=    latitude=${lat}
${longitude}=    longitude=${lon}
${currentWeather}=    current_weather=true
${hourly}=    hourly=temperature_2m,relativehumidity_2m,windspeed_10m
${wrongLat}=    latitude=123122
${wrongLon}=    longitude=12322311

@{invalidUrls}=    ${baseURL}${wrongLat}&${longitude}&${currentWeather}&${hourly}    ${baseURL}${latitude}&${wrongLon}&${currentWeather}&${hourly}    ${baseURL}${wrongLat}&${wrongLon}&${currentWeather}&${hourly}


## check values
@{lat}=    52.52    51.5    48.8    38
@{lon}=    13.41    0.1    2.3    116
${currentLatitude}
${currentLongitude}
## local variables
${body}
${convertDataToString}
${getDataFromJSON}
${responseData}

*** Test Cases ***
API returns valid Longitude and Latitude
    [Documentation]    Valid data is returned
    [Tags]    Smoke
    Given a functioning API url
    When valid data is returned
    Then the result is equal on both sides

API returns valid date-time
    [Documentation]    Date time is the same as current date time
    [Tags]    Smoke
    Given a functioning API url
    When time data is returned
    Then the date time is correct
    
API returns error
    [Documentation]    Latitude error is returned
    [Tags]    Smoke
    Given an incorrect URL
    When data is returned
    Then the error flag is set to true


*** Keywords ***

a functioning API url
    #${currentLongitude}=    Get Dictionary Values    ${lon}
    FOR    ${dataInURL}    IN    @{lat}
        ${getCurrentIndex}=    Get Index From List    ${lat}    ${dataInURL}
        ${currentLatitude}=    Get From List    ${lat}    ${getCurrentIndex}
        ${currentLongitude}=    Get From List    ${lon}    ${getCurrentIndex}
        ${body}=    GET    ${baseURL}latitude\=${currentLatitude}&longitude\=${currentLongitude}&${currentWeather}&${hourly}
        ${convertDataToString}=    Convert String To Json    ${body.content}
        Set Suite Variable    ${convertDataToString}
        Set Suite Variable    ${currentLatitude}
        Set Suite Variable    ${currentLongitude}
    END
    [Return]    ${convertDataToString} ${currentLatitude} ${currentLongitude}

valid data is returned
    ${inheritJson}=    Get Variable Value    ${convertDataToString}
    ${getDataFromJSON}=    Get From Dictionary    ${inheritJson}    latitude
    Set Suite Variable    ${getDataFromJSON}
    [Return]    ${getDataFromJSON}

the result is equal on both sides
    ${getValueToCheck}=    Get Variable Value    ${getDataFromJSON}
    ${getCurrentLatitude}=    Get Variable Value    ${currentLatitude}
    ${convertLatitudeToNumber}=    Convert To Number    ${getCurrentLatitude}
    Should Be Equal    ${getValueToCheck}    ${convertLatitudeToNumber}
    

an incorrect URL
    FOR    ${Urls}    IN     @{invalidUrls}
         ${body}=    GET    ${Urls}    expected_status=any
         Log To Console    ${Urls}
         ${responseData}=    Convert String To Json    ${body.content}
         Set Suite Variable    ${responseData}
    END
             [Return]    ${responseData}

data is returned
    ${getData}=    Get Variable Value    ${responseData}
    ${getDataFromJSON}=    Get From Dictionary    ${getData}    error
    Set Suite Variable    ${getDataFromJSON}
    [Return]    ${getDataFromJSON}

the error flag is set to true
    ${errorFlag}=    Get Variable Value    ${getDataFromJSON}
    Should Be True    ${errorFlag}

time data is returned
    ${inheritJson}=    Get Variable Value    ${convertDataToString}
    ${currentWeatherDictionary}=    Get From Dictionary    ${inheritJson}    current_weather
    ${getDataFromJSON}=    Get From Dictionary    ${currentWeatherDictionary}    time
    Set Suite Variable    ${getDataFromJSON}
    [Return]    ${getDataFromJSON}

the date time is correct
    ${getData}=    Get Variable Value    ${getDataFromJSON}
    ${x}=    extractHour    fromString=${getData}
    ${y}=    extractDate    fromString=${getData}
    ${currentDateTime}=    Get Current Date    time_zone=UTC    exclude_millis=true
    ${z}=    removeSeconds    fromString=${currentDateTime}
    Should Be Equal    first=${y} ${x}    second=${z}