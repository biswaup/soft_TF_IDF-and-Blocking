import pandas as pd
import re
import string
import SoftScoreCalculator as calc
import Blocking as bloc
import TfIdfLibCalc as tfIdfLib


class Dataset():
    def __init__(self, data_file):
        self.data = (pd.read_csv(data_file)).values.tolist()


class DataPreProcess:
    """
    deletes extra whitespaces and prefixes,
    deletes punctuations except - which is replaced by space
    """
    def Preprocess(self, data):
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        newData = []
        for line in data:
            s = line[0].replace('-',' ')
            s = s.replace("’", ' ')
            s = regex.sub (' ', s)
            s = " ".join(s.split())
            s = self.DeletePrefix(s.lower())
            newData.append(s)

        return list(set(newData))

    """
    deletes prefixes in names
    """
    def DeletePrefix(self, s):
        prefix = ('mr', 'mrs', 'miss', 'ms', 'dr', 'professor', 'sr', 'jr')
        new_s = ' '.join([wrd for wrd in s.split() if wrd not in prefix])
        return new_s


if __name__ == '__main__':
    do_blocking = True
    scoreLst = []

    datast = Dataset('D:/Upasana/Internship/ZyLAB/SVM_Data/Test2ForSVM.csv')
    dataPro = DataPreProcess().Preprocess(datast.data)

    # calculate tf idf
    tfIdfNorm = tfIdfLib.TfIdfLibCalc().CalculateTfIdf(dataPro)


    # calculate soft tf idf WITH BLOCKING
    if do_blocking:
        hashTab = bloc.Blocking().CreateHashTable(dataPro)
        print('--------- printing hash table -------')
        print(hashTab)

        for key, value in hashTab.items():
            # create the combinations of keys possible for each key
            setOfKeys = bloc.Blocking().FindKeys(key)

            # compare within your own block if block size is > 1
            if len(value) > 1:
                for i in range(0, len(value) - 1):
                    for j in range(i + 1, len(value)):
                        val1 = value[i].split(',')[0]
                        val2 = value[j].split(',')[0]
                        doc1 = value[i].split(',')[-1]
                        doc2 = value[j].split(',')[-1]
                        if len(val1.split()) == 1 and len(val2.split()) == 1:
                            continue
                        else:
                            score = calc.SoftTfIdfCalculator().CalcLevenshtein(val1, val2, int(doc1), int(doc2), tfIdfNorm)
                            if score >= 0.3:
                                scoreLst.append((val1, val2, score))

            # loop through keys combinations, find blocks and compare
            for key in setOfKeys:
                val_from_diff_block = hashTab.get(key, None)
                if val_from_diff_block is not None:
                    for m in range(0, len(value)):
                        for n in range(0, len(val_from_diff_block)):
                            val1 = value[m].split(',')[0]
                            val2 = val_from_diff_block[n].split(',')[0]
                            doc1 = value[m].split(',')[-1]
                            doc2 = val_from_diff_block[n].split(',')[-1]

                            if len(val1.split()) == 1 and len(val2.split()) == 1:
                                continue
                            else:
                                score = calc.SoftTfIdfCalculator().CalcLevenshtein(val1, val2, int(doc1), int(doc2),
                                                                                   tfIdfNorm)
                                if score >= 0.3:
                                    scoreLst.append((val1, val2, score))


    # calculate soft tf idf WITHOUT BLOCKING
    else:
        for i in range(0, len(dataPro) - 1):
            for j in range(i + 1, len(dataPro)):
                if len(dataPro[i].split()) == 1 and len(dataPro[j].split()) == 1:
                    continue
                else:
                    score = calc.SoftTfIdfCalculator().CalcLevenshtein(dataPro[i], dataPro[j], i, j, tfIdfNorm)
                    if score >= 0.3:
                        scoreLst.append((dataPro[i], dataPro[j], score))


