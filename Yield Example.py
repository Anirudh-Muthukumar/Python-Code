import itertools

def F(s):
    skip = 0
    for x in reversed(s):
        if x=='#':
            skip += 1
        elif skip > 0:
            skip -= 1
        else:
            yield x

s = "ab#c"
t = "ac"
x = [''.join(i) for i in F(s)]
y = [''.join(i) for i in F(t)]
print(x, y)