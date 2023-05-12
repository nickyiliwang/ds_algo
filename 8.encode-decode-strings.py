def encode(strs):
    res = ""
    for word in strs:
        res = res + str(len(word)) + "#" + word
    return res


def decode(str):
    res = []
    i = 0

    while i < len(str):
        j = i

        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1 : j + 1 + length])
        i = j + 1 + length

    return res


# Explanation
# Key: length needs to become an integer before we can use it.
def encode(strs):
    res = ""
    for word in strs:
        # "#" is the delimiter
        res = res + str(len(word)) + "#" + word
    return res


def decode(str):
    res = []
    # char index
    i = 0

    # before we reach the length of the string
    while i < len(str):
        # start at the position of i
        j = i

        # loop till we reach "#" delimiter
        while str[j] != "#":
            j += 1

        # length variable can get double or triple digit word lengths
        # str[start:stop] <= does not include stop
        length = int(str[i:j])

        # we do j + 1 becasue we are skipping the "#" delimiter
        # the word is start: j + 1, and end:  "#" delimiter + length
        res.append(str[j + 1 : j + 1 + length])

        # char index updates at the end of the word
        i = j + 1 + length

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
    "code",
    "love",
    "you",
]
str = encode(strs)
print("encoded", str)
# OUTPUT single string
decode(str)
# OUTPUT ["", "we", "#say", ":", "yes"]


# watching event horizon while trying to debug my code is not the best way to focus
