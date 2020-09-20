import math


class Combination:
    """
    class to calculate combination and store it by Dynamic Programing
    """

    comb = {}

    @classmethod
    def calc(cls, n, k):
        if k == n or k == 0:
            return 1
        if (n, k) in cls.comb.keys():
            return cls.comb[(n, k)]
        result = cls.calc(n - 1, k - 1) + cls.calc(n - 1, k)
        cls.comb[(n, k)] = result
        return result


def prob(n, p, N):
    return Combination.calc(N, n) * p ** n * (1 - p) ** (N - n)


def infoMeasure(n, p, N):
    return -1.0 * math.log2(prob(n, p, N))


def sumProb(N, p):
    """
    :param N: max of bernoulli trials
    :param p: probability of "head" event
    :return: Sum probability of symbols from 0 ... N
    """
    return sum([prob(i, p, N) for i in range(0, N + 1)])


def approxEntropy(N, p):
    """
    :param N: max of bernoulli trials
    :param p: probability of "head" event
    :return: Approximate entropy
    """
    probs = [prob(i, p, N) for i in range(N + 1)]
    return sum([-1.0 * x * math.log2(x) for x in probs])
