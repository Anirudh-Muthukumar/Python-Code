'''
Given an array of integers, find the total sum of all the unordered pair XOR of an array.

A = [5, 3, 9]

Total Sum = (5^3) + (5^9) + (3^9)
          = 6 + 12 + 10
          = 28

Idea: (Number of pairs with ith bit set) X (1<<i)

'''
def totalSum(A):
    res = 0
    for i in range(31):
        ct_0, ct_1 = 0, 0
        for num in A:
            if num & (1<<i):
                ct_1 += 1
            else:
                ct_0 += 1
        pairs = ct_1 * ct_0
        res += pairs * (1<<i)
    return res



if __name__ == '__main__':
    # A = [5, 3, 9]
    A = [5, 9, 7, 6]
    print("Total Sum = ", totalSum(A))