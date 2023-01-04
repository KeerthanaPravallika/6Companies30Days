/*
Question Link : https://leetcode.com/problems/airplane-seat-assignment-probability/
n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

Take their own seat if it is still available, and
Pick other seats randomly when they find their seat occupied
Return the probability that the nth person gets his own seat.

 

Example 1:

Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.


*/

class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        if(n==1){
            return 1.0;
        }
        else
             return 0.5; /* as it has only two options 
             1. Take their own seat if it is still available
2. Pick other seats randomly when they find their seat occupied
*/
    }
};
