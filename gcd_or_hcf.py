""" 
Problem statement
You are given two integers 'n', and 'm'.



Calculate 'gcd(n,m)', without using library functions.



Note:
The greatest common divisor (gcd) of two numbers 'n' and 'm' is the largest positive number that divides both 'n' and 'm' without leaving a remainder.


Example:
Input: 'n' = 6, 'm' = 4

Output: 2

Explanation:
Here, gcd(4,6) = 2, because 2 is the largest positive integer that divides both 4 and 6.

Sample Input 1:
9 6


Sample Output 1:
3


Explanation of sample output 1:
gcd(6,9) is 3, as 3 is the largest positive integer that divides both 6 and 9.

Sample Input 2:
2 5


Sample Output 2:
1


Expected Time Complexity:
Try to solve this in O(log(n)) 


Constraints:
0 <= 'n' <= 10^5

Time Limit: 1 sec

"""


# Brute force approach
def calcGDC(n: int, m: int) -> int:
    gcd = 1
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    return gcd


if __name__ == "__main__":
    # n, m = int(input()), int(input())
    gcd = calcGDC(n, m)
    # print(gcd)

""" Time Complexity: O(min(N1, N2)) where N1 and N2 is the input number. The algorithm iterates from 1 to the minimum of N1 and N2 and each iteration checks whether both the numbers are divisible by the current number (constant time operations).

Space Complexity: O(1)as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is required to store the integer variables. """


# Better approach
def calcGDC1(n: int, m: int) -> int:
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i
    return 1


""" """


def main():
    n = int(input())
    m = int(input())
    gcd = calcGDC1(n, m)
    print(gcd)


if __name__ == "__main__":
    main()


""" Time Complexity: O(min(N1, N2)) where N1 and N2 is the input number. The algorithm iterates from the minimum of N1 and N2 to 1 and each iteration checks whether both the numbers are divisible by the current number (constant time operations).

Space Complexity: O(1) as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is required to store the integer variables. """

# Optimal Approach
# The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers. It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.


def calcGDC2(n: int, m: int) -> int:
    while n > 0 and m > 0:
        if n > m:
            n %= m
        else:
            m %= n
    if n == 0:
        return m
    return n


def main():
    n = int(input())
    m = int(input())

    gcd = calcGDC2(n, m)
    print(gcd)


if __name__ == "__main__":
    main()

""" Time Complexity: O(min(N1, N2)) where N1 and N2 is the input number. The algorithm iterates from the minimum of N1 and N2 to 1 and each iteration checks whether both the numbers are divisible by the current number (constant time operations).

Space Complexity: O(1) as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is required to store the integer variable """
