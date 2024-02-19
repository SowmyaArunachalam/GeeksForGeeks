'''
Given a square matrix of size n×n. Your task is to calculate the sum of its diagonals.
 

Example 1:

Input: matrix = {{1, 1, 1}, 
{1, 1, 1}, {1, 1, 1}}
Output: 6
Example 2:

Input: matrix = {{1, 2}, {3, 4}}
Output: 10
 

Your Task:
You don't need to read or print anyhting. Your task is to complete the function DiagonalSum() which takes the matrix as input parameter and returns the sum of its diagonals.
 

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
1 <= n <= 100
1 <= matrix elements <= 10000


'''
class Solution:
	def DiagonalSum(self, matrix):
		# Code here
		s1=0
		s2=0
		for i in range(0,len(matrix)):
		    for j in range(0,len(matrix)):
		        if(i==j):
		            s1+=matrix[i][j]
		        if((i+j)==(n-1)):
		            s2+=matrix[i][j]
	    return s1+s2

