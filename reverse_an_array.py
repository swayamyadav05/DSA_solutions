""" 
Problem statement
Given an array 'arr' of size 'n'.



Return an array with all the elements placed in reverse order.



Note:
You don’t need to print anything. Just implement the given function.
Example:
Input: n = 6, arr = [5, 7, 8, 1, 6, 3]

Output: [3, 6, 1, 8, 7, 5]

Explanation: After reversing the array, it looks like this [3, 6, 1, 8, 7, 5].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
8
3 1 1 7 4 2 6 11
Sample Output 1:
11 6 2 4 7 1 1 3    
Explanation Of Sample Input 1 :
After reversing the array, it looks like this [11, 6, 2, 4, 7, 1, 1, 3].
Sample Input 2:
4
8 1 3 2
Sample Output 2:
2 3 1 8
Explanation Of Sample Input 2 :
After reversing the array, it looks like this [2, 3, 1, 8].
Expected time complexity
The expected time complexity is O(n).
Constraints:
1 <= 'n' <= 10^6
-10^9 <= 'arr[i]' <=10^9
"""


def reverse_Array(n: int, nums: list[int]) -> list[int]:
    return reversed(nums)


# OR


def reverseArray(n: int, nums: list[int]) -> list[int]:
    left = 0
    right = n - 1

    while left < right:
        # Swap elements at left and right indices in-place
        nums[left], nums[right] = nums[right], nums[left]
        # Move the pointers towards each other
        left += 1
        right -= 1

    return nums


# OR


def reverseArray(n: int, nums: list[int]) -> list[int]:
    # Base case: If the array is empty or has only one element, return it.
    if n <= 1:
        return nums
    else:
        # Recursively reverse the sublist from index 1 to n-1.
        reversed_sublist = reverseArray(n - 1, nums[1:])
        # Append the first element of the original array to the reversed sublist.
        reversed_sublist.append(nums[0])
        return reversed_sublist


# OR


def swap(arr: list[int], left: int, right: int) -> None:
    """
    Helper function to swap elements in the array.
    """
    if left < right:
        # Swap elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # Recursively call swap on the remaining sublist
        swap(arr, left + 1, right - 1)


def reverseArray(n: int, nums: list[int]) -> list[int]:
    # Call the helper function to swap elements recursively
    swap(nums, 0, n - 1)
    return nums


# OR


def reverseArray(n: int, nums: list[int]) -> list[int]:
    def reverseArrayHelper(i: int) -> None:
        """
        Helper function to reverse the array recursively using swapping.
        """
        if i >= n // 2:
            return
        else:
            # Swap elements at i and (n - i - 1) indices
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
            # Recursively call on the next index
            reverseArrayHelper(i + 1)

    # Call the helper function with initial index 0
    reverseArrayHelper(0)
    return nums


if __name__ == "__main__":
    n = 5
    nums = [1, 5, 2, 1, 6]
    print(reverseArray(n, nums))
