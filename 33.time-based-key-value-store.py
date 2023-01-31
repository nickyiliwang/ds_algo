class TimeMap:
    def __init__(self):
        self.hashMap = {}  # {key: [[value, timestamp]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key] = self.hashMap.get(key, [])
        self.hashMap[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        database = self.hashMap.get(key, [])
        left, right = 0, len(database) - 1
        # binary search for BigO(log n)
        while left <= right:
            middle = (left + right) // 2
            if database[middle][1] <= timestamp:
                res = database[middle][0]
                left = middle + 1
            elif database[middle][1] > timestamp:
                right = middle - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

obj = TimeMap()
print(obj.set("love", "high", 10))
print(obj.set("love", "low", 20))
print(obj.get("love", 5))
print(obj.get("love", 10))
print(obj.get("love", 15))
print(obj.get("love", 20))
print(obj.get("love", 25))

# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# OUT: [null,null,null,"","high","low","low","low"]
# EXP: [null,null,null,"","high","high","low","low"]
