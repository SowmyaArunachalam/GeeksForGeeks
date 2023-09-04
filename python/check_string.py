'''
Given a string, check if all its characters are the same or not.

Example 1:

Input:
s = "geeks"
Output: False
Explanation: The string contains different
character 'g', 'e', 'k' and 's'.

Example 2:

Input: 
s = "gggg"
Output: True
Explanation: The string contains only one
character 'g'.

Your Task:
You don't need to read input or print anything. Your task is to complete the function check() which takes a string as input and returns True if all the characters in the string are the same. Else, it returns False.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1 <= |S| <= 104
'''
class Solution:
    def check (self,s):
        # your code here
        l=[]
        s1=list(set(s))
        for i in s1:
            if i not in l :
                l.append(i)
        if(len(l)==1):
            return True
        else:
            return False
