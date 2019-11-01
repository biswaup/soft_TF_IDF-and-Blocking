# soft_TF_IDF-and-Blocking
This project implements soft TF-IDF algorithm with and without blocking approach, which was mainly used to reduce the execution time. The dataset used is personal names, which has been constructed and labelled from DbPedia.

DataLoadProcess.py is the file with the _main_ function which loads and preprocesses the data
TfIdfLibCalc.py computes tf-idf for the list of personal names as strings
SoftScoreCalculator.py calculates soft tf-idf score
Blocking.py implements the blocking approach

# Idea of implementation
The input is a list of strings or personal names. Each string is compared with every other string in the list and a score is computed. TF-IDF values are calculated for all of the strings. And finally, using the tf-idf values, soft tf-idf scores are computed for every pair. For the soft part of the algorithm, Levenshtein has been used. The cut-off scores can be tuned as required

# Blocking approach
Comparing one string with every other is very computation intensive, which is why blocking approach has been implemented. The idea behind the approach is that for each name, a key is generated. Based on the keys, the names are divided into separate blocks. Now, a subset of possible combinations from each key is generated. Only those blocks are compared, who share a similar combination in their subsets. It can be illustrated with the following picture:
![Image_Blocking](https://github.com/biswaup/soft_TF_IDF-and-Blocking/blob/master/Blocking.PNG)

