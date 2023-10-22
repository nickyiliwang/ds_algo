def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while right > left and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right += 1

    return True


# Explanation
# Key: remember isalnum and use a while loop to sift out the non alpha numeric.

# Checking left and right char and moving towards the center.
# If odd, meet center, if even left and right compare, even surpass


def isPalindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        # Skips non alpha numeric characters
        while l < r and not s[l].isalnum():
            l += 1

        while r > l and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        # moving the pointer
        l, r = l + 1, r - 1

    return True


# #  This solution is using python built in isalnum, and uses extra memory by building an string and array.
# # Time: O(n), Space: O(n)
# def solution(s):
#     newStr = ""

#     for c in s:
#         # is alpha numeric
#         if c.isalnum():
#             newStr += c.lower()

#     # [::-1] is a pythonic way to reverse a list
#     return newStr == newStr[::-1]

# s = "A man, a plan, a canal: Panama"
# print(solution(s))

# def pointer_solution(s):
#     l, r = 0, len(s) - 1

#     # left and right haven't met
#     while l < r:
#         # this checks that left/right will not pass each other
#         # and makes sure it's a alpha numeric char
#         # else it's going to increment/decrement until it is.
#         while l < r and not alphaNum(s[l]):
#             l += 1

#         # see above
#         while r > l and not alphaNum(s[r]):
#             r -= 1

#         # left and right not equal, not palindrome
#         if s[l].lower() != s[r].lower():
#             return False

#         # moving the pointer
#         l, r = l + 1, r - 1

#     return True

# def alphaNum(c):
#     # using ASCii and ord function we are checking if:
#     # Upper case, lower case, or number ?
#     # if not, it is not alphaNumeric
#     return (ord('A') <= ord(c) <= ord("Z") or ord('a') <= ord(c) <= ord("z")
#             or ord('0') <= ord(c) <= ord("9"))

# s = "A man, a plan, a canal: Panama"
# print(pointer_solution(s))

# # # My solution, Hey you are pretty good!
# # import re

# # def solution(s):
# #     clean = re.sub("[^A-Za-z0-9]", '', s).lower()
# #     reverse = []
# #     for i in range(len(clean) - 1, -1, -1):
# #         reverse.append(clean[i])

# #     res = ''.join(reverse)

# #     return True if res == clean else False

# # s = "A man, a plan, a canal: Panama"
# # print(solution(s))
