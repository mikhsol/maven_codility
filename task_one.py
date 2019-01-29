"""
Solution for the problem of finding the number of fragments of integer array
sum of which equal zero.
"""


MIN_SIZE = 0
MAX_SIZE = 100_000
MIN_EL = -10_000
MAX_EL = 10_000


def solution(a):
    N = len(a)
    if N <= MIN_SIZE or N > MAX_SIZE or (N == MAX_SIZE and not all(a)):
        return -1
    cnt = 0
    prev_sum = 0
    fragments = []
    for q in range(N):
        for p in range(q+1):
            if a[p] > MAX_EL or a[p] < MIN_EL:
                return -1
            if a[p] + a[q] == 0 or sum(a[p:q+1]) == 0:
                cnt += 1
                prev_sum = 0
                if len(fragments) > 0 and fragments[-1][1] + 1 == p:
                    cnt += 1
                fragments.append((p, q))
            else:
                prev_sum += a[p]
    return cnt