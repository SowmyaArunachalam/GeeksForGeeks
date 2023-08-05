'''
Given a number, N. Find the sum of all the digits of N
 

Example 1:

Input:
N = 12
Output:
3
Explanation:
Sum of 12's digits:
1 + 2 = 3
Example 2:

Input:
N = 23
Output
5
Explanation:
Sum of 23's digits:
2 + 3 = 5

Your Task:
You don't need to read input or print anything. Your task is to complete the function sumOfDigits() which takes an integer N as input parameters and returns an integer, total sum of digits of N.
'''
class Solution:
    def sumOfDigits (self, N):
        # code here
        c=str(N)
        s=0
        for i in range(0,len(c)):
            s+=int(c[i])
        return s
