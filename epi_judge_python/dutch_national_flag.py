import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

<<<<<<< HEAD
# Hint: do two passes
def dutch_flag_partition(pivot_index, A):
    # l is smaller index
    # r is larger index
    l, r = 0, len(A)-1
    # smaller ones first
    p = A[pivot_index]
    for i in range(len(A)):
        if(A[i] < p):
            A[l], A[i] = A[i], A[l]
            l += 1
    # then do larger ones
    for i in reversed(range(len(A))):
        if(A[i] < p):
            break
        if(A[i] > p):
            A[r], A[i] = A[i], A[r]
            r -= 1
    return A

# trickier implementation with split between lower, equal, higher
def dutch_flag_partition_optimal(pivot_index, A):
    pass
=======

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    return

>>>>>>> b736406dfb6e8e6be2612e8a57e710baf90a2d3e

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
