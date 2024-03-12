# Sliding window

# 1. creating a window which can either be an array or number from one position to another
# 2. Depending on conditions, the window either increases or closes, and a new window is created

# Good for:
# keeping track of a subset of data in an array/string


def maxSubArraySum(numList, num):
    maxSum = 0
    tempSum = 0
    if len(numList) < num:
        return None

    for i in range(num):
        maxSum += numList[i]

    #  we get the initial window
    #  1, 2, 3 => 6
    #  tempSum will start as 6
    tempSum = maxSum

    for i in range(len(numList)):
        # for each new number, subtract the old number
        # [1,2,3] => [2,3,4]
        # tempSum = 6 - 1 + 4
        # tempSum = maxSum starting point - arr[3 - 3] + arr[3]
        tempSum = tempSum - numList[i - num] + numList[i]

        maxSum = max(maxSum, tempSum)

    return maxSum


print(maxSubArraySum([1, 2, 3, 4, 5, 6, 7], 3))
