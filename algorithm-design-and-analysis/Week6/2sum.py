import sys

def read_file(file_name):
    f = open(file_name, 'r')
    return f.readlines()

def create_dict(data):
    """Create hashmap for input data."""
    return {(int)(elem) for elem in data}

def find_2sum(result_dict, range_start, range_end):
    """Find the number of target values for desired range."""
    sat_count = 0
    for target in range(range_start, range_end):
        for x in result_dict:
            y = target - x
            if y in result_dict and y != x:
                sat_count += 1
                break
    return sat_count
    
def run_hash(file_name, start, end):
    result_dict = create_dict(file_name)
    print "The number of target values in [-10000, 10000] \
    that satisfied the requirement is: {}".format(find_2sum(result_dict,
                                                            start,
                                                            end))
    
if __name__ == '__main__':
    start = -10000
    end = 10000
    file_name = "/users/timallard/git_repo/coursera_design_analysis_algorithms/Week6/2sum.txt"
    run_hash(file_name, start, end)











