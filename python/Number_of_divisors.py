'''
Given an integer N, find the number of divisors of N that are divisible by 3.
 

Example 1:

Input : 6
Output: 2
Explanation: 1, 2, 3, 6 are divisors 
of 6 out of which 3 and 6 are divisible 
by 3.

Example 2:

Input: 10
Output: 0
Explanation: 1, 2, 5 and 10 are divisors 
of 10 but none of them are divisible by 3.
 

Your Task:

You don't need to read or print anything. Your task is to complete the function count_divisors() which takes N as input parameter and returns count of divisor which are divisible by 3.
 

Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)
 

Constraints:
1 <= N <= 105
'''
class Solution:
    def count_divisors(self, N):
        # code here
        
        count = 0
        sqrt_N = int(N ** 0.5)
        for i in range(1, sqrt_N + 1):
            if N % i == 0:
                if i % 3 == 0:
                    count += 1
                divisor = N // i
                if divisor != i and divisor % 3 == 0:
                    count += 1
        return count
