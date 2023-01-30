from collections import Counter

# Time: O(n), Memory O(n)
def topKFrequent(nums, k):
    counter = Counter()
    freq = [[] for i in range(len(nums) + 1)]

    res = []
    for n in nums:
        counter[n] += 1

    for n, c in counter.items():
        freq[c].append(n)

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if (len(res)) == k:
                return res


# bucket sort
# def topKFrequent(nums, k):
#     hashMap = {}
#     freq = [[] for i in range(len(nums) + 1)]

#     # https://stackoverflow.com/a/2785963
#     # Be careful this create N copies of the same item
#     # do not do this
#     # same = [[]] * (len(nums) + 1)

#     res = []
#     for n in nums:
#         hashMap[n] = hashMap.get(n, 0) + 1

#     # my original solution
#     # for x in hashMap:
#     #     # for every key in map
#     #     # the bucket tuple will keep the hash value (number of times a number repeated)
#     #     # the bucket index value will be keeping the numbers with the same repeating times + if the key (number) has the same repeated times
#     #     bucket[hashMap[x]] = bucket[hashMap[x]] + [x]

#     # neet code solution
#     # hashMap.items() => [(1, 3), (2, 3), (3, 1), (4, 3]
#     for n, c in hashMap.items():
#         # we are appending
#         freq[c].append(n)

#     # for i in reversed(freq):
#     # uses the value instead of index

#     # range(starting len - 1, to index 0, -1 steps)
#     for i in range(len(freq) - 1, 0, -1):
#         for n in freq[i]:
#             res.append(n)
#             # return once we reach k
#             if (len(res)) == k:
#                 return res


# nums = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4]
# k = 3
# print(topKFrequent(nums, k))


# # # O(n log m) n is the nums, m is the hashMap item
# def topKFrequent(nums, k):
#     hashMap = {}
#     # build a hashMap with:
#     # value:
#     for n in nums:
#         hashMap[n] = hashMap.get(n, 0) + 1

#     # gets the (key, val) pair in a tuple
#     items = hashMap.items()

#     # sorting by the second tuple which was the times repeated, in reverse order
#     sortedItems = sorted(items, key=lambda tup: tup[1], reverse=True)

#     # only take the first index in the tuple, the key, in the sortedItems tuple list, only go up to k index
#     return [s[0] for s in sortedItems[:k]]
