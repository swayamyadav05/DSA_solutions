"""Problem statement
You are given a number 'n'.



Find the number of digits of 'n' that evenly divide 'n'.



Note:
A digit evenly divides 'n' if it leaves no remainder when dividing 'n'.


Example:
Input: 'n' = 336

Output: 3

Explanation:
336 is divisible by both '3' and '6'. Since '3' occurs twice it is counted two times.
Note:
You don't need to print anything. Just implement the given function.
"""


def countDigits(n: int) -> int:
    count = 0
    for digit in str(n):
        if digit != "0" and n % int(digit) == 0:
            count += 1
    return count


n = int(input("Enter number: "))
result = countDigits(n)
print(result)
