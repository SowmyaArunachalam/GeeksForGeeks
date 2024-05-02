/*
Given a positive integer, N. Find the factorial of N.
 

Example 1:

Input:
N = 5
Output:
120
Explanation:
5*4*3*2*1 = 120
Example 2:

Input:
N = 4
Output:
24
Explanation:
4*3*2*1 = 24

Your Task:
You don't need to read input or print anything. Your task is to complete the function factorial() which takes an integer N as input parameters and returns an integer, the factorial of N.
 

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 

Constraints:
0 <= N <= 18
*/
long long int factorial(int N){
       //code here
       long f=1;
       for(int i=1;i<=N;i++){
           f*=i;
       }
       return f;
       
}
