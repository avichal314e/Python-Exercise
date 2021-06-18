# Given a list of N positive integers and a number S, find out and return a continuous sub-list sum of whose elements is S, return empty list if no such sub array exists.
# Invokation: python3 sublistsum.py


from typing import List


def findSublist(arr: List[int], n: int, target: int) -> List[int]:
    '''
    Function returns sublist having the sum of elements equal to target.
    '''
    if(not arr):
        return []
    arr += [0]
    i = 0
    j = 1
    current_sum = arr[0]
    while(j < n):
        if(current_sum == target):
            return arr[i:j]
        elif(current_sum < target):
            current_sum += arr[j]
            j += 1
        else:
            current_sum -= arr[i]
            i += 1

    if(current_sum == target):
        return arr[i:j]
    return []


try:
    N = int(input("Please enter the number of elements: "))
    print("Enter numbers in array as space separated integers: ")
    arr = list(map(int, input().split()))
    S = int(input("Enter the sum of sub-list required: "))
    output = findSublist(arr, N, S)
    print(output)
except:
    print("Please enter valid input!")
