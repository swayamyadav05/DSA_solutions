""" 
125. Valid Palindrome
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""


def isPalindrome(s: str) -> bool:
    def clean_string(s):
        return "".join(c.lower() for c in s if c.isalnum())

    cleaned_s = clean_string(s)

    return cleaned_s == cleaned_s[::-1]


import re


def isPalindrome1(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lower case
    clean_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
    print(isPalindrome(" "))
