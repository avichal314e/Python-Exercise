# Given a matrix (list of lists) of size N*M and a number X, find if X is present in matrix.
# Invokation: python3 findX.py


from typing import List


def findX(mat: List[List[int]], n: int, m: int, target: int) -> bool:
    '''
    Function returns True if element present, otherwise False.
    '''
    for i in range(n):
        for j in range(m):
            if(mat[i][j] == target):
                return True
    return False


try:
    N, M = map(int, input("Please enter N and M (dimensions): ").split())
    print("Enter the matrix row-wise, space seperated integers: ")
    mat = []
    for i in range(N):
        mat.append(list(map(int, input().split())))
    X = int(input("Enter the number to search: "))
    output = findX(mat, N, M, X)
    if(output):
        print(f'{X} is present in the matrix.')
    else:
        print(f'{X} is not present in the matrix.')

except:
    print("Please enter valid input!")
