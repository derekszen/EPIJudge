from typing import List

from test_framework import generic_test
import bisect

<<<<<<< HEAD
def search_first_of_k(A, k):
    l, m, r, result = 0, len(A)//2 ,len(A)-1, -1
    while(l <= r): 
        m = (l + r)//2
        if A[m] > k:
            r = m - 1
        elif A[m] == k: 
            result = m
            r = m - 1
        else: #A[m] < k
            l = m + 1
    return result
=======
def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> b736406dfb6e8e6be2612e8a57e710baf90a2d3e


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
