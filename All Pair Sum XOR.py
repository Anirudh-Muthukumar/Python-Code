def allPairXOR(A):
    # Except for diagonal elements all the elements appear twice, so XOR of them will become 0
    res = 0
    for a in A:
        res ^= (2*a)
    return res 

if __name__ == '__main__':
    arr = [4, 3, 9, 1]
    print("All pair XOR = ", allPairXOR(arr))