# Palindromic substrings
# Expand around center
# O(n^2) and O(1)

def expandAroundCenter(s):
    ans = 0
    N = len(s)
    for center in range(2*N-1):
        left = center // 2
        right = left + center % 2
        while left>=0 and right < N and s[left]==s[right]:
            ans += 1
            left -= 1
            right += 1
    return ans

# Manacher's Algorithm for finding longest palindromic substring
# O(n) and O(n)
def manachersAlgorithm(s):
    A = "@#" + "#".join(s) + "#$"
    Z = [0] * len(A)

    center, right = 0, 0

    for i in range(1, len(A)-1):
        if i < right:           # right is the boundary of longest palindrome so far
            Z[i] = min(right - i, Z[2*center - i])  # updating the least possible length of Z[i] 
        
        #expand around center i
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        
        # update center, right
        if right < i + Z[i]:
            center = i
            right = i + Z[i]
    
    return Z




s = "ababa"
print("# of palindromic substrings in {} : {}".format(s, expandAroundCenter(s)))

ans = 0
# since we added 'n' characters, we have to count the length as (1+v)/2 for each palindrome of length v
for v in manachersAlgorithm(s):
    ans += (v+1)//2

print("# of palindromic substrings in {} : {}".format(s, ans))
