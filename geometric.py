import math


def prob(n, p):
    return p * (1.0 - p) ** (n - 1)


def infoMeasure(n, p):
    return -1.0 * math.log2(prob(n, p))


def sumProb(N, p):
    """
    :param N: max number of symbols
    :param p: probability of "head" event
    :return: Sum probability of symbols from 1 ... N
    """
    return sum([prob(i, p) for i in range(1, N + 1)])


def approxEntropy(N, p):
    """
    :param N: max number of symbols
    :param p: probability of "head" event
    :return: Approximate entropy
    """
    probs = [prob(i, p) for i in range(1, N + 1)]
    return sum([-1.0 * x * math.log2(x) for x in probs])
