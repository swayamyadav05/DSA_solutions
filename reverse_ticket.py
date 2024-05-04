"""
Problem statement
There is a song concert going to happen in the city. The price of each ticket is equal to the number obtained after reversing the bits of a given 32 bits unsigned integer 'n'.

Sample Input 1 :
2
0
12
Sample Output 1:
 0
 805306368
Explanation For Sample Input 1 :
For the first test case :
Since the given number N = 0 is represented as 00000000000000000000000000000000 in its binary representation. So after reversing the bits, it will become 00000000000000000000000000000000 which is equal to 0 only. So the output is 0.     



For the second test case :
Since the given number N = 12 is represented as 00000000000000000000000000001100 in its binary representation. So after reversing the bits, it will become 0110000000000000000000000000000, which is equal to 805306368 only. So the output is 805306368.

"""


def reverse(n):
    result = 0
    # Iterate through each bit of n
    for i in range(32):
        # Extract the least significant bit of n
        bit = n & 1

        # Append the extracted bit to the result
        result = (result << 1) | bit

        # Right shift n to move to the next bit of n
        n = n >> 1
    # Return the reversed bit as the price of the ticket
    return result


n = int(input())
print(reverse(n))
