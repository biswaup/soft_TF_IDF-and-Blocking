import Levenshtein as lev

class SoftTfIdfCalculator:

    """calculate token to token scores between 2 strings"""
    def CalcLevenshtein(self, string1, string2, doc1, doc2, tfIdfLst):
        distList = []
        tok1 = ''
        tok2 = ''

        for token in string1.split():
            if token.strip():
                nMax = 0
                for tok in string2.split():
                    if tok.strip():
                        d = lev.distance(token, tok)

                        if d == 0:
                            d = 1
                        elif d >= 0.4 * (max(len(token), len(tok))):
                            d = 0
                        else:
                            d = 1 - (d / max(len(token),len(tok)))

                        if d > nMax:
                            nMax = d
                            tok1 = token
                            tok2 = tok
            if nMax > 0:
                distList.append((tok1, tok2, nMax))

        # calculate the final score
        score = self.CalFinScore(distList, tfIdfLst, doc1, doc2)
        return score


    """calculate the final score between 2 strings"""
    def CalFinScore(self, dLst, tfIdfLst, doc1, doc2):
        score = 0

        if len(dLst) > 0:
            for d in dLst:
                tf1 = 0
                tf2 = 0

                for tfIdf in tfIdfLst:
                    if doc1 == tfIdf[0] and tfIdf[1] == d[0]:
                        tf1 = tfIdf[2]

                for tfIdf in tfIdfLst:
                    if doc2 == tfIdf[0] and tfIdf[1] == d[1]:
                        tf2 = tfIdf[2]

                score = score + (tf1 * tf2 * d[2])
        else:
            score = 0

        return score
