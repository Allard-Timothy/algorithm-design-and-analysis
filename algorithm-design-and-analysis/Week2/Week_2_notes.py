#################--------------Week 2 Notes----------------###########################

#---------------------------------------Day 1-----------------------------------------------#

######-------Recurrence Relations------########

#Example 1: Integer Multiplication 

#T(n) = maximum number of operations this algorithm needs to multiply two n- digit numbers
#Recurrence: express T(n) n terms of running time if recursive calls
#Base Case: T(1) <= a constant 
#Express in formula consisting of two parts - 1: Work done in recursive calls
#                                             2: Work done outside of recursive calls
#
#For all n > 1: T(n) <= 4T(n/2) + O(n)
#                        /         \
#                       /           \
#                   Work done by    Work done outside of recursive call
#                   recursive call
#
#
########--------Better Recursive Algorithm for integer multiplication---------###########
#Algorithm #2 (Gauss): recursively compute - ac, bd, (a+b)(c+d); or three products instead of 4

#New Recurrence for multiplication:

#Base Case: T(1) <= a constant
#Recurrence: For all n > 1: T(n) <= 3T(n/2) + O(n)
#                                    /          \
#                                   /            \
#                               Work done by    Work done outside of recursive call
#                               recursive call
#
#
#Bullet Point: Recurrence relations: specifically breaking them down into two parts;
#               the first being the base case == no more recursion to be done.
#               The second being the recurrence expressed in formula of work done by 
#               recursive calls and then work done outside of recursive call.


######---------Master Method------########

#Cool Feature: a 'black box' for solving recurrences
#Assumption: All sub-problems have equal size
#           eg. mergesort has two recursive calls on half the array
#           eg. integer multiplication on all sub-problems of n/2 digits
#           eg. Will not apply: recursive calls on 1/3 of n and then 2/3 of n 
#
#Base case: T(n) <= a constanct for all sufficiently small n
#For all larger n: T(n) <= aT(n/b)m + O(n^d)
# where: a = number of recursive calls   (>= 1)
#        b = input size of shrinking factor  (> 1)
#        d = exponent in running time of 'combine' step   (>= 0)
#        [a,b,d indendepent of n]
#
#####--Three cases for master theorem--#####
#T(n) = {O(n^d logn)} - if a = b^d
#       {O(n^d)} - if a < b^d
#       {O(n^logb^a)} - if a > b^d
#
#Note: Case 1: Base of log doesn't matter as it only changes leading constant
#      Case 3: Base matters!
#
#Final Statement: If T(n) <= aT(n/b) + O(n^d)
#                 then
#                 T(n) = {O(n^d logn)} - if a = b^d - Case 1
#                        {O(n^d)} - if a < b^d - Case 2
#                        {O(n^logb^a)} - if a > b^d - Case 3
#
#
#Bullet Point: Master Theorem applies to all divide and conqeur recurrences where sub-problems are equal size
#
##########-----Master Theorem applied----########
#Example 1 Merge Sort:
# a (number of recursive calls) = 2 (recurse on both halves of problem size)
# b (factor by which problem size is smaller than original) = 2 (working on half the array)
# d (exponent in running time for work done outside recursive calls) = 1 (linear work done)
#
# b^d = 2 therefore a = b^d or Case 1 => T(n) <= O(n^d logn) => O(nlogn)
#
#
#-------------------------------------------Day 2----------------------------------------------#
#
#
#Example 2 Binary Search:
# a = 1 => 1 recursive call on either right or left half
# b = 2 => Recurse on half the array
# d = 0 => 1 comparison which is constant
#
# b^d = 2 therefore 2^0 = 1 or Case 1 => T(n) = O(n^dlogn) => O(logn)
#                                                  /
#                                                 /
#                                                n^0 == 1 and logn * 1 = logn
#
#Example 3 Integer Multiplication:
# a = 4 recurisve calls 
# b = 2 as you're using n/2 digits
# d = 1 doing additions and padding zeros in O(n)
#
# b^d = 2^1 = 2 < 4 - Case 3
#
# T(n) = O(n^logb^a) = O(n^log2^4) = O(n^2)
#
#
#
#
#Example 4 Gauss algorithm for Integer Multiplication:
# a = 3 recursive calls
# b = 2 as you're working on n/2 digits
# d = 1 as you're doing additions in O(n)
#
# 2^1 = 2 < 3 or Case 3 = T(n) = O(n^log2^3) = O(n^1.59)
#
#
#
#
#Example 5 Strassen's Matrix Multiplication:
# a = 7 as there is 7 recursive calls
# b = 2 as you're working on n/2 digits
# d = 2 as work done outside is linear to size matrix or quadratic to dimension of n
#
# b^d = 4 < 7 or Case 3 = T(n) = O(n^log2^7) = O(n^2.81) 
#
#
#
#
#Example 6 Fictitious Recurrence to demonstrate Case 2
# a = 2
# b = 2
# d = 2
#
# b^d = 4 > a or Case 2 => T(n) = O(n^2)
#
#
#Bullet Point: Use master method to determine running time by plugging in a,b,d factors.
#    You'll want to count number of recursive calls and assign to a, b represents the problem
#    size on each of the recursive calls and d represents work done outside of the recursive call.
#    Case 1 and Case 3 far and away most popular
#
#
##-----------------------------Day 3---------------------#####
#
###------Master Theorem Proof--------### 
# Focus: Conceptual meaning of each case as it relates to it's respective recursion tree.
#        This will lead to reverse engineering run times based on specific recursion tree.
#
#Assumption 1: recurrence is in following form:
#    i: T(1) <= c
#   ii: T(n) <= a(T(n/b)) + c(n^d)     (For some constant c)
#
#Assumption 2: n is power of b
#  (general case is similar but more tedious)
#
#Idea: Use recursion tree to analyze master method
#
#
#                    level 0:     n
#                                / \
#                               /   \ <------------ a branches  
#                              /     \
#         level 1           n/b     n/b
#                           /   \   /   \
#                          .     .  .    .
#                          .     .  .    .
#                          .     .  .    .
#        level logb^n     o o o o o o o o o o  <------------------base cases (size 1)
#
# Total work at level j (ignore all work in recursive calls):
#  
# <= a^j * [n/b^j]^d <<------- Work per level j subproblem
#   /          \
# # of         size of each level j subproblem
# level j
# subproblems
# 
# = cn^d * (a/b^d)^j
#
#
#
#Summing over all levels: j = 0,1,2,3,.......,logb^n
#
# total work <= cn^d * sum((a/b^d)^j for j in range(0,logb^n))
#
#
#Bullet Point: Recognizing conceptual meanings of each case of the master method as it
#    relates to it's respective recursion tree will provide insight into run times via
#    reverse engineering.
#
#
#--------------------------------------------Day 4--------------------------------------------#
#
#
####----Intuition for the Master Method----####
#
#Upper Bound work for level j in recursion tree:    c(n^d) * (a/b^d)^j
#
# Conceptually, this could be forces of evil working against forces of good. The input
# size goes down by factor b, but less work done per subproblem is key. Thus, b^d governs
# forces of good and a governs forces of evil.
#
#Interpretaton:                   Forces of evil, causes slow run time
#                                          /
#                                         /
# a   = rate of subproblem proliferation (RSP)
#
# b^d = rate of work shrinkage per subproblem (RWS)
#                                              \
#                                               \
#                                           Forces of good
# Key take aways/intuition of 3 cases:
#
# if RSP < RWS; amount of work decreases per recursion level j   ie. (expect O(n^d))
#
# if RSP > RWS; amount of work increases per recursion level j    ie. (expect O(#leaves))
#
# if RSP == RWS; amount of work is the same per recursion level j  ie. Mergesort (expect O(n^d*logn))
#
#-------------Proof of Master Method Pt. II--------------------------#####
#
# total work <= cn^d * sum((a/b^d)^j for j in range(0,logb^n)) = (*)   
#
# (Case 1)
#
# if a = b^d ;
#
# then
#
# * => c(n^d)(logb^n+1) => O(n^d*logn)
#
# (Case 2)
# 
# if a < b^d ; 
#
# then
#
# O(n^d) ie. work is dominated by top level
#
# (Case 3)
#
# if a > b^d ;
#
# then
#
# O(n^d(a/b^d)^logb^n) => b^-dlogb^n => n^-d => n^d => O(a^logb^n) (# of leaves)
#
#
#--------------Basic Sum Facts-----------------#
#
# for r != 1; sum powers of r                   
#   1 + r + r^2 + r^3 + ..+..+..+..+ r^k  =   (r^k+1)-1 / r-1
#                                              independent of k
# Upshot:                                     /
# 1: if r<1 is constant; <= 1/r-1 = a constant  ie. first term of sum dominates
# 2: if r>1 is constant; RHS <= r^k * (1*(1/r-1)) ie. last term of sum dominates
#
#
#
######---------------------------Day 5-------------------------------########
#
#
###------Quick-sort-------### - Developed by Tony Hoare
#
#Key idea: Partition around pivot element - must be careful in choosing; first element is safe choice
#
#Step 1: Choose pivot element        [3, 8, 2, 5, 1, 4, 7, 6]
#                                    /
#                                  pivot element
#
#
#Step 2: Arrange array to satisfy two properties:         [2, 1, 3, 6, 7, 4, 5, 8]
#                                                         |____|   |_____________| 
#            - left of pivot if element < pivot              /             \
#            - right of pivot if element > pivot            /               \
#                                                        < pivot            > pivot
#Note: Order not necessary, just partial sort into >/< buckets, central to pivot, but leaves pivot
#           in proper position.
#
#Facts for partitioning:
#    - linear time O(n) where n is size of input; no extra memory
#    - reduces problem size and enables divide and conquer
#
#High level description of QuickSort Algorithm:
#
"""
Quicksort(array A, length n):
    left = []
    right = []
    if n == 1:             #check single element arrays
        return array A
    pivot = A[0]           #choose pivot elememt, first element works 
    partition around A
    recursively sort right half
    recursively sort left half
"""
#
#Bullet Point: Key here is to choose a good pivot, if first element is always chosen, then already
#                  sorted lists will be O(n^2). But if we always choose the median of the subarray then it's 
#                  running time drops to O(nlogn).
#
#
####----------Probability Review-------------####
#Concept 1: Sample Spaces
#
#Sample space Omega = "all possible outcomes"
#    [this is usually finite in algorithms]
#
#Also: each outcome i-E-Omega has probability p(i) >= 0
#
#constraint: sum(p(i)) == 1                                  36 ordered pairs 
#                                                             /
#Example 1: 2 6-sided dice: (Omega) = [all 36 possible outcomes]
#    and p(i) = 1/36 for all i-E-Omega
#
#Example 2: choosing random pivot in outer Quicksort call
#  Omega = {1,2,....n} - corresponding to index of pivot and each p(i) = 1/n for all i-E-Omega
#
#Concept 2: Events - a subset of Omega
#Probability of event: sum of all probabilities within event S is sum(p(i) for all i in s)
#
#Example 1: probability of event where the sum of two dice is 7:
#    1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 == 3/18 == 1/6
#    (1,6) (5,2) (3,4) (6,1) (2,5) (4,3)
#
#Example 2: probability of event where pivot selection in quicksort provides 25-75 split or better
#    S = {(n/4 + 1)th smallest element, ...., (3n/4)th smallest element}
#    P(S) == (n/2)/n == 1/2
#
#Concept 3: Random Variables
#
#
#
#
#
#
#
#
#
#









