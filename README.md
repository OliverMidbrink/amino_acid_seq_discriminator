# Overview
The software will essentially measure the distance between two datasets. Smaller values mean a smaller distance. The distance does not start from 0 and grow, since there is a "Limit of detection". But the bigger the number, the more different the sets are. 

# Preparation
1. Put a list of sequences in seq_1 (max seq length is 100)
2. Put another list of sequences in seq_2, line separated (also max 100 length)
3. They should be line separated. Try to keep the same number of lines for best comparison, for example by doing subsets of the longer one if they have unequal length. 

# Setting parameters (basically naming the experiment)
4. Edit disc.py and set the name parameter. 
5. Run python disc.py, the program will output final scores.

# Note
You can run multiple experiments on the same datasets for a higher sample size and easier statistical significanse