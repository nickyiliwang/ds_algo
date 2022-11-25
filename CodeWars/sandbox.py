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
=======
# def first_non_repeating_letter(string):
#     original = string

#     string = string.lower()
#     hash = {}
#     for c in string:
#         hash[c] = hash.get(c, 0) + 1

#     nonRepeatIndexes = []
#     for t in hash.items():
#         if (t[1] == 1):
#             nonRepeatIndexes.append(string.index(t[0]))

#     if (nonRepeatIndexes):
#         nonRepeatingIndex = min(nonRepeatIndexes)
#         return original[nonRepeatingIndex]
#     else:
#         return ""

# # test.it('should handle simple tests')
# print(first_non_repeating_letter('a'), 'a')
# print(first_non_repeating_letter('stress'), 't')
# print(first_non_repeating_letter('moonmen'), 'e')

# # test.it('should handle empty strings')
# print(first_non_repeating_letter(''), '')

# # test.it('should handle all repeating strings')
# print(first_non_repeating_letter('abba'), '')
# print(first_non_repeating_letter('aa'), '')

# # test.it('should handle odd characters')
# print(first_non_repeating_letter('~><#~><'), '#')
# print(first_non_repeating_letter('hello world, eh?'), 'w')

# # test.it('should handle letter cases')
# print(first_non_repeating_letter('sTreSS'), 'T')
# print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')

# def valid_parentheses(string):
#     validHash = {
#         ")": "("
#     }
#     stack = []
#     for b in string:
#         print(b)
#         if b in validHash:
#             if stack and stack[-1] == validHash[b]:
#                 stack.pop()
#             else:
#                 return False
#         elif b == "(":
#             stack.append(b)

#     return True if not stack else False


# # print(valid_parentheses("()"))
# # # =>  true
# # print(valid_parentheses(")(()))"))
# # # =>  false
# # print(valid_parentheses("("))
# # # =>  false
# # print(valid_parentheses("(())((()())())"))
# # # =>  true
# # print(valid_parentheses('qlgxlqg(knz)b(dwrs)'))
# # # =>  true

# def rgb(r, g, b):
#     res = ""
#     rgb = [r, g, b]
#     hexHash = {
#         10: "A",
#         11: "B",
#         12: "C",
#         13: "D",
#         14: "E",
#         15: "F"
#     }

#     for n in rgb:
#         if (n > 255):
#             n = 255
#         elif (n < 0):
#             n = 0

#         quotient = n // 16
#         remainder = n % 16

#         if (quotient > 9):
#             res = res + str(hexHash[quotient])
#         else:
#             res = res + str(quotient)

#         if (remainder > 9):
#             res = res + str(hexHash[remainder])
#         else:
#             res = res + str(remainder)

#     print(res)
#     return res

# rgb(255, 255, 255)  # returns FFFFFF
# rgb(255, 255, 300)  # returns FFFFFF
# rgb(0, 0, 0)  # returns 000000
# rgb(148, 0, 211)  # returns 9400D3

# def longest_consec(strarr, k):
#     res = ""

#     if (k <= 0 or k > len(strarr)):
#         return res

#     for i in range(len(strarr)):
#         curr_word = "".join(strarr[i:i+k])
#         if (len(curr_word) > len(res)):
#             res = curr_word
#     return res


# longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0)

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
>>>>>>> bf41999c9fa04f1531dc9276f61cf07d03ba3a0b

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
