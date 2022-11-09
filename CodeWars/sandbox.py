def longest_consec(strarr, k):
    for w in strarr:
                


longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)

# def scramble(s1, s2):
#     s1Hash, s2Hash = {}, {}
#     res = True
#     for n in s1:
#         s1Hash[n] = s1Hash.get(n, 0) + 1
#     for n in s2:
#         s2Hash[n] = s2Hash.get(n, 0) + 1

#     for p in s2Hash:
#         if (p in s1Hash and s1Hash[p] >= s2Hash[p]):
#             res = True
#         else:
#             res = False
#             return res

#     return res

# scramble('rkqodlw', 'world')
# ==> True
# scramble('cedewaraaosscodewarsoqqyt', 'codewars')
# ==> True
# print(
#     scramble('djkggcxapezrlc', 'elldcz')
# )
# ==> False

# def tribonacci(signature, n):
#     res = signature
#     for i in range(n - len(signature)):
#         res = i + (res)


# tribonacci([1, 1, 1], 10)

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

# # reverse words

# def reverse_words(text):
#     res = ""
#     textList = text.split(" ")
#     for word in textList:
#         for i in range(len(word)-1, -1, -1):
#             temp = ""
#             temp += text[i]
#         word = temp
#     print(textList)
#     return (" ").join(textList)


# text = "d c b a"
# reverse_words(text)
# # "This is an example!" ==> "sihT si na !elpmaxe"
# # "double  spaces"      ==> "elbuod  secaps"
