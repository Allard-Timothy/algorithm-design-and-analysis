"""Take in text file containing an unsorted text file containing all digits (inclusive) from 1 - 10,000
and return the number of comparisons with the first index, last index and middle index as the pivot point.
"""

def check_median(elem_list, median, start, end, middle):
    """Compare the median to specific elements in element list."""
    if median == elem_list[start]:
        return start
    elif median == elem_list[end]:
        return end
    else:
        return middle

def swap(n, index_1, index_2):
    """Swap elements."""
    n[index_1], n[index_2] = n[index_2], n[index_1]

def middle_median(elem_list, start, end):
    """We'll want to handle the case when the pivot point is the middle index."""
    middle = start + int((end - start) / 2)
    median = min(max(elem_list[start], elem_list[end]),
                 max(elem_list[start], elem_list[middle]),
                 max(elem_list[middle], elem_list[end]))
    return check_median(elem_list, median, start, end, middle)
        
def elem_partition(elem_list, start, end, num_comparison, partition):
    """Partition elements in element list around specific pivot point.
    The goal is to partition element list with elements greater than
    pivot point on the right and elements less than pivot point on the 
    left side. The end results should leave the pivot point in the
    proper position.
    """
    if partition == 1:
        swap(elem_list, end, start)
    elif partition == 2:
        middle_med = middle_median(elem_list, start, end)
        swap(elem_list, middle_med, start)
    else:
        assert partition == 0, "Illegal pivot selection"
    pivot = elem_list[start]
    i = start + 1
    num_comparison[0] += end - start
    for j in range(start+1, end+1): # indices from start+1 to end
        if elem_list[j] < pivot:
            swap(elem_list, j, i)
            i += 1
    swap(elem_list, start, i-1)
    return i-1

def quicksort(elem_list, start, end, num_comparison, partition=0):
    """Runs quicksort algorithm on element list with specific pivot points 
    and specific index position.
    :param start: beginning position of element list
    :param end: last position of element list
    :param num_comparison: current comparision count
    :param partition: which point to pivot around.
    """
    if start < end: # if list has 2 or more items
        pivot_index = elem_partition(elem_list, 
                                     start, 
                                     end, 
                                     num_comparison, 
                                     partition)
        quicksort(elem_list, 
                  start, 
                  pivot_index - 1, 
                  num_comparison, 
                  partition)
        quicksort(elem_list, 
                  pivot_index + 1, 
                  end, 
                  num_comparison, 
                  partition)

def convert_pivot(case):
    """Takes in pivot case and returns the specific index."""
    if case == 0:
        return "first index"
    elif case == 1:
        return "last index"
    else:
        return "middle index"

def run_comparisons(file_path):
    """Takes in file_path to text file, runs quicksort and counts the comparisons.
    :param file_path: path to text file
    :return: number of comparisons for given index.
    """
    for case in range(3): # 0, 1, and 2
        f = open(file_path, 'r')
        line_list = f.readlines()
        int_list = [int(line.split()[0]) for line in line_list if line]
        num_comparison = [0]
        quicksort(int_list, 0, len(int_list)-1, num_comparison, case)
        print "The number of comparisons with pivot as {} is {}".format(convert_pivot(case), 
                                                                        num_comparison[0])
    
if __name__ == '__main__':
    fp = '/users/timallard/git_repo/coursera_design_analysis_algorithms/Week2/Week_2_algorithms/qsort_test.txt'
    run_comparisons(fp)



