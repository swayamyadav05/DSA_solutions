""" 
Problem statement
Determine if a given string ‘S’ is a palindrome using recursion. Return a Boolean value of true if it is a palindrome and false if it is not.

Note: You are not required to print anything, just implement the function. Example:
Input: s = "racecar"
Output: true
Explanation: "racecar" is a palindrome.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
abbba
Sample Output 1:
true
Explanation Of Sample Input 1 :
“abbba” is a palindrome

Sample Input 2:
abcd
Sample Output 2:
false
Explanation Of Sample Input 2 :
“abcd” is not a palindrome.

Constraints:
0 <= |S| <= 10^6
where |S| represents the length of string S.
"""


def isPalindrome(string: str) -> bool:
    # Base case: if the string is empty or has only one character, it is a palindrome
    if len(string) <= 1:
        return True
    # Compare first and last characters
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    else:
        # If the character don't match, it's not a palindrome.
        return False


def isPalindrome1(i: int, string: str) -> bool:
    if i >= len(string) / 2:
        return True
    if string[i] != string[len(string) - i - 1]:
        return False
    return isPalindrome1(i + 1, string)


if __name__ == "__main__":
    print(isPalindrome("madam"))
    print(isPalindrome(" "))
    print(isPalindrome1(0, "madam"))
    print(isPalindrome1(0, " "))
