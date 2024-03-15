n = int(input())
s = set(int(x) for x in input().split(" "))

sumToN = 0

for i in range(n):
    sumToN += i + 1

for num in s:
    sumToN -= num

print(sumToN)
