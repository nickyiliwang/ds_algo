# ZIP
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)

print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# sorted()
numbers = [2, 4, 5, 6, 2, 4, 3, 5]
sortedNumbers = sorted(numbers)

print("sorted numbers", sortedNumbers)  # O(nlogn)

# Will only combine the lower of the two
numbers = [1, 2, 3, 4, 5, 6, 7, 8]  # 4 - 8 is ignored
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)

print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# ABS
# returns the absolute value of a number
print(abs(-123))

# GET
# add a key val pair with a default value
listA = ["a", "a", "b", "c"]
hash = {}
for c in listA:
    hash[c] = hash.get(c, 0) + 1
print(hash)

# ORD
# Return the Unicode for a string.
# reference groupAnagrams for example
print(ord("a"), ord("b"), ord("c"))

# [::-1]
# reversing an array
listX = [1, 2, 3, 4, 5, 6]
print(listX[::-1])
