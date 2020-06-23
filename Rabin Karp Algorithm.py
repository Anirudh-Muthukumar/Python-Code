def search(text, pattern, q):
    d = 10
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    for i in range(n-m+1):
        if p==t:
            if text[i:i+m] == pattern:
                print("Found at position = ", i+1)
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
            if t<0:
                t += q
    
    

if __name__ == '__main__':
    text = "GEEKSFORGEEKS"
    pattern = "GEEK"
    prime = 101
    search(text, pattern, prime)



