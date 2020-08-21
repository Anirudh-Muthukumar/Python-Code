'''
Boyer Moore Voting algorithm can be generalized to find all the elements which appear atleast floor(n/k)
times 

Time complexity : O(n+k)
Space complexity: O(k)
'''

import collections

def boyerMoore(A, k):
    n = len(A)
    counters = collections.defaultdict(int)
    occurences = collections.defaultdict(int)

    for x in A:
        occurences[x]+=1
        # maintain atmost k counters
        if len(counters) < k-1 or counters[x]:
            if x not in counters:
                counters[x] = 0
            counters[x] += 1
        else:
            for key in counters:
                counters[key] -= 1
            counters = {key: val for key, val in counters.items() if val}
    
    res = []
    for key, val in counters.items():
        if occurences[key] > n//k :
            res.append(key)
    
    return res

A = [1, 2, 3, 4, 1, 1, 3, 3]
print(boyerMoore(A, 4))