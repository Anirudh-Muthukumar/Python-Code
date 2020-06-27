def activitySelection(A):
    A.sort(key = lambda x: x[1])
    n = len(A)
    j = 0   # first activity is selected
    res = [0]
    for i in range(1, n):
        if A[i][0] > A[j][1]:      # start time of A[i] > finish time of A[j]
            res.append(i)
            j = i
    print("Activities = ", res)

if __name__ == '__main__':
    activities = [[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]]
    activitySelection(activities)