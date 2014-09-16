# Research Project: Evaluate the Metatone Gesture Classifier

## Preliminary Approach:

- a performance (20130427) was coded by hand by a researcher at five second intervals with our gesture classes. 
- this classification was interpolated to one second by forward filling.
- the same performance was classified by the RF algorithm in silico on 2014-09-16.
- the accuracy was calculated:  `CORRECT_CLASSIFICATIONS / TOTAL_CLASSIFICATIONS`

Results are as follows:

    Regular Gesture Accuracy:

    Accuracy for performer charles was: 0.448275862069
    Accuracy for performer christina was: 0.658045977011
    Accuracy for performer yvonne was: 0.522030651341
    Accuracy for performer jonathan was: 0.449233716475
    Accuracy over whole classified performance: 0.519396551724

    Gesture Group Accuracy: 

    Accuracy for performer charles was: 0.723180076628
    Accuracy for performer christina was: 0.807471264368
    Accuracy for performer yvonne was: 0.727011494253
    Accuracy for performer jonathan was: 0.620689655172
    Accuracy over whole classified performance: 0.719588122605