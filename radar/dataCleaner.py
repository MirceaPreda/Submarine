import pandas as pd

newDataSet = {
    'weather':  ["sunny", "overcast", "raining"],
    'temperature':  [30, 23, 10]
}

showData = pd.DataFrame(newDataSet)

print(showData.loc[[0,2]])



secondDataSet = ['string', 21, 3]

showSecondSet = pd.Series(secondDataSet)
print(showSecondSet)


rcsv = pd.read_csv('C:\Users\mphq\OneDrive\Desktop\stuff\submarine\engine\geo.csv')
print(rcsv)