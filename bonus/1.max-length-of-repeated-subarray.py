# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100


# Old time limit exceeding approach
def findLength(nums1, nums2):
    res = 0
    N, M = len(nums1), len(nums2)
    # https://stackoverflow.com/a/6667288
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if (nums1[i-1] == nums2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(dp[i][j], res)

    # https://stackoverflow.com/a/50257693
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in dp]))

    # 0       0       0       0       0       0
    # 0       1       1       1       1       1
    # 0       1       2       2       2       2
    # 0       1       2       3       3       3
    # 0       1       2       3       4       4
    # 0       1       2       3       4       5

    print(res)
    return res


nums1 = [0, 0, 0, 0, 0]
nums2 = [0, 0, 0, 0, 0]

findLength(nums1, nums2)
