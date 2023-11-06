import sys
sys.path.append('./')
from engine.fuelTank import extractor, transformer
#import engine.fuelTank as ft
from radar import dataCleaner as dc



def startExtractor():

    try:

        extractor.locationExtractor('Bucharest')
        extractor.dataExtractor()
    except:
        print("Error starting the extractor")

def startTransformer():
    try:
        transformer.baseData()
        transformer.transformer()
    
    except:
        print('Error starting the extractor')
    
def cleanAndDisplayData():
    try:

        dc.dataCleaner()
        dc.forecastCleaner()
    except:
        print('Error starting the cleaner')


startExtractor()
startTransformer()
cleanAndDisplayData()