# Given a positive integer N, print pretty square of N.
# Pretty square of 1 is :
# 1
# pretty square of 2 is:
# 2 2 2
# 2 1 2
# 2 2 2
# pretty square of 3 is:
# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3
# Invokation: python3 pretty_square.py 5

import sys

N = sys.argv[1]


def printmat(n: int) -> None:
    '''
    Function takes integer input n and prints pretty matrix.
    '''
    pretty_mat = []

    for i in range(2*n-1):
        pretty_mat.append([0]*(2*n-1))

    for i in range(2*n-1):
        for j in range(2*n-1):
            dis_i = min(i-0, (2*n-2)-i)
            dis_j = min(j-0, (2*n-2)-j)
            pretty_mat[i][j] = str(n-min(dis_i, dis_j))

    print(f'Pretty Square of {n} is:')
    for row in pretty_mat:
        print(" ".join(row))


try:
    N = int(N)
    if(N > 0):
        printmat(N)
    else:
        print("Please enter a positive integer greater than 0!")
except:
    print("Please enter a valid integer!")
