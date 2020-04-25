'''
Quick Sort Algorithm
Time complexity: O(nlogn)
Space complexity: O(1) - In place 
'''
def partition(A, lo, hi):
    pivot = A[hi]
    p = lo - 1
    for i in range(lo, hi):
        if A[i] <= pivot:
            p += 1
            A[i], A[p] = A[p], A[i]
    
    # place pivot element in its place
    A[p+1], A[hi] = A[hi], A[p+1]

    # return index of pivot after partitioning
    return p+1

def quickSort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quickSort(A, lo, p-1)
        quickSort(A, p+1, hi)

arr = [5, 10, 8, 7, 3, 6, 12, 2, 7]

quickSort(arr, 0, len(arr)-1)
print(arr)