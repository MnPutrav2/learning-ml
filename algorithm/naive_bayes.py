class NaiveBayes:
    def __init__(self, site):
        self.site = site

    def mean(self, data):

        sample = []
        res = {}

        for c in data:

            sample.append(c[self.site])

        for s in sample:
            if s in res:
                res[s] += 1
            else:
                res[s] = 1

        return res

    def orion(self, data):

        rec = []
        sample = self.mean(data)

        for c in data:

            b = []
            res = {}

            for d in c:
                b.append(c[d])

            for s in b:
                if s in res and sample[1]:
                    res[s] += 1
                else:
                    res[s] = 1

            rec.append(res)
            

        # for s in rec:
        #     if s in res:
        #         res[s] += 1
        #     else:
        #         res[s] = 1

        return rec



data_sample = [
  [0, 0, 0, 0],
  [0, 0, 1, 0],
  [1, 0, 0, 1],
  [2, 0, 0, 1],
  [2, 1, 0, 1],
  [2, 1, 1, 0],
  [1, 1, 1, 1],
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [2, 1, 0, 1],
  [0, 1, 1, 1],
  [1, 0, 1, 1],
  [1, 1, 0, 1],
  [2, 0, 1, 0]
]

nb = NaiveBayes(site=3)

print(nb.orion(data_sample))