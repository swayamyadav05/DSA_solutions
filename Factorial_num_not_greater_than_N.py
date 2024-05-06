""" 
Problem statement
You are given an integer ’n’.



Your task is to return a sorted array (in increasing order) containing all the factorial numbers which are less than or equal to ‘n’.



The factorial number is a factorial of a positive integer, like 24 is a factorial number, as it is a factorial of 4.



Note:
In the output, you will see the array returned by you.
Example:
Input: ‘n’ = 7

Output: 1 2 6

Explanation: Factorial numbers less than or equal to ‘7’ are ‘1’, ‘2’, and ‘6’.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
7
Sample Output 1 :
1 2 6
Explanation Of Sample Input 1:
Input: ‘n’ = 7

Output: 1 2 6

Explanation: Factorial numbers less than or equal to ‘7’ are ‘1’, ‘2’, and ‘6’.
Sample Input 2:
2
Sample Output 2:
1 2
Explanation Of Sample Input 2:
Input: ‘n’ = 2

Output: 1 2

Explanation: Factorial numbers less than or equal to ‘2’ are ‘1’ and ‘2’.
Expected Time Complexity:
The expected time complexity is O(m), where ‘m’ is the number of factorial numbers which are less than or equal to ‘n’.
Expected Space Complexity:
The expected space complexity is O(m), where ‘m’ is the number of factorial numbers which are less than or equal to ‘n’.
Constraints:
1 <= n <= 10^18

Time Limit: 1-sec
Python (3.5)
12345
from typing import *

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    pass
"""


def factorialNumbers(
    n: int, i: int = 1, factorial: int = 1, result: list[int] = []
) -> list[int]:
    if factorial <= n:
        result.append(factorial)
        return factorialNumbers(n, i + 1, factorial * (i + 1), result)
    else:
        return result


def fact(n: int):
    result = 1
    count = 1
    ans = []
    while result <= n // count:
        result *= count
        count += 1
        ans.append(result)
    return ans


if __name__ == "__main__":
    n = int(input())
    print(factorialNumbers(n))
    print(fact(n))
