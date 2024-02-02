def solution(n, b):
    bucket = []
    k = len(n)

    def toBaseNum(num, b):
        if b == 10 or n == 0:
            return str(num)
        baseNum = ""
        while num:
            baseNum += str(num % b)
            num //= b
        return baseNum[::-1]

    while True:
        x = int("".join(sorted(n, reverse=True)), b)
        y = int("".join(sorted(n)), b)
        z = x - y

        n = toBaseNum(z, b)

        while len(n) < k:
            n = "0" + n

        if n in bucket:
            return len(bucket) - bucket.index(n)
        bucket.append(n)


print(solution("210022", 3))
# 210111, 122221, 102212
# print(solution("1211", 10))
