# Sorting a linked list
# Merge sort is usually used for sorting a linked list because many other sorting techniques like quick sort and heap sort
# have poor performance due to slow random-access of linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMiddle(head):
    if not head or not head.next:
        return head 
    
    slow, fast = head, head 

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next 
    
    return slow

def merge(A, B):
    result = None

    if not A:
        return B
    if not B:
        return A

    if A.data <= B.data:
        result = A  
        result.next = merge(A.next, B)
    else:
        result = B
        result.next = merge(A, B.next)
    
    return result 

def mergeSort(head):
    
    if not head or not head.next:       # if 0 or 1 element
        return head

    middleElement = findMiddle(head)
    middleNext = middleElement.next 

    # Break linked list into two halves
    middleElement.next = None

    # Merge Sort both the halves 
    leftHalf = mergeSort(head)
    rightHalf = mergeSort(middleNext)

    print(leftHalf.data)
    print(rightHalf.data)

    # Merge two sorted arrays
    newHead = merge(leftHalf, rightHalf) 

    return newHead


if __name__ == '__main__':

    temp = Node(15)
    head = temp 
    temp.next = Node(10)
    temp = temp.next
    temp.next = Node(5)
    temp = temp.next
    temp.next = Node(20)
    temp = temp.next
    temp.next = Node(3)
    temp = temp.next
    temp.next = Node(2)
    
    print("Linked List before sorting: ")
    temp = head
    while (temp):
        print(temp.data, end = ' ')
        temp = temp.next
    
    # Merge sort 
    newHead = mergeSort(head)
    print()

    print("Sorted Linked List: ")
    temp = newHead
    while (temp):
        print(temp.data, end = ' ')
        temp = temp.next

    print()