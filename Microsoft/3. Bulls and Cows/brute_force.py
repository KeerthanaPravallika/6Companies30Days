'''
Question Link : https://leetcode.com/problems/bulls-and-cows/description/
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

'''


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        no_of_bulls = 0
        bull_index = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                no_of_bulls += 1
                bull_index.append(i)
        
        no_of_cows = 0
        guess = list(guess)
        for i in range(len(secret)):
            if i not in bull_index:
                for j in range(len(guess)):
                    if secret[i] == guess[j] and j not in bull_index:
                        guess[j] = "+"
                        no_of_cows += 1
                        break
        
        return str(no_of_bulls)+"A"+str(no_of_cows)+"B"

        
