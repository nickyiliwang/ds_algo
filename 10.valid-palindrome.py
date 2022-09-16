# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


# Using pointers
# Meaning checking left and right char and moving towards the center.
# If odd, meet center, if even left and right compare, even surpass
#
def pointer_solution(s):
    # left and right pointers
    l, r = 0, len(s) - 1

    # left and right haven't met or crossed each other
    while l < r:
        # this checks that left/right will not pass each other
        # and makes sure it's a alpha numeric char
        # else it's going to increment/decrement until it is.
        while l < r and not alphaNum(s[l]):
            l += 1

        # see above
        while r > l and not alphaNum(s[r]):
            r -= 1

        # left and right not equal, not palindrome
        if s[l].lower() != s[r].lower():
            return False

        # moving the pointer
        l, r = l + 1, r - 1

    return True


def alphaNum(c):
    # using ASCii and ord function we are checking if:
    # Upper case, lower case, or number ?
    # if not, it is not alphaNumeric
    return (ord('A') <= ord(c) <= ord("Z") or
            ord('a') <= ord(c) <= ord("z") or
            ord('0') <= ord(c) <= ord("9"))


s = "A man, a plan, a canal: Panama"
print(pointer_solution(s))


# #  This solution is using python built in isalnum, and uses extra memory by building an string and array.
# Time: O(n), Space: O(n)
# def solution(s):
#     newStr = ""

#     for c in s:
#         # is alpha numeric
#         if c.isalnum():
#             newStr += c.lower()

#     # python shorthand for reversing a string
#     return newStr == newStr[::-1]


# s = "A man, a plan, a canal: Panama"
# print(solution(s))


# # My solution, Hey you are pretty good!
# import re


# def solution(s):
#     clean = re.sub("[^A-Za-z0-9]", '', s).lower()
#     reverse = []
#     for i in range(len(clean) - 1, -1, -1):
#         reverse.append(clean[i])

#     res = ''.join(reverse)

#     return True if res == clean else False


# s = "A man, a plan, a canal: Panama"
# print(solution(s))
