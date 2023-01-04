/*

Question Link : https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.

Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.

Note that an integer x divides y if y % x == 0.

 

Example 1:

Input: nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
Output: 2
Explanation: 
The smallest element in [2,3,2,4,3] is 2, which does not divide all the elements of numsDivide.
We use 2 deletions to delete the elements in nums that are equal to 2 which makes nums = [3,4,3].
The smallest element in [3,4,3] is 3, which divides all the elements of numsDivide.
It can be shown that 2 is the minimum number of deletions needed.

*/

class Solution {
public:
    int minOperations(vector<int> &nums, vector<int> &numsDivide) {

        /*
        If a number x divides all the elements of an array then we can say it is one  of it's common divisors if not GCD .

If we can manage to find the GCD of all the elements in the array numsDivide and then manage to find the smallest element from nums which divides the GCD then our answer will be the smallest number (GCD can itself be the answer also).
*/
        int gcd = numsDivide[0];
        for (int i = 1; i < numsDivide.size(); ++i)
            gcd = std::__gcd(gcd, numsDivide[i]);

        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); i++)
            if (gcd % nums[i] == 0) return i;
        return -1;
    }
};
