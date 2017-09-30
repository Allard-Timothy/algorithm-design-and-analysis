"""
r_select(array A, len(n), order statistic i):
    if n == 1: return A[1]      # base case
    choose pivot p from A       # at random
    partition A around pivot    # [<p   p   >p]
    j = index[p]                # new index of p after partition
    if j == i: return p
    if j > i: return r_select(right part of A, j-1, i)
    if j < i: return r_select(left part of A, n-j, i-j)

Worst case: O(n^2)
"""

from random import randint

def partition(n, start, end):
    """Partition n around pivot.
    n = list to partition
    start = start index
    end = end index
    """
    rand_idx = randint(start, end)
    n[start], n[rand_idx] = n[rand_idx], n[start]
    p = n[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if n[j] < p:
            n[j], n[i] = n[i], n[j]
            i += 1
    n[start], n[i - 1] = n[i - 1], n[start]
    return i-1

def r_select(n, k):
    """Return the kth order statistics in the input list
    n = input array
    k = order statistics k, or kth smallest element in the original list
    """
    k -= 1
    if len(lst) == 1:
        return lst[0]
    p_idx = partition(n, 0, len(n)-1)
    if p_idx == k:
        return n[p_idx]
    elif p_idx > k:
        return r_select(n[:p_idx], k + 1)
    else:
        return r_select(n[(p_idx + 1):], k - p_idx)