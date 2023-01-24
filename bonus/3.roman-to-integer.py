def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res

def romanToInt(s: str) -> int:
    romanNumerals = {
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000,
    }

    countStack = []
    res = []
    for n in s:
        # # if the previous symbol is smaller than the current one, it will become negative, and we pop it
        if countStack and romanNumerals[countStack[-1]] < romanNumerals[n]:
            res.append(romanNumerals[n] - romanNumerals[countStack[-1]])
            countStack.pop()
        else:
            countStack.append(n)

    if countStack:
        for n in countStack:
            res.append(romanNumerals[n])

    return sum(res)


s = "MCMXCIV"
# Output: 1994
romanToInt(s)

# one pass solution

def romanToInt(s: str) -> int:
    romanNumerals = {
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000,
    }

    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and romanNumerals[s[i]] < romanNumerals[s[i + 1]]:
            res -= romanNumerals[s[i]]
        else:
            res += romanNumerals[s[i]]

    return sum(res)
