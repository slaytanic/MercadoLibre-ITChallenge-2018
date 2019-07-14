
// A DP based solution to find Jacobsthal 
// and Jacobsthal-Lucas numbers  
#include <bits/stdc++.h> 
using namespace std; 
  
// Return nth Jacobsthal number. 
int Jacobsthal(unsigned long n) 
{ 
    unsigned long dp[n + 1]; 
  
    // base case 
    dp[0] = 0; 
    dp[1] = 1; 
  
    for (unsigned long i = 2; i <= n; i++) 
        dp[i] = dp[i - 1] + 2 * dp[i - 2]; 
  
    return dp[n]; 
} 
  
// Return nth Jacobsthal-Lucas number. 
int Jacobsthal_Lucas(int n) 
{ 
    int dp[n + 1]; 
  
    // base case 
    dp[0] = 2; 
    dp[1] = 1; 
  
    for (int i = 2; i <= n; i++) 
        dp[i] = dp[i - 1] + 2 * dp[i - 2]; 
  
    return dp[n]; 
} 
// Driven Program 
int main() 
{ 
    for(unsigned long n = 1; n < 100; n++) { 
      cout << "Jacobsthal number " << n << ": " << Jacobsthal(n) << endl; 
      // cout << "Jacobsthal-Lucas number: " << Jacobsthal_Lucas(n) << endl;
    } 
    return 0; 
} 
