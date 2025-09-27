class NaiveBayes:
    def __init__(self, site):
        self.site = site

    def mean(self, data):

        sample = [c[self.site] for c in data]
        res = {}

        for s in sample:
            if s in res:
                res[s] += 1
            else:
                res[s] = 1

        return res

    def orion(self, data):

        rec = []
        reg = [x for x in data[0]]
        
        for index, x in enumerate(reg):
           
           num = [d[index] for d in data]
           let = [n for n in num]
              
           rec.append(let)
           
        x = rec[3]
        f = rec[0]
        y = rec[self.site]
        
        res = []
        
        for index, b in enumerate(x):
           if f[index] == 1 and b == 1:
              res.append(1)
           else:
              res.append(0)

        return sum(res)



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
