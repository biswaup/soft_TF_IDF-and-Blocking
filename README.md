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

# Results
Soft TF-IDF works fairly well in not too big datasets and better for the balanced one. The overall precision calculated varies from 0.80 to
0.90 based on dataset type, distribution of names and variations in names. Since, it is hard to calculate performance metrics accurately for unlabelled data, it has been further applied on the constructed labelled personal names datasets. For the class-imbalanced
dataset, the average precision is 0.78 and for the class-balanced one, it is 0.91.
For Blocking, implementation of blocking before comparison resulted in execution time as well as precision gain in the performance. Due to the avoidance of unwanted comparisons, huge improvement in execution time has been observed for person names. The below graph shows the change in execution time, with and without blocking, for datasets of three different sizes.
![graph_Blocking](https://github.com/biswaup/soft_TF_IDF-and-Blocking/blob/master/plot1.PNG)

