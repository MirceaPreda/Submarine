import re

#functionality
def extractHour(fromString):
    regexReplace= re.sub('.+\-\d+', '', fromString)
    timeOnly= regexReplace.replace('T', '')
    return timeOnly
    
def extractDate(fromString):
    regexReplace= re.sub('T.*', '', fromString)
    return regexReplace

def removeSeconds(fromString):
    regexReplace= re.sub(':[^:]*$', '', fromString)
    return regexReplace