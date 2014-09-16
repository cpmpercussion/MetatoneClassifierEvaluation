"""
Calculate Classifier Accuracy given a predicted and coded gesture log.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("\nLoading Gesture files.")

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

gesture_groups = {
    0 : 0,
    1 : 1,
    2 : 1,
    3 : 2,
    4 : 2,
    5 : 3,
    6 : 3,
    7 : 3,
    8 : 4,
    9 : 5}




predictions = pd.read_csv(PREDICTED_GESTURES,index_col="time",parse_dates=True)

targets = pd.read_csv(TARGET_GESTURES,index_col="time",parse_dates=True)
# targets = targets.resample('1s',fill_method='ffill')
targets = targets.resample('1s',fill_method='bfill')

targets = targets.ix[predictions.index]

names = targets.columns

#
# Gesture Accuracy
#
print("\nRegular Gesture Accuracy:\n")

scores = targets.replace([0,1,2,3,4,5,6,7,8,9],0)

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


#
# Gesture Group Accuracy
#
print("\nGesture Group Accuracy: \n")

scores = targets.replace([0,1,2,3,4,5,6,7,8,9],0)

for n in names:
    for i in targets.index:
        if (gesture_groups[targets[n].ix[i]] == gesture_groups[predictions[n].ix[i]]):
            scores[n].ix[i] = 1

for n in names:
    accuracy = 1. * scores[n].sum() / scores[n].count()
    print("Accuracy for performer " + n + " was: " + str(accuracy))

allscores = pd.melt(scores)
accuracy = 1. * allscores['value'].sum() / allscores['value'].count()
print("Accuracy over whole classified performance: " + str(accuracy))


# Some plots:
pd.melt(predictions).hist(range=(-0.5,9.5),bins=10)

## Plot a nice Histogram
gesture_restore = {
    0:'N',
    1:'FT',
    2:'ST',
    3:'FS',
    4:'FSA',
    5:'VSS',
    6:'BS',
    7:'SS',
    8:'C',
    9:'?'}

from ggplot import *
long = pd.melt(predictions)
long.columns = ['name','gesture']
long = long.replace(to_replace = {'gesture':gesture_restore})

p = ggplot(aes(x="factor(gesture)"),data=long)
p+ geom_bar() + labs('gesture','count')

