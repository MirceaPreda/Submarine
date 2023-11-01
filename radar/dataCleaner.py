import pandas as pd
import json
import glob

allFiles = glob.glob('./submarine/engine/fuel/*.json')
dfs = []

for file in allFiles:
    readFile = pd.read_json(file, lines=True)
    print(readFile.to_string())

    temp = dfs.append(readFile)

completeData = pd.concat(dfs, ignore_index=True)
print(completeData)