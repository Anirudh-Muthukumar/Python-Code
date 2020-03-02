def partition(A, lo, hi):
    i = lo - 1
    pivot = A[hi]

    for j in range(lo, hi):
        if A[j] < pivot:
            i+=1
            A[i], A[j] = A[j], A[i]
    
    # Position pivot at correctly
    A[i+1], A[hi] = A[hi], A[i+1]

    return i+1

def quickSort(A, lo, hi):
    if lo < hi :
        pi = partition(A, lo, hi)
        # Element at pi is sorted
        
        # Sort left half and right half
        quickSort(A, lo, pi-1)
        quickSort(A, pi+1, hi)

if __name__ == '__main__':
    nums = [10, 7, 8, 9, 1, 5] 
    quickSort(nums, 0, len(nums)-1)
    print("Sorted Array: ", nums)