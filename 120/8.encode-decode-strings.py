# https://neetcode.io/problems/string-encode-and-decode
# Key
# Use a delimiter

def encode(strs):
    res = ""
    for word in strs:
        res += str(len(word)) + "#" + word
    return res


def decode(str):
    res = []
    i = 0

    while i < len(str):
        j = i

        while str[j] != "#":
            j += 1

        charLen = int(str[i:j])
        res.append(str[j + 1 : j + 1 + charLen])

        i = j + 1 + charLen

    return res


strs = [
    "I",
    "love",
    "you",
]
str = encode(strs)
print(str)
print(decode(str))

