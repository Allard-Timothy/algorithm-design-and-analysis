#####-------Hash Tables and Hash Table Operations--------#######
# Idea: Mapping of key to item
# Purpose: maintain a possibly evolving set of items
# Operations:
#  - Insert
#  - Delete
#  - Lookup
# Running Time: O(1) for all operations
#   - If not properly implemented (multiple values at single key) *Danger: easy to impl. wrong*
#   - non-pathological data
# 
####-----Applications-------####
#
# De-Duplication Problem: * trivial use
#  - stream of objects
# 
# Goal: remove duplication ie. keep track of unique objects
# Solution: when new object arrives; look up in hash
#             - if not found
#               - add to hash
#
# 2-Sum Problem:
#  - in unsorted array; how many integers sum to target
# 
# Goal: determine if there are two numbers (x, y) in A with x + y = t
# Solution:
#  - Naive:
#      - Brute Force: O(n^2)
#  - Better: 
#      - Sort first; for each x in A;
#      - look for t - x in A via binary search: O(logn)
#  - Best:
#      - insert all elements into hash
#      - for each x, look up t-x in hash
#
###----------Historical Applications---------###
# - Fast lookups for compilers
# - Blocking network traffic
# - speeding up search (ie. game-tree exploration)
#
#
#
#####---------Implementation Details------------#####
# 
# Setup: Figure out what you want to store ie. universe of application 
#    - all possible IP addresses, all possible names, all possible chess board configs
#    - Generally, really big
#
# Goal: want to maintain evovlving set 
#    - Generally, of reasonable size
#
# Naive solutions:
#    - array-based solution; indexed by u
#         - O(1) operations but O(u) space where u is all elements
#    - list-bases solution
#
# Optimized solution: 
#    - pick n=# of buckets with n = |s|
#    - choose hash function h: U = {1,2,3,4,5,...,n-1}   
#    - use arrau A of length m, store x in A[h(x)]
#
######----------Resolving Collisions--------#########
#
# Collision: mapping of different elements to same bucket
# Solution1: chaining
#    - keep linked list in each bucket
#    - given key/object x, perform insert/delete/lookup
#          in the list of A[h(x)]
#
# Solution2: open addressing - one object per bucket
#    - hash function specifies probe sequence where it
#         keeps looking until it hits empty slot
#    - probe sequence: linear probe == sequential
#    - double hashing: provide second hash to offset bucket ie. 1st == 17, look at 23 ==
#          not empty; increment by 23 and look there until you find opening
#
#
####---------Good Hash Functions--------############# 
#
# Note: in hash with chaining, Insert is O(1)
# - Reduce collisions
# - handle collisions properly
#
##--Chaining---####
#
# - Insert is O(1)
# - O(len of list) for insert/delete
#     - len of list could be m/n to m for m
#
#
# key Ideas:
#  - spead data uniformly across
#     - completely randomized
#  - easy to store and very fast to evaluate
# Bad Hash functions
#  - keys equal phone numbers (10 digits)
#    - len of n == 10^10
#    - choose n == 10^3
#  
# - bad: h(x) = 1st three digits of phone number
# - mediocre: h(x) = last three digits of phone number - still vulnerable to patterns
#
#
#
#####-------Bloom Filters------#########
#
###Space efficiency is key
#
# Exact Operations as Hash Table
#
# Pros and Cons
#    - Raison D'etre: Faster insert and lookup
#    - no deletions
#    - Can't store associated object
#    - False positives
#
#---Applications---###
#
# - early spell checkers
# - list of forbidden passwords
# - network routers
#   - limited memory; need to be super fast
#
#
#
#

































