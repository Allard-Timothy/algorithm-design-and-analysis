from mergesort_2d_array import *
import math 
import random 
import re

def pre(points):
    px = mergesort_2d(points, 0)
    py = mergesort_2d(points, 1)
    return px, py

def dist(pair):
    try:
        a, b = pair[0], pair[1]
        return math.sqrt((a[0] - b[0])**2 + (a[1] -b[1])**2)
    except:
        return None

def closest_split_pair(pair_x, pair_y, delta):
    mid = int(len(pair_x)/2)
    x_bar = pair_x[mid-1][0]
    bar_pts = [p for p in pair_y if ((x_bar-delta) <= p[0] <= (x_bar+delta))]
    best = delta
    best_pair = None
    for i in range(0, len(bar_pts)):
        for j in range(0, min(7, len(bar_pts)-i)):
            if i == (i + j):
                continue
            pair = [bar_pts[i], bar_pts[i+j]]
            if dist(pair) < best:
                best_pair = pair
                best = dist(pair)
    return best_pair

def closest_pair(pair_x, pair_y):
    mid = int(len(pair_x)/2)
    left_x = pair_x[:mid]
    right_x = pair_x[mid:]
    left_y = pair_y[:mid]
    right_y = pair_y[mid:]
    pair_dist = []
    if len(pair_x) == 1:
        return None
    elif len(pair_x) == 2:
        return pair_x
    else:
        left = closest_pair(left_x, left_y)
        right = closest_pair(right_x, right_y)
        if left == None:
            delta = dist(right)
        else:
            delta = min(dist(left), dist(right))
        split = closest_split_pair(pair_x, pair_y, delta)
        pair_dist = [(x, dist(x)) for x in (left, right, split) if x]
        return mergesort_2d(pair_dist, 1)[0][0]


#########-----------------Closest Pair Analysis-------------##################


#Input: a set p = {p1, p2, .....pn} of n points

#notation: d(pi, pj) = Euclidian distance
#  if pi = (xi, yi) and pj = (xj, yj)
#        d(pi, pj) = sqrt((xi-xj)^2 + (yi-yj)^2)

#output: pair of distinct points that minimize d(p,q) over range

#Assumptions: all points have distinct x-coord, y-coord
#Brute Force: O(n^2) 
#   note: even for 1d implementation, still O(n^2)
#1-d version: ---------*----*--*-------*-----*----
#                            \/
#                        closest pair
#
#step 1: sort points O(n logn)
#step 2: return closest pair of adjacent points O(n) 
#Goal: O(n logn) for 2-d version


#1: let q = left_p, r = right_p 
#    for qx, qy, rx, ry [takes O(n) time]
#2: (p1, q1) = closest_pair(qx, qy)
#3: (p2, q2) = closest_pair(rx, ry)
#4: (p3, q3) = closest_pair(px, py)
#5: return best of [(p1, q2), (p2,q2), (p3, q3)]





