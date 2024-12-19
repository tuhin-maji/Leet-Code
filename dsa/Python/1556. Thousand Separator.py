"""
1556. Thousand Separator
Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"


Constraints:

0 <= n <= 231 - 1
"""

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:
            return str(n)
        output=""
        count=1
        while n>0:
            digit=n%10
            n=n//10
            if count%3==0 and n>0:
                output="."+str(digit)+output
            else:
                output=str(digit)+output
            count+=1

        return output
