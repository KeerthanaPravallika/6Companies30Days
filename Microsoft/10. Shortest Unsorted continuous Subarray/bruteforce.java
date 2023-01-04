/*

Question link : https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

*/

class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int[] arr= new int[nums.length];
        System.arraycopy(nums,0,arr,0,nums.length);
        Arrays.sort(arr);

        int start = 0, end = nums.length-1;

        for(;start < nums.length; start++)
            if(nums[start] != arr[start]) 
                break;
        // if it reaches to end
        if(start >= nums.length-1) 
            return 0;
        for(; end>=0; end--)
            if(nums[end] != arr[end])
                 break;
        
        return end-start+1;
    }
}
