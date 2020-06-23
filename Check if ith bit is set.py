def checkBit(n, i):
    return n & (1<<i)

if __name__ == '__main__':
    n = int(input())
    bit = int(input())
    if checkBit(n, bit):
        print("True")
    else:
        print("False")
