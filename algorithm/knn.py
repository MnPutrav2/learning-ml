import math

class KNearestNeighbor:
    def __init__(self, site):
        self.site = site

    def fit(self, sample, train):

        result = []

        for index, s in enumerate(sample):

            dac = []
            rec = []

            for index, x in enumerate(s):
                if index < len(train):
                    knn = (x - train[index]) ** 2

                    dac.append(knn)

            for c in s:
                rec.append(c)

            result.append([math.sqrt(sum(dac)), rec[self.site]])

        return result
    
    def predict(self, sample, train):
        rec = self.fit(sample, train)
        rec.sort()

        res = []

        for c in rec[:3]:
            res.append(c[1])

        duc = [x for x in res if res.count(x) > 1]

        return duc.pop()