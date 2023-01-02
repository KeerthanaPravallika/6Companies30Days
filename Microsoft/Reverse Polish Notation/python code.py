'''
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        op = ['+','-','*','/']

        for ele in tokens:
            if ele in op:
                second_ele = stack.pop()
                first_ele = stack.pop()

                if ele == '+':
                    res = first_ele + second_ele
                elif ele == '-':
                    res = first_ele - second_ele
                elif ele == '*':
                    res = first_ele * second_ele
                elif ele == '/':
                    res = first_ele / second_ele
                    if res  < 0:
                        res = ceil(res)
                    else:
                        res = floor(res)
                stack.append(res)
            else:
                stack.append(int(ele))
        return stack[0]
                

        
