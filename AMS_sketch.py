import numpy as np
from collections import Counter
# The data stream will be in range [0, RANGE)
RANGE = 100
# Size of data stream
SIZE_STREAM = 10000
S1 = 100
S2 = 100

# TODO: online update
# TODO: timer

class AMS_offline(object):
    '''
    AMS Sketch for offline learning. We precompute the frequency vector of the data
    stream. Online update is not implemented yet.
    '''

    def __init__(self, stream, s1, s2):
        '''
        Build frequency vector
        :param stream: list of non-negative integer in range(0, RANGE)
        '''
        counter = Counter(stream)
        self.frequency_vector = np.array([counter[i] for i in sorted(list(counter))])

        self.F_1 = np.sum(self.frequency_vector)
        self.s1 = s1
        self.s2 = s2

    def estimate_F2(self):
        '''
        Implement the improved estimation of F2 with matrix multiplication.
        Uniformly random hashing is used in place of the four-independent hashing
        This is not exactly the same as in the original paper, but is the most popular
        way for implementation nowadays
        :return: estimated F_2
        '''
        self.hashing_matrix = np.random.choice(a = [1, -1], size=(self.s1, self.s2, RANGE), replace=True)
        Z = np.matmul(self.hashing_matrix, self.frequency_vector)
        X = np.square(Z)
        Y = np.mean(X, axis=0)
        estimation = np.median(Y)

        return estimation


    def estimate_Fk(self, k):
        '''
        Implement the estimation of Fk
        :return: estimated Fk
        '''
        self.X = np.zeros((self.s1, self.s2))

        prob = self.frequency_vector / self.F_1

        for i in range(self.s1):
            for j in range(self.s2):
                idx = np.random.choice(a=RANGE, size=1, p=prob)[0]
                r = np.random.randint(low=1, high=self.frequency_vector[idx], size=1)[0]
                self.X[i][j] = self.F_1 * (r**k - (r - 1)**k)

        Y = np.mean(self.X, axis=0)
        estimation = np.median(Y)

        return estimation



    def estimate_Fk_vectorized(self, k):
        prob = self.frequency_vector / self.F_1
        idx = np.random.choice(a=RANGE, size=(self.s1, self.s2), p=prob)

        onehot_idx = np.eye(RANGE)[idx]
        freq = np.matmul(onehot_idx, self.frequency_vector)
        offset = np.random.random(size=(self.s1, self.s2))
        r = np.round((freq - 1) * offset) + 1


        X = (np.power(r, k) - np.power(r-1, k)) * self.F_1
        Y = np.mean(X, axis=0)
        estimation = np.median(Y)
        return estimation




