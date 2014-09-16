# Research Project: Evaluate the Metatone Gesture Classifier

## Preliminary Approach:

- a performance (20130427) was coded by hand by a researcher at five second intervals with our gesture classes. 
- this classification was interpolated to one second by forward filling.
- the same performance was classified by the RF algorithm in silico on 2014-09-16.
- the accuracy was calculated:  `CORRECT_CLASSIFICATIONS / TOTAL_CLASSIFICATIONS`

Results are as follows:

    Regular Gesture Accuracy:

    Accuracy for performer charles was: 0.448275862069
    Accuracy for performer christina was: 0.578544061303
    Accuracy for performer yvonne was: 0.466475095785
    Accuracy for performer jonathan was: 0.521072796935
    Accuracy over whole classified performance: 0.503591954023

    Gesture Group Accuracy: 

    Accuracy for performer charles was: 0.726053639847
    Accuracy for performer christina was: 0.735632183908
    Accuracy for performer yvonne was: 0.661877394636
    Accuracy for performer jonathan was: 0.719348659004
    Accuracy over whole classified performance: 0.710727969349

