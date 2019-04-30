from test_framework import generic_test


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
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
