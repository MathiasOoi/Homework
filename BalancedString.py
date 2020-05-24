import unittest
import time


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


def solve(n, currString="(", openCount=1, closeCount=0):
    """
    :param n: Integer
    :param currString: The current string you have
    :param openCount: Count of "(" in currString
    :param closeCount: Count of ")" in currString
    :return: Returns number of balanced strings of length 2n
    """
    if len(currString) == 2 * n:
        # Check if the string is of length 2n
        if openCount == closeCount:
            return 1
        return 0
    if closeCount > openCount:
        return 0
    return 0 if not n else solve(n, currString + "(", openCount + 1, closeCount) + solve(n, currString + ")", openCount,closeCount + 1)


if __name__ == "__main__":
    unittest.main(exit=False)
    for i in range(5):
        start = time.time()
        print("n = " + str(i))
        print("Solution: " + str(solve(i)))
        print("Time: " + str(time.time() - start))
        print()
