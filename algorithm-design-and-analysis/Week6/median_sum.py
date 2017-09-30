import sys
from heapq import heappush, heappop
from stream import Stream

def read_file(file_name):
    """Takes in a file and outputs it's contents"""
    f = open(file_name, 'r')
    return f.readlines()
    
def make_stream(l_object):
    """Add a decorator for the Stream Class. We'll stream the contents
    from the provided list object.
    """
    def compute_rest():
        return make_stream(l_object[1:])
    return Stream(l_object[0], compute_rest)

def compute_median(stream):
    """By delegating min/max properties to each half of the heap,
    we can build a structure that is easy to find the median.
    """
    top_half = []
    bottom_half = []
    while stream:
        if len(bottom_half) == 0 or (int)(stream.first) < -(bottom_half[0]): 
            heappush(bottom_half, -(int)(stream.first)) 
        else:
            heappush(top_half, (int)(stream.first))
        stream = stream.rest
        if len(top_half) - len(bottom_half) > 1:
            heappush(bottom_half, -heappop(top_half))
        elif len(bottom_half) - len(top_half) > 1:
            heappush(top_half, -heappop(bottom_half))

        if len(top_half) > len(bottom_half):
            yield top_half[0]
        else:
            yield (-bottom_half[0])
            
def find_median(file_name):
    l_object = read_file(file_name)
    stream = make_stream(l_object)
    final = 0
    for median in compute_median(stream):
        final += median
        print final
    print "Sum of all the medians modulo 10000 is: {}".format(final % 10000)

if __name__ == '__main__':
    file_name = "/users/timallard/git_repo/coursera_design_analysis_algorithms/Week6/Median.txt"
    find_median(file_name)