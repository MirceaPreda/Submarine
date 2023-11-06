import pandas as pd
import matplotlib.pyplot as plot
import glob



def dataCleaner():

    tableHeaders = ['Latitude', 'Longitude', 'Temperature', 'Windspeed', 'Date', 'Day']
    allFiles = glob.glob('./engine/propeller/baseDataFrom*.csv')
    try:
        for file in allFiles:
            readFile = pd.read_csv(file, names=tableHeaders, parse_dates=True)
            df = pd.DataFrame(data=readFile)
            df.plot.scatter(x="Date", y="Temperature")
            plot.show()
    except:
        print('Issue cleaning the data')

def forecastCleaner():
    tableHeaders = ['Time', 'Temperature', 'Humidity', 'Windspeed']
    forecastFiles = glob.glob('./engine/propeller/futureDates*.csv')
    
    try:
        for file in forecastFiles:
            readForecast = pd.read_csv(file, names=tableHeaders, parse_dates=True)
            df = pd.DataFrame(data=readForecast)
            df.plot.scatter(x="Time", y="Temperature")

    except:
        print('Cannot plot the forecast')
