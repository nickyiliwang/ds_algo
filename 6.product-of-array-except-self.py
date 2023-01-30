# Time: O(n) Memory: O(n) | O(1)
def productExceptSelf(nums):
    res = [1] * len(nums)
    prefix = 1

    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1

    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

# Explanation
def productExceptSelf(nums):
    res = [1] * len(nums)
    prefix = 1

    # create prefix in res array
    for i in range(len(nums)):
        res[i] = prefix
        # Keep prefix updated
        prefix *= nums[i]

    postfix = 1

    # create postfix in prefix (res) array
    # from last element going backwards one by one, stop before -1 which is 0
    for i in range(len(nums) - 1, -1, -1):
        # multiply prefix with postfix
        res[i] *= postfix
        postfix *= nums[i]

    return res

nums = [4, 5, 1, 8, 2]
# [80, 64, 320, 40, 160]
productExceptSelf(nums)

# Without the constrains this problem would be easy, just divide each number with the sum of all the numbers multiplied together.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
# nums: [1,2,3,4]
# prefix: [1,2,6,24]
# postfix: [24,24,12,4]
# calc index: [nums[0] * 1 * postfix[1]] (prefix here is None, but we use 1 to keep it neutral)
# calc: [1*1*24]
# res: [24, 12, 8, 6]

# chars: [a, b, c, d]
# prefix: -> | a | a*b | a*b*c | a*b*c*d |
# postfix: <- | a*b*c*d | b*c*d | c*d | d |

# res[i] = prefix[i - 1] * postfix[i + 1]

# prefix postfix long version with pre/post fix array
def productExceptSelf(nums: List[int]) -> List[int]:
    # So we are at idx 3, prefix [1,2], post fix [4]

    # in the context of this problem
    # this result array does not count for memory complexity
    res = [1] * len(nums)
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    for x in range(len(prefix)):
        # we want to stop before going out of bounds
        if (x + 1 < len(prefix)):
            # prefix * nums number at x idx will be the number in x + 1
            # nums array will stop at last idx in this pass
            prefix[x + 1] = prefix[x] * nums[x]

    # python reverse range with range(len(x) - 1, -1, -1), the stop will stop before -1 meaning it reached 0 idx
    for x in range(len(prefix) - 1, -1, -1):
        if (x > 0):
            postfix[x - 1] = postfix[x] * nums[x]

    for x in range(len(prefix)):
        res[x] = prefix[x] * postfix[x]

    return res

nums = [4, 5, 1, 8, 2]
productExceptSelf(nums)

# brute force
def productExceptSelf(nums: List[int]) -> List[int]:
    res = []

    for x in range(len(nums)):
        sum = 1

        for y in range(len(nums)):
            if (x != y):
                sum = sum * nums[y]
        res.append(sum)
    return res