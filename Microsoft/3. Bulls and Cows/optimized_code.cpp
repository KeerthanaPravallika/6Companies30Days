/*
Question link : https://leetcode.com/problems/bulls-and-cows/description/

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

*/

class Solution {
public:
    string getHint(string secret, string guess) {
        
        int bulls = 0, cows = 0,i;

        vector<int> secret_freq(10,0);
        vector<int> guess_freq(10,0);

        for(i=0;i<secret.length();i++)
        {
            if(secret[i] == guess[i])
                bulls++;
            else
            {
                secret_freq[secret[i]-'0']++;
                guess_freq[guess[i]-'0']++;
            }
        }

        for(i=0;i<10;i++)
            cows += min(secret_freq[i],guess_freq[i]);
       
        string res = to_string(bulls) + 'A' + to_string(cows)+ 'B';

        return res;

    }
};
