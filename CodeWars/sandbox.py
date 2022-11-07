def tribonacci(signature, n):
    res = signature
    for i in range(n - len(signature)):
        res = i + (res)


tribonacci([1, 1, 1], 10)

# # fib with memo in python
# memo = {}

# def fib(n):
#     if (n <= 2):
#         return 1
#     if n not in memo:
#         memo[n] = fib(n - 1) + fib(n - 2) + fib(n - 3)
#     return memo[n]

# print(fib(50))

# def tribonacci(signature, n):

# def high_and_low(numbers):
#     nums = numbers.split(" ")
#     high = int(nums[0])
#     low = int(nums[0])
#     for s in nums:
#         high = max(high, int(s))
#         low = min(low, int(s))

#     res = str(high) + " " + str(low)

#     print(res)
#     return res


# high_and_low("1 2 3 4 5")  # return "5 1"
# # high_and_low("1 2 -3 4 5")  # return "5 -3"
# # high_and_low("1 9 3 4 -5") # return "9 -5"


# # return masked string
# def maskify(cc):
#     lastFour = cc[-4:]
#     res = "" + "#" * (len(cc) - 4) + lastFour
#     return res

# maskify("Nananananananananananananananana Batman!")
