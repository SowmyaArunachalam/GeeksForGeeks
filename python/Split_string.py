'''
Given a string S which consists of alphabets , numbers and special characters. You need to write a program to split the strings in three different strings S1, S2 and S3 such that the string S1 will contain all the alphabets present in S , the string S2 will contain all the numbers present in S and S3 will contain all special characters present in S.  The strings S1, S2 and S3 should have characters in same order as they appear in input.


Example 1:

Input:
S = geeks01for02geeks03!!!
Output:
geeksforgeeks
010203
!!!
Explanation: The output shows S1, S2 and S3. 
Example 2:

Input:
S = **Docoding123456789everyday##
Output:
Docodingeveryday
123456789
**##

Your Task:  
You dont need to read input or print anything. Complete the function splitString() which takes the string S as input parameters and returns a list of strings containing S1, S2 and S3 respectively. If you return an empty string the driver will print -1.

 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(N)

 

Constraints:
1 ≤ |S| ≤ 105
'''
class Solution:
    def splitString(ob, S): 
        # code here 
        al=""
        n=""
        sy=""
        l=[]
        for i in range(0,len(S)):
            if ((S[i]>='A' and S[i]<='Z')or(S[i]>='a' and S[i]<='z')):
                al+=S[i]
            elif(S[i]>='0' and S[i]<='9'):
                n+=S[i]
            else:
                sy+=S[i]
        
        l.append(al)
        l.append(n)
        l.append(sy)
        return l
