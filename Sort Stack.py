def sortStack(nums):
    stack1 = []
    stack2 = []

    temp = None

    for num in nums:
        stack1.append(num)
    
    while stack1:
        temp = stack1.pop()
        if not stack2:
            stack2.append(temp)
        else:
            while stack2 and stack2[-1]>temp:
                stack1.append(stack2.pop())
            stack2.append(temp)
    
    print(stack2)

if __name__ == '__main__':
    sortStack([2,3,1,4])
