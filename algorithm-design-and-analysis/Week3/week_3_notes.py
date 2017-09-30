###---------------Week 3 Notes-----------------------###
##--Day 1--##
#
# The Selection Problem:
#
# Input: Array A with n distict numbers
#
# Output: ith order statistic ie. ith smalled element of input array
#   [10,8,2,4]
#        \
#        3rd order statistic
# Middle element == median
#    i = (n+1)/2 if n odd
#    i = n/2 if n even
#
# Concept: Reduction to Sorting - 
#
# O(nlogn) algorithm:
#  1: apply mergesort
#  2: return ith element of sorted array 
#
# Fact: can't sort any faster than O(nlogn)
# 
#
# Problem: 5th order statistic in input array of len = 10,
#    partitioned array leaves pivot in 3rd spot. On which side
#    of pivot do we recurse and what order statistic should we 
#    look for?
#
# Solution: 2nd order statistic of right side;
#  the pivot in 3rd position == 3rd order statistic;
#  2nd order statistic of right side == 5th order overall.
#
#
########------Randomized Selection---------###########
#
# r_select(array A, len(n), order statistic i):
#      if n == 1: return A[1]      # base case
#      choose pivot p from A       # at random
#      partition A around pivot    # [<p   p   >p]
#      j = index[p]                # new index of p after partition
#      if j == i: return p
#      if j > i: return r_select(right part of A, j-1, i)
#      if j < i: return r_select(left part of A, n-j, i-j)
#
####--------Analysis-----------#####
#
#Claim: r_select is correct (guaranteed to output ith order statistic)
#Proof: by induction
#Running time: depends on quality of chosen pivots
#
#
####-----Day 2-----####
#
#Upshot: Running time depends on how good pivot is, could be as bad as O(n^2)
#    
#Key: Best pivot = pivot giving "balanced" split, this is median
# 
#choosing median =>> T(n) <= T(n/2) + O(n) =>> T(n) = O(n) 
#Master Method: a = 1; b = 2; d = 1 =>> a < b^d; 1 < 2^1                                         
#
##------Proof------##
#Proof 1: Tracking Progress via Phases
#Note: Workhorse is partition sub-routine - uses <= Cn operations outside recurisve call
#        (for some constant C > 0)
#Progress Notation:
#  - phase-j; quantifies how much progress made thus far; higher order == more progress
#  - mid-point of execution: length of array recursive call is working is between (3/4)^j+1n and (3/4)^jn
#  - Xj: counts number of recursive calls during phase j
#Note: running time of r_select <= sum(phase(j) * Xj) * C * (3/4)^jn
#                                                 /     |         \    
#                                            # of       |          \  upper bound      
#                                        phase j        |           |on array during phase j            
#                                        sub-problems   |___________|          
#                                                              \         
#                                                           work per phase j         
#                                                              sub-problem
#Proof 2: Reduction to Coin Flipping   
#Xj = Recursive calls during phase j-- (3/4)^j+1n <= size <= (3/4)^jn 
#
#Note: if r_select chooses pivot giving 25%/75% split or better;
#      then current phase must end. This means new sub-array is at 
#      most 75% of old length 
#
#Recall: probability of 25%/75% split is 50%
#
#So: E[Xj] <= expected number of times you need to flip fair coin till it lands on heads
#
###---------Day 3--------------###
#
#Proof 3: Coin Flipping Analysis
#
#Let n = number of coin flips until you get heads
#    (a "geometric random variable")
#
#Note: E[n] = 1 + 1/2*E[n]
#            /     |     \
#          1st    Prob.   # of further coin glips needed in this case 
#         flip    tails
#
#Solution: E[n] = 2
#
#Expected running Time: <= Cn*(sum(phase(j)*(3/4)^jXj)) = Cn*(sum(phase(j) * (3/4)^jE[Xj]))
#                           
#E[Xj] <= E(# of coin flips) = 2
# 
###---Deterministic Choose Pivot---###
#  **--Two Round Knockout Tournament--**
#
# ChoosePivot(A,n)
#     -logically break A into n/5 groups of size 5 each
#     -sort each group (use mergesort)
#     -copy n/5 medians (middle element of each sorted group)
#         into new array C
#     -recursively compute median of C 
#     -return this as pivot
#     
# Dselect(A, len n, order i)
#      break A into 5 groups, sort each group(mergesort)
#      C = n/5 "middle elements"
#      p = Dselect(C, n/5, n/10)  (recurisvely compute median of C)
#      Partition A around p
#      if j = i: return p
#      if j < i: Dselect(1st part of A, j-1, i)
#      elif j > i: return Dselect(2nd pair of A, n-j, i-j)
#
#
#



















