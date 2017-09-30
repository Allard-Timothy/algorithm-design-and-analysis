############################-------Week 1 Notes-------##########################################

Fast Algorithm: worst-case running time grows slowly with input size.

#Naive Integer Multiplication

#Karatsuba for Integer Multiplication
"""
x = 5678
y = 1234

a = x[0:2] = 56
b = x[2:] = 78
c = y[0:2] = 12
d = y[2:] = 34

z1 = ac = 672
z2 = bd = 2652
z3 = (a+b)(c+d) = 6164
z4 = z3 - z2 - z1 = 2840 

xy = (z1 * 10000) + z2 + (z4 * 100)  

n = len([k for k in str(x)]) # number of digits
a = str(x)[0:2]
b = str(x)[2:]
c = str(y)[0:2]
d = str(y)[2:]

x = ((10 ** n/2) * a) + b
y = ((10 ** n/2) * c) + d

z1 = ac
z2 = bd
z3 = (a+b) * (c+d)
z4 = ad
z5 = bc
star = ((10**n/2) * z1) + ((10**n/2) * (z4+ z5)) + z2
"""

###########------Asymptotic Analysis------##################

High-level concept: Suppress constant factors and lower-order terms
                           /                            \
                          /                              \
                     too system dependent           irrelevant for large inputs

eg: 6n * log2n + 6n == n logn


Examples: 

Problem 1: Does array A contain integer t?

for i = 1 to n
    if A[i] == t 
        return True
return False

Running time: O(n) - Linear

---------------------------

Problem 2: Given two arrays A, B of length n and integer t, does A or B contain t?

for i = 1 to n
    if A[i] == t
        return True
for i = 1 to n
    if B[i] == t
        return True
return False

Running time: O(n) - Linear

----------------------------

Problem 3: Do arrays A,B have a number in common, given arrays A, B of length n?

for i = 1 to n
    for j = 1 to n
        if A[i] == B[i]
            return True
return False

Running time: O(n^2) - Quadratic

----------------------------

Problem 4: Does array A have duplicate entries?

for i = 1 to n
    for j = 1 to n
        if A[i] == A[j] 
            return True
return True

Running time: O(n^2) - Quadratic

#####-----Big Oh-notation-----#####

Example 1:

Claim: if t(n) = A(k)* n^k + ........ + A(1)n + A(0) then
    t(n) == O(n^k)

Proof: 
n0 = 1 
c = 1(A)k(1) + 1(A)(k-1) + 1A(1)1 

Vn >= 1, T(n) <= c * n^k


Example 2:

Claim: 2^n+10 = O(2^n)
Proof:
Constants C1n0
2^n+10 <= C * 2^n

Vn >= n0

Note: 2^n+10 = 2^10 * 2^n = 1024 * 2^n


###########----------Divide and Conquer Paradigm--------##############

1: Divide into smaller sub-problems
2: Conquer sub-problems via recursion
3: Combine solutions of sub-problems into one for original problem



#########------Matrix Multiplication---------#############

Example:

matrix-x  *  matrix-y == matrix-z 

where zij = (ith row of x) * (jth row of y)

      n
==   SUM xik * yjk for input size O(n^2)
     k=1

Example:

(a   b)(e  f)    (ae+bg  af+bh)
(     )(    ) == (            ) 
(c   d)(g  h)    (ce+dg  cf+dh)

Apply Divide and Conquer

Break x and y down into subquandrants 

x = (a  b) and y = (e  f)
    (c  d)         (g  h)

where a-h are all n/2 * n/2

then:

x * y = (ae+bg  af+bh)
        (ce+dg  cf+dh)

Leads to recursive algorithm 1:

Step1: recursively compute 8 necessary products
Step2: do necessary additions
            O(n^2) - running time of additions
Fact: running time is O(n^3) 

#########-----------Strassen's Algorithm---------##########

Step1: recursively compute 7 products
Step2: do necessary addition + subtractions
            O(n^2)
Fact: better than cubic O(n^2)

p1 = a(f-h)
p2 = h(a+b)
p3 = e(c+d)
p4 = d(g-e)
p5 = (a+d)(e+h)
p6 = (b-d)(g+h)
p7 = (a-c)(e+f)

claim: x * y == (ae+bg  af+bh) == (p5+p4-p2+p6   p1+p2)
                (ce+dg  cf+dh)    (p3+p4   p1+p5-p3-p7)

proof: ae+bg == p5+p4+p2+p6 == ae+ah+de+dh+dg-de-ah-bh+bg+bh-dg-dh == ae+bg



















































