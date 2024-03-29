'''
Given 3 numbers A, B and C. Find the greatest number among them.

Example 1:

Input: A = 10, B = 3, C = 2
Output: 10
Explanation:
10 is the greatest among the three.
Example 2:

Input: A = -4, B = -3, C = -2
Output: -2
Explanation:
-2 is the greatest among the three.

Your Task:
You don't need to read input or print anything.Your task is to complete the function greatestOfThree() which takes three numbers A,B and C as input parameters and returns the greatest among them.


Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)


Constraints:
-109<=A,B,C<=109
'''
class Solution:
    def greatestOfThree(self,A,B,C):
        #code here
        a=A
        b=B
        c=C
        if(a>b and a>c):
            return a
        elif(b>a and b>c):
            return b
        else:
            return c
