# LSB is zero

# xx1 last 3 bit patterns

# 001 => Subtraction is better
# 011 => when n is 3: then subtraction is better, else addition is better
# 111 => Addition is better
# 101 => Subtraction is better


def solution(n):
    ops = 0
    n = int(n)

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n - 1 if (n == 3 or n % 4 == 1) else n + 1

        ops += 1

    return ops


print(solution("15"))
# solution("12")
# print(solution("4"))
