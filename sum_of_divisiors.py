# Sum of all divisors
""" 
Problem statement
You are given an integer 'n'.



Function 'sumOfDivisors(n)' is defined as the sum of all divisors of 'n'.



Find the sum of 'sumOfDivisors(i)' for all 'i' from 1 to 'n'.



Example:
Input: 'n'  = 5

Output: 21

Explanation:
We need to find the sum of 'sumOfDivisors(i)' for all 'i' from 1 to 5. 
'sumOfDivisors(1)' = 1
'sumOfDivisors(2)' = 2 + 1 = 3
'sumOfDivisors(3)' = 3 + 1 = 4
'sumOfDivisors(4)' = 4 + 2 +1 = 7 
'sumOfDivisors(5)' = 5 + 1 = 6
Therefore our answer is sumOfDivisors(1) + sumOfDivisors(2) + sumOfDivisors(3) + sumOfDivisors(4) + sumOfDivisors(5) = 1 + 3 + 4 + 7 + 6 = 21.

Sample Input 1:
3


Sample Output 1:
8


Explanation of sample output 1:
We need to find sumOfDivisors(1) + sumOfDivisors(2) +sumOfDivisors(3).
sumOfDivisors(1) = 1
sumOfDivisors(2) = 2 + 1 = 3
sumOfDivisors(3) = 3 + 1 = 4
Therefore, the answer is sumOfDivisors(1) + sumOfDivisors(2) + sumOfDivisors(3) = 1 + 3 + 4 = 8. 

Sample Input 2:
10


Sample Output 2:
87


Expected Time Complexity:
Try to solve this in O(sqrt('n')).


Constraints:
1 <= 'n' <= 3*10^4

Time Limit: 1 sec

"""


def sum_of_all_divisors(n: int) -> int:
    # Function to calculate the sum of the divisors of a number
    def divisor_sum(num):
        # Initialize the sum
        div_sum = 1
        p = 2

        # Find prime factor and their exponents
        while p * p <= num:
            if num % p == 0:
                exp = 0
                while num % p == 0:
                    num //= p
                    exp += 1
                div_sum *= (pow(p, exp + 1) - 1) // (p - 1)
            if p == 2:
                p = 3
            else:
                p += 2

        # If num is prime
        if num > 1:
            div_sum *= (pow(num, 2) - 1) // (num - 1)

        return div_sum

    # Sum of divisors of numbers from 1 to n
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += divisor_sum(i)

    return total_sum


# n = int(input())
print(sum_of_all_divisors(3))
print(sum_of_all_divisors(10))
