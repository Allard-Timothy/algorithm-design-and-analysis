import os
import sys

#Naive - Brute Force:
#Run-Time: O(n^2) - Quadratic
def naive_inversion(seq):
    inv_count = 0 
    for i in xrange(0, len(seq)):
        for j in xrange(i + 1, len(seq)):
            if seq[i] >= seq[j]:
                inv_count += 1
    return inv_count 

#Can we do better? - yes, via mergesort
#Run-Time: O(n lgn)

file_path = '/users/timallard/git_repo/coursera_design_analysis_algorithms/Week1/Week_1_Algorithms/IntegerArray.txt'

def get_int_array():
    f = open(file_path, 'r')
    int_array = []
    line = f.readline()
    while (line != ''):
        int_array.append(int(line))
        line = f.readline()
    return int_array

inv_count = 0

def mergesort_inversion(seq):
    global inv_count
    mid = len(seq)//2
    lft = seq[:mid]
    rgt = seq[mid:]
    if len(lft) > 1: 
        lft = mergesort_inversion(lft)
    if len(rgt) > 1: 
        rgt = mergesort_inversion(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
            inv_count += len(rgt)
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


seq = get_int_array()
print mergesort_inversion(seq)
print naive_inversion(seq)
print inv_count


#############----------Counting inversions------------###########

#Input: array A containing the numbers 1, 2, 3, .... in some
    #arbitrary order

#Output: number of inversions = number of pairs (i, j) of array indices
    # i < j and A[i] > A[j]
#Example: (1, 3, 5, 2, 4, 6)

#Inversions: ((3, 2), (5, 2), (5, 4))

#Uses: Collaborative filtering
#Notes: Number of possible inversions in any array is n(n-1)/2 (similar to knock-out tournament problem)

##------------------------Pseudocode-------------------##
#c = output(length = n)
#a = 1st sorted array (n/2)
#b = 2nd sorted array (n/2)
#i = 1
#j = 1

"""
for k=1 to n
    if a(i) < b(j)
        c(k) = a(i)
        i++
    else b(j) < a(i)
        c(k) = b(j)
        j++
end 
"""

#Goal: Implement CountSplitInv in linear time => Count will run O(n logn)