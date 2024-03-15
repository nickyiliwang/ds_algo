s = input()

pointer = 0
res = 1

while pointer < len(s):
    if (pointer + 1) < len(s) and s[pointer] == s[pointer + 1]:
        j = pointer
        temp = 1
        while (j + 1) < len(s) and s[j] == s[j + 1]:
            temp += 1
            j += 1
        res = max(temp, res)
        pointer = j

    pointer += 1

print(res)
