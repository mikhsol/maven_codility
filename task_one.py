"""
Solution for the problem of finding the number of fragments of integer array
sum of which equal zero.
"""

MIN_SIZE = 0
MAX_SIZE = 100_000
MIN_EL = -10_000
MAX_EL = 10_000


def solution(a):
    """
    Return number of fragments in array `a` sum of which equal to zero.

    :param a: list of integers
    :return: cnt: integer
    """
    N = len(a)
    if N <= MIN_SIZE or N > MAX_SIZE or (N == MAX_SIZE and not all(a)):
        return -1
    sum = 0
    sums_of_fragments = dict()
    fragments = []
    for i in range(N):
        if a[i] > MAX_EL or a[i] < MIN_EL:
                return -1
        sum += a[i]
        if sum == 0:
            fragments.append((0, i))

        if sum in sums_of_fragments.keys():
            started_indexes = sums_of_fragments[sum]
            for el in started_indexes:
                fragments.append((el, i))
            sums_of_fragments[sum].append(i)
            continue

        sums_of_fragments[sum] = [i]

    return len(fragments)
