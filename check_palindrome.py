""" 
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


def isPalindrome(x: int) -> bool:
    # INT_MAX = 2**31 - 1
    # INT_MIN = -(2**31)

    # if x < INT_MIN or x > INT_MAX:
    #     return False
    # # Special cases:
    # # 1. Negative numbers are not palindrome
    # # 2. Any number ending with 0 is not a palindrome
    # if x < 0 or (x % 10 == 0 and x != 0):
    #     return False

    # reversed_num = 0
    # original_num = x

    # # Reversing half of the numbers
    # while x > reversed_num:
    #     reversed_num = reversed_num * 10 + x % 10
    #     x //= 10

    # # For even number of digits, both halves should be equal
    # # For odd number of digits, the middle digit can be ignored
    # return x == reversed_num or x == reversed_num // 10

    # If can be done by changing in string
    x = str(x)
    return x == x[::-1]


x = int(input())
print(isPalindrome(x))
