'''
Given a string. Count the number of Camel Case characters in it.

Example 1:

Input:
S = "ckjkUUYII"
Output: 5
Explanation: Camel Case characters present:
U, U, Y, I and I.

â€‹Example 2:

Input: 
S = "abcd"
Output: 0
Explanation: No Camel Case character
present.

Your Task:
You don't need to read input or print anything. Your task is to complete the function countCamelCase() which takes the string S as input and returns the count of the camel case characters in the string.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1<=|S|<=105
'''
class Solution:
    def countCamelCase (self,s):
        # your code here
        c=0
        for i in s:
            if(i.isupper()):
                c+=1
        return c
