from functools import cache


# 1
class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 2) + self.fib(n - 1)


# 2
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


""" 
the first code snippet (with @cache decorator) optimizes the calculation of Fibonacci numbers by avoiding redundant computations through memoization, while the second code snippet recalculates Fibonacci numbers without any optimization.
"""


""" 
1. The first code snippet utilizes the @cache decorator from the functools module. This decorator memorizes (or caches) the results of function calls. When the function is called with the same arguments again, instead of recalculating the result, it returns the value from the cache. This effectively saves computation time by avoiding redundant calculations. This technique is known as memoization.


2. The second code snippet does not use memoization. It calculates Fibonacci numbers recursively without storing previously computed results. As a result, it may end up recalculating the same Fibonacci numbers multiple times, leading to inefficiency, especially for large values of n.
"""
