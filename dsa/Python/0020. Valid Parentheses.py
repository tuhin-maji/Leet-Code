"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


(Runtime: 28 ms, faster than 99.01% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.)

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in match:
                if len(stack)==0:
                    return False
                elif match[ch]!=stack.pop():
                    return False
            else:
                stack.append(ch)
        if len(stack)==0:
            return True
        else:
            return False
