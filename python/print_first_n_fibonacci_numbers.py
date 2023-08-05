'''
Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.

Example 1:

Input:
N = 5
Output: 1 1 2 3 5
Example 2:

Input:
N = 7
Output: 1 1 2 3 5 8 13
Your Task:
Your task is to complete printFibb() which takes single argument N and returns a list of first N Fibonacci numbers.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Note: This space is used to store and return the answer for printing purpose.

Constraints:
1<= N <=84
'''
class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        a=0
        b=1
        d=[]
        print(b,end=" ")
        for i in range(n-1):
            c=a+b
            d.append(c)
            a=b
            b=c
        return d
