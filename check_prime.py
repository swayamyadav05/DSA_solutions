""" 
A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.



You are given a number 'n'.



Find out whether 'n' is prime or not.



Example :
Input: 'n' = 5

Output: YES

Explanation: 5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.


Sample Input 1:
5


Sample Output 1:
YES


Explanation of sample input 1 :
5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.


Sample Input 2:
6


Sample Output 2:
NO


Explanation of sample input 2 :
6 is divisible by 1, 2, 3, and 6. Therefore it is not a prime number.
Numbers having more than two factors are known as composite numbers.


Sample Input 3:
1


Sample Output 3:
NO


Explanation of sample input 3 :
1 is divisible only by 1, having only one factor. Therefore it is not a prime number.
1 is neither a prime nor a composite number.


Expected time complexity :
The expected time complexity is O(sqrt('n')).


Constraints :
1 <= 'n' <= 10 ^ 9

Time limit: 1 second
"""

# Brute Force Approach
# def checkPrime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1

#     if count == 2:
#         return True

#     else:
#         return False


# Optimal Approach
import math


def checkPrime(n):
    # Initialize a counter variable to count the number of factors.
    count = 0
    # Loop through numbers from 1 to the square root of n.
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If n is divisible by i without any remainder.
            count += 1  # Increment the counter.
            if n // i != i:  # If n is not perfect square, count its reciprocal factor.
                count += 1

    if count == 2:
        return True
    else:
        return False


def main():
    n = int(input())
    isPrime = checkPrime(n)
    if isPrime:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()


# if __name__ == "__main__":
#     n = int(input())
#     isPrime = checkPrime(n)
#     if isPrime:
#         print("YES")
#     else:
#         print("NO")
