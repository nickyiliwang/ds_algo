# Problem: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode

# Example(s):

# Example1

# Input: [“lint”,“code”,“love”,“you”] Output: [“lint”,“code”,“love”,“you”] Explanation: One possible encode method is: “lint:;code:;love:;you”

# Example2

# Input: [“we”, “say”, “:”, “yes”] Output: [“we”, “say”, “:”, “yes”] Explanation: One possible encode method is: “we:;say:;:::;yes”

# Space: O(n) Time: O(n)


def encode(strs):
    res = ''
    for word in strs:
        res = res + str(len(word)) + "#" + word  # "#" is the delimiter
    return res


# neetcode


def decode(str):
    res = []
    # i variable is the character index
    i = 0

    # before we reach the length of the string
    while i < len(str):
        # start at the position of i
        j = i
        # before we reach the delimiter "#"
        while str[j] != "#":
            j += 1
        # length variable can get double or triple digit word lengths
        # str[start:stop] <= does not include stop
        # that's why we did j += 1 in above 
        length = int(str[i:j])
        print("length", length)
        # we do j + 1 becasue we are skipping the "#" delimiter
        # the word is start: j + 1, and end: j + 1 + length
        res.append(str[j + 1:j + 1 + length])
        # like my own solution, char index will restart at last end
        i = j + 1 + length
    print(res)
    return res


# # Space: O(n) Time: O(n)
# # My solution with while loop
# # THIS DOES NOT WORK WHEN we have over 10 letters
# # ie. 10#asdfghjkli4#code4#love3#you

# def decode(str):
#     res, i = [], 0
#     print(str)
#     while i < len(str):
#         # empty string edge case
#         if str[i] == "0":
#             i += 2
#             res.append('')

#         else:
#             start = i + 2  # 2 is the number + #
#             stop = start + int(str[i])  # int(str[i]) is
#             word = str[start:stop]  # get the word with start and stop
#             res.append(word)
#             i = stop  # get to the next index with a number indicating next word length
#     print(res)
#     return res

# my solution before checking solution, while loop if preferred with explicit index value
# def decode(str):
#     # print(str[2:4:1][0])
#     res = []
#     print(str)
#     step = 2
#     start = 0
#     for i in range(start, len(str), step):
#         if(str[i] == 0):
#             res.append("")
#             step = 2
#             start += 2
#         else:
#             # string[start:end:step]
#             res.append(str[])
#     return res

strs = [
    "asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4asdfghjkli4",
    "code", "love", "you"
]
str = encode(strs)
print("encoded", str)
# OUTPUT single string
decode(str)
# OUTPUT ["", "we", "#say", ":", "yes"]

# watching event horizon while trying to debug my code is not the best way to focus
