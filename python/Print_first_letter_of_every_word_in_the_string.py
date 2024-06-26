'''
Given a string S, the task is to create a string with the first letter of every word in the string.
 

Example 1:

Input: 
S = "geeks for geeks"
Output: gfg

Example 2:

Input: 
S = "bad is good"
Output: big

Your Task:
You don't need to read input or print anything. Your task is to complete the function firstAlphabet() which takes string S as input parameter and returns a string that contains the first letter of every word in S.


Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)


Constraints:
1 <= |S| <= 105
S contains lower case English alphabets
Words have a single space between them.
'''
class Solution:
	def firstAlphabet(self, S):
		# code here
		d=""
		d+=S[0]
		for i in range(0,len(S)):
		    if S[i]==" ":
		        d+=S[i+1]
        return d
