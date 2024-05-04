"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""


def reverse_digit(x: int) -> int:
    INI_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    is_negative = x < 0

    x = abs(x)

    rev = 0

    while x != 0:
        digit = x % 10
        rev = rev * 10 + digit
        x //= 10

    if is_negative:
        rev = -rev

    if rev > INI_MAX or rev < INT_MIN:
        return 0

    return rev


n = int(input("Enter number: "))
result = reverse_digit(n)
print(result)
