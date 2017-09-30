def merge_2d(a, b, axis = 0):
    i ,j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if a[i][axis] < b[j][axis]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:]
    c += b[j:]
    return c

def mergesort_2d(seq, axis = 0):
    if len(seq) == 1:
        return seq
    else:
        mid = int(len(seq)/2)
        head = mergesort_2d(seq[:mid], axis)
        end = mergesort_2d(seq[mid:], axis)
        return merge_2d(head, end, axis)