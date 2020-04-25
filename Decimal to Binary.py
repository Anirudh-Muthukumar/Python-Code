def binary(x):
    ans = ""
    while x:
        if x&1:
            ans += '1'
        else:
            ans += '0'
        x = x//2
    
    return ans[::-1]   

for i in range(8, 16):
    print(binary(i))