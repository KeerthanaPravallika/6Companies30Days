'''

Question Link : https://leetcode.com/problems/combination-sum-iii/description/
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def function(lst,index):
            if len(lst) > k or sum(lst) > n:
                return
            if len(lst) == k and sum(lst) == n :
                res.append(lst)
                return
            else:
                for j in range(index,len(num)):
                    function(lst+[num[j]],j+1)
        
        res = []
        num = [i for i in range(1,10)]
        function([],0)
        return res
