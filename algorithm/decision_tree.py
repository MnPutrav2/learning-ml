import math

class DecisionTree:
    def __init__(self, s, n, column=[]):
        self.s = s
        self.n = n
        self.column = column

    def before(self, sample, nod):

        samp = []

        for c in nod:
            sal = c / sample
            samp.append(sal * math.log2(sal))

        result = 0

        if sum(samp) < 0:
            result = abs(sum(samp))

        return result

    def entropy(self, x1):

        entropy = 0
        dataSum = sum(x1)

        for c in x1:
            if c > 0:
                p = c / dataSum
                entropy -= p * math.log2(p)

        return entropy

    def gain(self, x2):

        gain = []
        all = []
        ax = []

        for c in x2:
            gain.append(self.entropy(c))
            ax.append(sum(c))

            for x in c:
                all.append(x)

        result = []
        sam = self.before(self.s, self.n)

        for index, v in enumerate(gain):
            result.append((ax[index] / sum(all) * v))

        return abs(sam - sum(result))
    
    def train(self, x3):
        
        g = []

        for c in x3:
            g.append(self.gain(c))

        return g