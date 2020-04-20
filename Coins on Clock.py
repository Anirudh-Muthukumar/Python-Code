'''
4 pennies (1 hour)
4 nickles (5 hours)
4 dimes (10 hours)
'''

mp = ['P', 'N', 'D']
val = [1, 5, 10]
decode = {'P': 1, 'N': 5, 'D': 10}
clock = [i+1 for i in range(12)]
coins = [4, 4, 4]

max_profit = -float('inf')
min_profit = float('inf')

max_bits = None
min_bits = None

found = False
combs = set()
ct = 0

def bt(clock, pos, coins, bits):
    global max_profit
    global min_profit
    global min_bits
    global max_bits
    global ct

    if len(clock)==0:
        combs.add(str(bits))
        print(bits)
        ct+=1
        if bits == "NNPDDNPPPNDD":
            found = True
        profit = 0
        for i, bit in enumerate(bits[1:]):
            profit += (i+1)*decode[bit]
        if profit > max_profit:
            max_profit = profit
            max_bits = bits
        if profit < min_profit:
            min_profit = profit
            min_bits = bits    
        return True
    
    # wrong sequence backtrack
    if pos not in clock:
        return False
    
    # pos is a valid position, try placing each coin in given position
    for i in range(3):
        if coins[i]>0:
            bits[pos] = mp[i]
            coins[i]-=1
            clock.remove(pos) 
            new_pos = pos + val[i]

            if new_pos > 12:
                new_pos = new_pos % 12

            bt(clock[:], new_pos, coins[:], bits[:])
        
            # back track
            bits[pos] = None
            coins[i] += 1
            clock.append(pos)
    
    return False
            
for time in clock:
    bt(clock[:], time, coins[:], [None]*13)

print("Max profit = ", max_profit, max_bits)
print("Min profit = ", min_profit, min_bits)
print("Total ", len(combs))

# def dp(clock, pos, coins, lookup):
#     if len(clock)==0:
#         return 0
    
#     # print(clock, pos, not pos in clock)

#     if pos not in clock: # infeasible arrangement
#         print("Done")
#         return -float('inf')
    
#     key = str(clock) + '|' + str(pos) + '|' + str(coins)

#     if key not in lookup:

#         profit = -1

#         for i in range(len(coins)):
#             if coins[i]>0:
#                 coins[i]-=1
#                 # print(clock, pos, pos not in clock)
#                 if pos not in clock:
#                     return -float('inf')
#                 clock.remove(pos) 
#                 new_pos = pos + val[i]
#                 if new_pos > 12:
#                     new_pos = new_pos % 12
#                 profit = max(profit, pos*val[i] + dp(clock[:], new_pos, coins[:], lookup))
            
#             lookup[key] = profit

#     return lookup[key]

# # max_dp = 0

# for time in range(1, 12):
#     print(time, dp(clock[:], time, coins[:], {}))