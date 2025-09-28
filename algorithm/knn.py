import math

class KNearestNeighborClassified:
    def __init__(self, site):
        self.site = site

    def fit(self, sample, train):

        result = []

        for index, s in enumerate(sample):

            dac = []
            rec = [c for c in s]

            for index, x in enumerate(s):
                if index < len(train):
                    knn = (x - train[index]) ** 2

                    dac.append(knn)

            result.append([math.sqrt(sum(dac)), rec[self.site]])

        return result
    
    def predict(self, sample, train):
        rec = self.fit(sample, train)
        rec.sort()

        res = [c[1] for c in rec[:3]]
        duc = [x for x in res if res.count(x) > 1]

        return duc.pop()
