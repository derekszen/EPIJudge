from typing import Optional

from list_node import ListNode
from test_framework import generic_test


<<<<<<< HEAD
def merge_two_sorted_lists(L1, L2):
    if(L1 is None):
        return L2
    if(L2 is None):
        return L1
    # merge into L1
    if L1.data < L2.data:
        L1.next = merge_two_sorted_lists(L1.next, L2)
        return L1
    else:
        L2.next = merge_two_sorted_lists(L1, L2.next)
        return L2
    return L1
=======
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None
>>>>>>> b736406dfb6e8e6be2612e8a57e710baf90a2d3e

#doubly linked
def merge_two_sorted_lists_doubly_linked(L1, L2):
    if(L1 is None):
        return L2
    if(L2 is None):
        return L1
    # merge into L1
    if L1.data < L2.data:
        L1.next = merge_two_sorted_lists(L1.next, L2)
        return L1
    else:
        L2.next = merge_two_sorted_lists(L1, L2.next)
        return L2
    return L1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
