def quick_sort(some_list):
    """
    Quicksort algorithm that accepts a list and returns it in sorted order.
    :param some_list: list of items to be sorted
    """
    #single element lists are already sorted
    if len(some_list) <= 1:
        return some_list
    #define first or last element as pivot point
    pivot_point = some_list[0]
    #list comprehension optimization beats out `for` loops
    left = quick_sort([x for x in some_list[1:] if x < pivot_point])
    right = quick_sort([x for x in some_list[1:] if x >= pivot_point])
    return left + [pivot_point] + right


def q(n):
    """Quicksort algorithm implemented without list comprehensions."""
    r = []
    l = []
    if len(n) <= 1: return n
    pivot = n[0]
    for x in n[1:]:
        if x < pivot:
            l.append(x)
            print l
        if x >= pivot:
            r.append(x)
            print r
    lt = q(l)
    rt = q(r)
    return lt + [pivot] + rt

if __name__ == '__main__':
    
    k = [10,9,11,17,22,3,5,7,33,99,1,9,8,13]
    print q(k)
    print quick_sort(k)

