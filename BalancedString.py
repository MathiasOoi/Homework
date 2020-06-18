import unittest
import time
import functools

class TestisValid(unittest.TestCase):
    def test_balanced(self):
        self.assertTrue(isValid("()()"))
        self.assertTrue(isValid("(())"))
        self.assertTrue(isValid("()"))
        self.assertTrue(isValid(""))

    def test_not_balanced(self):
        self.assertFalse(isValid("("))
        self.assertFalse(isValid("())"))
        self.assertFalse(isValid("((())"))
        self.assertFalse(isValid(")("))


def isValid(s):
    """
    :param s: String of "(" and ")"
    :return: Return True if the string is balanced else False
    """
    openCount, closeCount = 0, 0
    for char in s:
        if char == "(":
            openCount += 1
        if char == ")":
            closeCount += 1
        if closeCount > openCount:
            return False
    return closeCount == openCount


def solve(n, openCount=0, closeCount=0):
    """
    :param n: Integer
    :param currString: The current string you have
    :param openCount: Count of "(" in currString
    :param closeCount: Count of ")" in currString
    :return: Returns number of balanced strings of length 2n
    """
    if openCount + closeCount == 2 * n:
        # Check if the string is of length 2n
        if openCount == closeCount:
            return 1
        return 0
    if closeCount > openCount:
        return 0
    return solve(n, openCount + 1, closeCount) + solve(n, openCount,closeCount + 1)

@functools.lru_cache(1000)
def solve_memo_cheat(n, openCount=0, closeCount=0):
    """
    :param n: Integer
    :param openCount: Count of open paren
    :param closeCount: Count of close paren
    :return: Returns number of balanced strings of length 2n
    """
    if openCount + closeCount == 2 * n:
        # Check if the string is of length 2n
        if openCount == closeCount:
            return 1
        return 0
    if closeCount > openCount:
        return 0
    return solve_memo_cheat(n, openCount + 1, closeCount) + solve_memo_cheat(n, openCount,closeCount + 1)

def solve_memo(n, cache, openCount=0, closeCount=0):
    """
    :param n: Integer
    :param cache: Dictionary that maps tuple of (openCount, closeCount) result (simulate memoization)
    :param openCount: Count of open paren
    :param closeCount: Count of close paren
    :return:Returns number of balanced strings of length 2n
    """
    if (openCount, closeCount) in cache:
        return cache[(openCount, closeCount)]
    elif openCount + closeCount == 2 * n:
        # Check if the string is of length 2n
        if openCount == closeCount:
            return 1
        cache[(openCount, closeCount)] = 0
        return 0
    elif closeCount > openCount:
        cache[(openCount, closeCount)] = 0
        return 0
    result = solve_memo(n, cache, openCount + 1, closeCount) + solve_memo(n, cache, openCount, closeCount + 1)
    cache[(openCount, closeCount)] = result
    return result

def genPairs(n):
    for i in reversed(range((2*n)+1)):
        for k in reversed(range((2*n)-i+1)):
            if i + k <= 2*n+1 and k < i + 2:
                yield (i, k)

def solve_iter(n):
    total = 0
    for pair in genPairs(n):
        pass


def test(func, i):
    # Helped function to use the multiple methods to solve balanced strings
    start = time.time()
    print(str(func).split()[1] if str(func).split()[1] != "object" else "solve_memo_cheat")
    print("n = " + str(i))
    print("Solution: " + (str(func(i)) if str(func).split()[1] != "solve_memo" else str(func(i, dict()))))
    print("Time: " + str(time.time() - start))
    print()

if __name__ == "__main__":
#    unittest.main(exit=False)
#    for i in range(13):
#        for func in [solve, solve_memo, solve_memo_cheat]:
#            test(func, i)
    c = {}
    print(solve_memo(5, c))
    print(c)
    u = {}
    for key, value in c.items():
        if value:
            u[key] = value
    print(u)
    for i in genPairs(5):
        print(i)
