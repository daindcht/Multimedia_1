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


def prob(n, p, r):
    return Combination.calc(n - 1, r - 1) * p ** r * (1 - p) ** (n - r)


def infoMeasure(n, p, r):
    return -1.0 * math.log2(prob(n, p, r))


def sumProb(N, p, r):
    """
    :param N: max number of symbols
    :param p: probability of "head" event
    :param r: number of heads to stop
    :return: Sum probability of symbols from r ... N
    """
    return sum([prob(i, p, r) for i in range(r, N + 1)])


def approxEntropy(N, p, r):
    """
    :param N: max number of symbols
    :param p: probability of "head" event
    :param r: number of heads to stop
    :return: Approximate entropy
    """
    probs = [prob(i, p, r) for i in range(r, N + 1)]
    return sum([-1.0 * x * math.log2(x) for x in probs])