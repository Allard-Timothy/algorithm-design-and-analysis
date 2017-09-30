
def swap(n, index_1, index_2):
    """Swap elements in array n."""
    n[index_1], n[index_2] = n[index_2], n[index_1]

def partition(n, first_el, last_el):
    """Partition array n with first element as pivot."""
    pivot_point = n[first_el]
    return_pivot = first_el + 1 
    for x in range(first_el + 1, last_el):
        if n[x] < pivot_point:
            swap(n, return_pivot, x)
            return_pivot += 1
    swap(n, return_pivot - 1, first_el)
    return return_pivot - 1

def quick_sort_w_partition(n, first_el, last_el):
    if last_el - first_el <= 1:
        return n
    else:
        pivot_point = partition(n, first_el, last_el)
        quick_sort_w_partition(n, first_el, pivot_point)
        quick_sort_w_partition(n, pivot_point + 1, last_el)
        return n

if __name__ == '__main__':
    
    k = [1,10,4,11,3,17,4]
    print quick_sort_w_partition(k, 0, len(k))
    
