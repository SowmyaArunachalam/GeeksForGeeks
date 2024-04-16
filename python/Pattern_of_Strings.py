'''
Given a string S of length N, find the pattern of the strings as shown below in the examples.

Example 1:

Input: S = "GeeK"
Output: Geek
        Gee
        Ge
        G
Explanation: Decrease one character 
after each line
â€‹Example 2:

Input: S = "G*g" 
Output: G*g
        G*
        G
Explanation: Decrease one character
after each line
Your Task:  
You don't need to read input or print anything. Your task is to complete the function pattern() which takes the string S as inputs and returns the answer as a list of strings.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N2)

Constraints:
1 ≤ N ≤ 103


'''
class Solution:
	def pattern(self, S):
		# code here
		k=[]
		for i in range(len(S),0,-1):
		    k.append(S[:i])
		return k
