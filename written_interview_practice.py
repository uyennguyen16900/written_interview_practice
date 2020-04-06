# Problem 1:
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21


def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    # naive solution:
    # We can repeatedly pop the last digit off of x using mod 10 and division and push it to the back of the reverse of the x
    # handle negative number

    # second solution:
    # handle negative number
    if x < 0:
        # convert x to string and reverse it, then convert it back to int
        num = -int(str(x)[:0:-1])
    # handle positive number
    else:
        num = int(str(x)[::-1])
    # check if the reversed integer is within the 32-bit signed integer range [-2^31, 2^31 - 1]
    if num > 2**31 - 1 or num < -2**31:
        # return 0 when the reversed integer overflows
        return 0

    return num


# Problem 2:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # create a stack to keep track of opening brackets
    stack = []

    # create a dict to make adding more brackets easier
    d = {"(":")", "{":"}", "[":"]"}
    # for every bracket in s
    for element in s:
        # if the bracket is an opening bracket
        if element in set(["(", "[", "{"]):
            stack.append(element)
        # if the bracket is an closing bracket and does match
        elif stack and element == d[stack[-1]]:
            # pop the topmost element from the stack, if it is not empty
            stack.pop()
        # elemnt of the stack don't match, return False
        else:
            return False
    # if the stack is empty, then we have a valid expression
    return stack == []
