

# def create_phone_number(n):
#     n = [str(i) for i in n]
#     partOne = "(" + "".join(n[:3]) + ")"
#     partTwo = "".join(n[3:6]) + "-" + "".join(n[-4:])

#     return partOne + " " + partTwo


# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# # "(123) 456-7890"


# def dirReduc(arr):
#     stack = []

#     dictHash = {
#         "SOUTH": "NORTH",
#         "NORTH": "SOUTH",
#         "EAST": "WEST",
#         "WEST": "EAST",
#     }

#     for d in arr:
#         if d in dictHash:
#             if stack and stack[-1] == dictHash[d]:
#                 stack.pop()
#             else:
#                 stack.append(d)

#     print(stack)
#     return stack


# dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])


# def two_sum(numbers, target):
#     diffHash = {}

#     for i, n in enumerate(numbers):
#         diff = target - n
#         if diff in diffHash:
#             return [diffHash[diff], i]

#         # saving the current number instead of diff
#         diffHash[n] = i

#     return

# print(two_sum([1, 2, 3], 4))

# (sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])
# (sorted(two_sum([2, 2, 3], 4)), [0, 1])

# def tribonacci(signature, n):
#     res = signature
#     if (len(signature) > n):
#         return signature[:n]
#     for i in range(n - len(signature)):
#         next = res[i] + (res[i + 1]) + (res[i + 2])
#         res.append(next)

#     return res


# print(tribonacci([300, 200, 100], 0))

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
