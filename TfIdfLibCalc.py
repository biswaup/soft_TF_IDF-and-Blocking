from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class TfIdfLibCalc:
    def CalculateTfIdf(self, data):
        sortedLst = []

        # create a sorted list of all the words
        for value in data:
            for token in value.split():
                sortedLst.append(token)
        sortedLst = list(set(sortedLst))
        sortedLst.sort()

        # calculate tf idf
        vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
        X = vectorizer.fit_transform(data)
        # print(vectorizer.get_feature_names())

        # map sorted list with tf idf matrix
        tfIdfLst = []
        X = X.todense()
        docNo = -1

        for item in X:
            docNo = docNo + 1
            count = -1
            item = np.array(item).flatten()
            for val in item:
                count = count + 1
                if val > 0:
                    tfIdfLst.append((docNo, sortedLst[count], val))

        return tfIdfLst