'''
The task is to complete the insertsort() function which is used to implement Insertion Sort.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: The sorted array will be [1, 3, 4, 7, 9].
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: The sorted array will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Input: arr[] = [4, 1, 9]
Output: [1, 4, 9]
Explanation: The sorted array will be [1, 4, 9].
Constraints:
1 <= arr.size() <= 1000
1 <= arr[i] <= 1000
'''
class Solution:
    def insertionSort(self, arr):
        #code here
        
        for j in range(1,len(arr)):
            curr=arr[j]
            i=j-1
            while(i>=0 and curr<arr[i]):
                arr[i+1]=arr[i]
                i-=1
            arr[i+1]=curr
        return arr