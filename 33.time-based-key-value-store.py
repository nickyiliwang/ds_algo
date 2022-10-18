# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"


# Constraints:

# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.


class TimeMap:

    def __init__(self):
        self.hashMap = {}  # {key: [[value, timestamp]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key] = self.hashMap.get(
            key, [])
        self.hashMap[key].append([value, timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        # return empty string by default
        res = ''
        # using get here to make sure we can get an value
        # incase empty key
        timeSeries = self.hashMap.get(key, [])
        left, right = 0, len(timeSeries) - 1
        # binary search for logn bigO
        while left <= right:
            middle = (left + right) // 2
            # less than or equal to here
            # so the return value is value associated with the largest timestamp_prev
            # ie. middle = 5, timestamp = 6
            if (timeSeries[middle][1] <= timestamp):
                res = timeSeries[middle][0]
                left = middle + 1
            elif (timeSeries[middle][1] > timestamp):
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
