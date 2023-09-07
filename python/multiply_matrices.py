'''
Given two square Matrices A[][] and B[][]. Your task is to complete the function multiply which stores the multiplied matrices in a new matrix C[][].
 

Example 1:

Input: 
N = 2
A[][] = {{7, 8}, {2 , 9}}
B[][] = {{14, 5}, {5, 18}}

Output: 
C[][] = {{138, 179}, {73, 172}}
 

Example 2:

Input: 
N = 2
A[][] = {{17, 4}, {17 , 16}}
B[][] = {{9, 2}, {7, 1}}

Output: 
C[][] = {{181, 38}, {265, 50}}
Constraints:
1 <=T<= 100
1 <= N <= 20
'''
def multiply(A, B, C, n):
    # Code here
    for i in range(len(A)):
   # iterate through columns of Y
        for j in range(len(B[0])):
       # iterate through rows of Y
            for k in range(len(B)):
                 C[i][j] += A[i][k] * B[k][j]
    return C 
