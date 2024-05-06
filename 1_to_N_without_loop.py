""" 
Problem statement
You are given an integer 'n'.



Your task is to return an array containing integers from 1 to 'n' (in increasing order) without using loops.



Example:
Input: 'n' = 5

Output: 1 2 3 4 5

Explanation: An array containing integers from '1' to 'n' is [1, 2, 3, 4, 5].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5
Sample Output 1 :
1 2 3 4 5
Explanation Of Sample Input 1:
The array contains all integers from 1 to 5 in ascending order.
Sample Input 2:
2
Sample Output 2:
1 2
Explanation Of Sample Input 2:
The array contains all integers from 1 to 2 in ascending order.
Expected Time Complexity:
The expected time complexity is O(n), where 'n' is the given integer.
Constraints:
1 <= n <= 10^6

Time Limit: 1-sec

"""


def printNos(x: int) -> list[int]:
    if x == 0:
        return []
    else:
        result = printNos(x - 1)
        result.append(x)
        return result


def main():
    n = int(input())
    print(printNos(n))


if __name__ == "__main__":
    main()
