# Referencing (Lewin, 2012; Stanford CS103) 4 properties of XOR

# 1) Input order independence: A XOR B = B XOR A

# 2) Chained out of order: A XOR ( B XOR C ) = ( A XOR B ) XOR C

# 3) XORing zero changes nothing: A XOR 0 = A

# 4) Self-inverting: A XOR A = 0

# Even First number
# Output (0 to n)
# ---------------
# (0 to 4) 0100 (4) # n
# (0 to 5) 0001 (1) # 1
# (0 to 6) 0111 (7) # n + 1
# (0 to 7) 0000 (0) # zero

# Odd First number
# Output (0 to n)
# ---------------
# (1 to 1) 0001 (1) # 1
# (1 to 2) 0011 (3) # n + 1
# (1 to 3) 0000 (0) # zero
# (0 to 8) 1111 (0) # n

# 0001 ^ 0011
# 0000


def solution(start, length):
    checksum = 0

    # 17 18 19 20 /
    # 21 22 23 / 24
    # 25 26 / 27 28
    # 29 / 30 31 32
    def XORCalculator(first, last):
        if first % 2 == 0:
            pattern = [last, 1, last + 1, 0]
        else:
            pattern = [first, first ^ last, first - 1, (first - 1) ^ last]

        return pattern[
            (last - first) % 4
        ]  # using remainder to get index, also since pattern repeats every 4 times

    for id in range(length):
        # 17 + 4 x 0 = 17
        # 17 + (4 - 0) -1 = 20

        # 17 + (4 * 1) = 21
        # 21 + (4 - 1) - 1 = 23
        first = start + (length * id)
        last = first + (length - id) - 1

        checksum ^= XORCalculator(first, last)

    return checksum

    # recursion isn't idea because we don't need to figure out all the numbers, just the first and last in the row
    # def checksumCalculator(
    #     start,
    #     list,
    #     loops,
    #     length,
    # ):
    #     if loops == 0:
    #         return list

    #     temp = []

    #     for i in range(length + 1):
    #         if i == loops:
    #             temp.append("/")
    #         else:
    #             temp.append(start)
    #             start += 1

    #     for num in temp:
    #         if num == "/":
    #             break
    #         list.append(num)

    #     return checksumCalculator(start, list, loops - 1, length)

    # checksumCalculator(
    #     start,
    #     [],
    #     length,
    #     length,
    # )


print(solution(0, 3))


# # ??
# def xor(n):
#     val = n % 4
#     if val == 0:
#         return n
#     if val == 1:
#         return 1
#     if val == 2:
#         return n + 1
#     return 0


# def solution(start, length):
#     res = 0
#     st = start - 1

#     for i in range(length):
#         sp = st + length - i
#         res ^= xor(st) ^ xor(sp)
#         st = sp + i

#     return res
