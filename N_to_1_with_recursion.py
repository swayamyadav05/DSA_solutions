"""
Problem statement
You are given an integer 'n'.



Your task is to return an array containing integers from 'n' to '1' (in decreasing order) without using loops.



Note:
In the output, you will see the array returned by you.
Example:
Input: 'n' = 5

Output: 5 4 3 2 1

Explanation: An array containing integers from 'n' to '1' is [5, 4, 3, 2, 1].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5
Sample Output 1 :
5 4 3 2 1
Explanation Of Sample Input 1:
Input: 'n' = 5

Output: 5 4 3 2 1

Explanation: An array containing integers from '5' to '1' is [5, 4, 3, 2, 1].
Sample Input 2:
2
Sample Output 2:
2 1
Explanation Of Sample Input 2:
Input: 'n' = 2

Output: 2 1

Explanation: An array containing integers from '2' to '1' is [2, 1].
Expected Time Complexity:
The expected time complexity is O(n), where 'n' is the given integer.
Expected Space Complexity:
The expected space complexity is O(n), where 'n' is the given integer.
Constraints:
1 <= n <= 10^4

Time Limit: 1-sec 
"""

from typing import List


def printNos(x: int, result: List[int] = None) -> List[int]:
    if result is None:
        result = []

    if x == 0:
        return result
    else:
        result.append(x)
        return printNos(x - 1, result)


def main():
    n = int(input())
    print(printNos(n))


if __name__ == "__main__":
    main()
