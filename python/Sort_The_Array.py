'''
Given a random set of numbers, Print them in ascending sorted order.

Example 1:

Input:
n = 4
arr[] = {1, 5, 3, 2}
Output: {1, 2, 3, 5}
Explanation: After sorting array will 
be like {1, 2, 3, 5}.
Example 2:

Input:
n = 2
arr[] = {3, 1}
Output: {1, 3}
Explanation: After sorting array will
be like {1, 3}.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sortArr() which takes the list of integers and the size n as inputs and returns the modified list.

Expected Time Complexity: O(n * log n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n, arr[i] ≤ 105
'''
class Solution:
    def sortArr(self, arr, n): 
        #code here
        s=sorted(arr)
        return s
