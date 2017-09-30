
"""Coursera Algorithms Weeks 1"""

def mergesort(seq):
    #find the middle point for division
    mid = len(seq)//2
    #assign the left and right hand halves
    lft, rgt = seq[:mid], seq[mid:]
    #recursively halve the sequence space
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    #neither half is empty
    while lft and rgt:
        #left side has greater last value
        if lft[-1] >= rgt[-1]:
            #append it
            res.append(lft.pop())
        #right side has greater last value    
        else:
            #append it
            res.append(rgt.pop())
    #result is backwards
    res.reverse()
    #don't forget the remainder
    return (lft or rgt) + res 

l = [5,8,2,4,0,2,4,67,3,10,99]
print mergesort(l)

#################-Merge sort analysis-#################
#Pseudocode
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

#upshot: run-time of merge on array of m numbers: <= 4m + 2 or <= 6m (since m >= 1)

#recall/GTK: log2n = # of times you divide n by 2 until you reach 1 ie. 5 = log2(32)
#claim: mergesort requires <= (6n * log2n) + 6n operations for n numbers or O(n * logn)
    # - insertion sort: O(m * n^2) where m = constant
    # - bubble sort: O(m * n^2) where m = constant

#recusive tree
    # - level 0: outer call to merge_sort
"""                           n    (entire input)
                            /   \
                           /     \
    # - level 1:         left  right
                          /\     /\    
                         /  \   /  \
    # - level 3:       l1   l2  r1  r2
                      / \   /\  /\   /\
                     /   \ /  \/  \ /  \
                    .    . .  ..  . .   .
                    .    . .  ..  . .   .
                    .    . .  ..  . .   .
"""
    # number of levels as f(n): log2n
    # number of sub-problems and size of input for given level j: 2^j, n/2^j
    # total number of operatings at level j:

"""         <=: 2^j * 6(n/j^2) = 6n (independent of level j)
               /        \
            # of      sub-prob
          level j     size at 
         sub-probs    level j * work per sub-prob

        total:
        <= 6n(log2n + 1)
           /        \
          /          \
        work        # of levels
        per
       level
 

"""