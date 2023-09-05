'''
Check if divisible by 4
BasicAccuracy: 46.91%Submissions: 13K+Points: 1
Join the most popular course on DSA. Master Skills & Become Employable by enrolling today! 
Given a number N. Check whether it is divisble by 4.

Example 1:

Input:
N = 1124
Output: 1
Explanation: The number is divisible by 4
as 1124 % 4 = 0.

â€‹Example 2:

Input: 
N = 7
Output: 0
Explanation: The number is not divisibly by
4 as 7 % 4 = 3.

Your Task:
You don't need to read input or print anything. Your task is to complete the function divisibleBy4() which takes the number in the form of a string N as input and returns 1 if the number is divisible by 4. Else, it returns 0.


Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).


Constraints:
1 <= N <= 101000+5

'''
class Solution:
	def divisibleBy4 (self, N):
		# Your Code Here
        if int(N)%4==0 :
            return 1
        else: 
            return 0
