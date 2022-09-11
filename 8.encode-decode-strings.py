# Problem: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode

# Example(s):

# Example1

# Input: [“lint”,“code”,“love”,“you”] Output: [“lint”,“code”,“love”,“you”] Explanation: One possible encode method is: “lint:;code:;love:;you”

# Example2

# Input: [“we”, “say”, “:”, “yes”] Output: [“we”, “say”, “:”, “yes”] Explanation: One possible encode method is: “we:;say:;:::;yes”

def encode(strs):
    res = ''
    for word in strs:
        res = res + str(len(word)) + "#" + word
    # print(res)
    return res


def decode(str):
    res, i = [], 0
    print(str)
    while i < len(str):
        print(str[i])
        # empty string edge case
        if str[i] == "0":
            print("zero")
            i += 2
            res.append('')

        else:
            start = i
            stop = start + int(str[i])
            word = str[start + 2:stop]
            print("word", word)
            res.append(word)
            i += stop
    print(i)
    print(res)
    return res

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


strs = ["", "we", "#say", ":", "yes"]
str = encode(strs)
# OUTPUT single string
decode(str)
# OUTPUT ["", "we", "#say", ":", "yes"]
