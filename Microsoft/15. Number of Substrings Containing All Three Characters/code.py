'''
Question link : https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        cnt = 0
        a_index,b_index,c_index = -1,-1,-1

        for key,val in enumerate(s):
            if val == 'a':
                a_index = key
            elif val == 'b':
                b_index = key
            else:
                c_index = key
        
            if key>1:
                cnt += min([a_index,b_index,c_index])+1
        return cnt

