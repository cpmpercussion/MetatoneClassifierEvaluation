"""
Calculate Classifier Accuracy given a predicted and coded gesture log.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading Gesture files and calculating accuracy.")

TARGET_GESTURES = "./data/20130427/20130427-17h46m19s-MicaiahCoded.csv"
PREDICTED_GESTURES = "./data/20130427/2013-04-27T17-46-19-MetatonePostHoc-gestures.csv"

## Int values for Gesture codes.
gesture_codes = {
    'N': 0,
    'FT': 1,
    'ST': 2,
    'FS': 3,
    'FSA': 4,
    'VSS': 5,
    'BS': 6,
    'SS': 7,
    'C': 8,
    '?': 9}

predictions = pd.read_csv(PREDICTED_GESTURES,index_col="time",parse_dates=True)

targets = pd.read_csv(TARGET_GESTURES,index_col="time",parse_dates=True)
targets = targets.resample('1s',fill_method='ffill')
targets = targets.ix[predictions.index]

scores = targets.replace([0,1,2,3,4,5,6,7,8,9],0)
names = targets.columns

for n in names:
	for i in targets.index:
		if (targets[n].ix[i] == predictions[n].ix[i]):
			scores[n].ix[i] = 1


for n in names:
	accuracy = 1. * scores[n].sum() / scores[n].count()
	print("Accuracy for performer " + n + " was: " + str(accuracy))

allscores = pd.melt(scores)
accuracy = 1. * allscores['value'].sum() / allscores['value'].count()
print("Accuracy over whole classified performance: " + str(accuracy))

