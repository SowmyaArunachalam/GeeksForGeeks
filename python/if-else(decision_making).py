'''
Given two integers, n and m. The task is to check the relation between n and m.

Example 1:

Input:
n = 4
m = 8

Output:
lesser

Explanation:
4 < 8 so print 'lesser'.
Example 2:

Input:
n = 8
m = 8

Output:
equal

Explanation:
8 = 8 so print 'equal'.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function compareNM() which takes two integer n and m as input parameters and returns string
'lesser' if n < m
'equal' if n == m
'greater' if n > m

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
-10000 <= m <= 10000
-10000 <= n <= 10000
'''
class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if(n<m):
            return "lesser"
        elif(n>m):
            return "greater"
        else:
            return "equal"
